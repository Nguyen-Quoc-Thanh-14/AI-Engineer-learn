#!/usr/bin/env python3
"""Proof of *physical NVIDIA CUDA execution* on CPython 3.15.2.

Never emit CUDA_HARDWARE_PASS without torch.cuda.is_available() and actual kernels.
"""
import hashlib
import json
import os
import re
import pathlib
import platform
import subprocess
import sys
import time
import traceback

ROOT=pathlib.Path(__file__).resolve().parents[1]
OUT=ROOT/"evidence"/"cuda_3152"/"gpu_runtime.json"
OUT.parent.mkdir(parents=True,exist_ok=True)

def execution_identity():
    """Bind the observation to the checked-out source and the Actions attempt."""
    head=subprocess.run(["git","rev-parse","HEAD"],cwd=ROOT,capture_output=True,
                        text=True,timeout=10,check=True).stdout.strip()
    if not re.fullmatch(r"[0-9a-f]{40}",head):
        raise RuntimeError("Cannot identify the checked-out commit")
    if os.getenv("GITHUB_SHA") and os.environ["GITHUB_SHA"]!=head:
        raise RuntimeError("GITHUB_SHA differs from checked-out commit")
    dirty=subprocess.run(["git","status","--porcelain","--untracked-files=no","--",
                          "tests/gpu_cuda_3152.py",".github/workflows/gpu-self-hosted-3152.yml"],
                         cwd=ROOT,capture_output=True,text=True,timeout=10,check=True)
    if dirty.stdout.strip():
        raise RuntimeError("CUDA collector/workflow differs from committed source")
    return {"commit_sha":head,"repository":os.getenv("GITHUB_REPOSITORY",""),
            "run_id":os.getenv("GITHUB_RUN_ID",""),
            "run_attempt":os.getenv("GITHUB_RUN_ATTEMPT","")}

def run():
    if not __debug__:
        raise RuntimeError("Optimized Python would disable CUDA assertions")
    identity=execution_identity()
    assert sys.implementation.name=="cpython" and sys.version_info[:3]==(3,15,2), sys.version
    assert platform.system()=="Linux" and platform.machine()=="x86_64", platform.platform()
    query=subprocess.run(["nvidia-smi","--query-gpu=name,driver_version,memory.total",
                          "--format=csv,noheader"],capture_output=True,text=True,timeout=20,check=True)
    assert query.stdout.strip(), "nvidia-smi did not report a device"
    import torch
    assert torch.__version__.split("+")[0]=="2.15.0", torch.__version__
    assert torch.version.cuda, "This PyTorch installation is CPU-only"
    assert torch.cuda.is_available(), "NVIDIA driver/CUDA GPU is not available"
    assert torch.cuda.device_count()>=1
    device=torch.device("cuda:0")
    props=torch.cuda.get_device_properties(device)
    capability=torch.cuda.get_device_capability(device)
    assert props.total_memory>0
    # PyTorch 2.15 CUDA 13.x binary wheels no longer support pre-Turing architectures.
    assert capability >= (7,5), ("GPU compute capability below 7.5 is unsupported "
                                  "by pinned PyTorch 2.15 CUDA binaries",capability)
    torch.manual_seed(3152)
    torch.set_num_threads(1)
    # Deterministic analytical gradient on *actual* CUDA tensors.
    cuda_x=torch.tensor([-2.,0.,3.],device=device,requires_grad=True)
    y=(cuda_x*cuda_x).sum()
    y.backward()
    expected=torch.tensor([-4.,0.,6.],dtype=torch.float32)
    torch.testing.assert_close(cuda_x.grad.detach().cpu(),expected,rtol=0,atol=0)
    assert y.device.type=="cuda"
    # CPU/GPU comparison for a separate convolution operator.
    tensor=torch.arange(25,dtype=torch.float32).reshape(1,1,5,5)
    kernel=torch.tensor([[[[1.,0.,-1.],[2.,0.,-2.],[1.,0.,-1.]]]])
    cpu=torch.nn.functional.conv2d(tensor,kernel)
    gpu=torch.nn.functional.conv2d(tensor.to(device),kernel.to(device))
    assert gpu.device.type=="cuda"
    torch.testing.assert_close(gpu.cpu(),cpu,rtol=1e-5,atol=1e-5)
    # Actual device-side training: optimized scalar regression with a nonzero gradient.
    x=torch.tensor([[-2.],[-1.],[0.],[1.],[2.]],device=device)
    labels=2*x+1
    model=torch.nn.Linear(1,1,device=device)
    with torch.no_grad():
        model.weight.zero_();model.bias.zero_()
    opt=torch.optim.SGD(model.parameters(),lr=0.05)
    first=None
    start=time.monotonic()
    for epoch in range(80):
        opt.zero_grad(set_to_none=True)
        loss=((model(x)-labels)**2).mean()
        if first is None:first=float(loss.detach().cpu())
        loss.backward()
        assert model.weight.grad is not None and model.weight.grad.device.type=="cuda"
        opt.step()
    torch.cuda.synchronize()
    final=float(((model(x)-labels)**2).mean().detach().cpu())
    pred=float(model(torch.tensor([[3.]],device=device)).detach().cpu().item())
    assert first==9.0 and final<first*0.01, (first,final)
    assert abs(pred-7.0)<0.1, pred
    report={"status":"CUDA_HARDWARE_PASS",**identity,
        "python":sys.version,"python_version":platform.python_version(),
        "platform":platform.platform(),"platform_system":platform.system(),
        "platform_machine":platform.machine(),"cuda_available":True,
        "torch_version":torch.__version__,"torch_cuda_runtime":torch.version.cuda,
        "device_name":props.name,"device_memory_bytes":props.total_memory,
        "device_compute_capability":list(capability),
        "torch_cuda_arches":torch.cuda.get_arch_list(),
        "nvidia_smi":query.stdout.strip(),
        "analytic_gradient_observed":cuda_x.grad.detach().cpu().tolist(),
        "convolution_cpu_gpu_close":True,
        "initial_mse":first,"final_mse":final,"prediction_x3":pred,
        "elapsed_seconds":round(time.monotonic()-start,4),
        "source_sha256":hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
        "limits":"Single visible GPU, smoke tests of a few CUDA ops and a tiny model; not full-course CUDA certification."}
    return report

def main():
    try: result=run()
    except Exception as ex:
        result={"status":"CUDA_HARDWARE_FAIL","error_type":type(ex).__name__,
                "error":str(ex),"traceback":traceback.format_exc(limit=9),
                "python":sys.version,"source_sha256":hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest()}
    OUT.write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding="utf8")
    print(json.dumps({k:result.get(k) for k in ("status","device_name","initial_mse","final_mse","prediction_x3","error")},ensure_ascii=False))
    return 0 if result["status"]=="CUDA_HARDWARE_PASS" else 1
if __name__=="__main__":raise SystemExit(main())

