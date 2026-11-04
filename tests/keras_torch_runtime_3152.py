#!/usr/bin/env python3
"""Keras/PyTorch/h5py runtime contract for CPython 3.15.2 Linux x86_64."""
from __future__ import annotations
import hashlib
import importlib.metadata as md
import json
import os
from pathlib import Path
import platform
import sys
import tempfile
import traceback

BASE = Path(__file__).resolve().parents[1]
EVIDENCE = BASE / "evidence" / "keras3152"
EVIDENCE.mkdir(parents=True, exist_ok=True)
RESULT = EVIDENCE / "runtime_result.json"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run():
    assert sys.implementation.name == "cpython" and sys.version_info[:3] == (3, 15, 2), sys.version
    assert platform.system() == "Linux" and platform.machine() == "x86_64", platform.platform()
    assert os.environ.get("KERAS_BACKEND") == "torch", "Set KERAS_BACKEND=torch before importing Keras"
    import numpy as np
    import torch
    import h5py
    import keras
    import keras.ops as ops

    assert keras.backend.backend() == "torch", keras.backend.backend()
    assert md.version("keras") == "3.15.1", md.version("keras")
    assert md.version("h5py") == "3.16.0", md.version("h5py")
    assert md.version("torch") == "2.15.0", md.version("torch")
    assert md.version("numpy") == "2.5.4", md.version("numpy")

    # Exercise deterministic Keras ops on PyTorch tensors, INCLUDING torch autograd.
    torch.manual_seed(2026)
    torch.set_num_threads(1)
    keras.utils.set_random_seed(2026)
    x = torch.tensor([-2.0, 0.0, 3.0], dtype=torch.float32, requires_grad=True)
    squared = ops.square(x)
    summed = ops.sum(squared)
    assert isinstance(summed, torch.Tensor), type(summed)
    assert abs(float(summed.detach()) - 13.0) < 1e-7
    summed.backward()
    torch.testing.assert_close(x.grad, torch.tensor([-4.0, 0.0, 6.0]))

    # Fit and predict using Keras's PyTorch backend on noise-free regression.
    train_x = np.array([[-2.], [-1.], [0.], [1.], [2.]], dtype=np.float32)
    train_y = 2 * train_x + 1
    model = keras.Sequential([
        keras.Input(shape=(1,)),
        keras.layers.Dense(1, kernel_initializer="zeros", bias_initializer="zeros")
    ])
    model.compile(optimizer=keras.optimizers.SGD(learning_rate=0.05), loss="mse")
    initial = float(model.evaluate(train_x, train_y, verbose=0))
    hist = model.fit(train_x, train_y, epochs=60, batch_size=5,
                     shuffle=False, verbose=0)
    final = float(model.evaluate(train_x, train_y, verbose=0))
    assert len(hist.history["loss"]) == 60
    assert initial > 0 and final < initial * 0.05, (initial, final)
    predict = float(model.predict(np.array([[3.0]], dtype=np.float32), verbose=0)[0][0])
    assert abs(predict - 7.0) < 0.3, predict

    # Save/load Keras model (uses h5py for model weights); require same prediction.
    with tempfile.TemporaryDirectory(prefix="keras_hdf5_") as d:
        artifact = Path(d) / "regression.keras"
        model.save(artifact)
        restored = keras.models.load_model(artifact)
        pred_after = float(restored.predict(np.array([[3.0]], dtype=np.float32),
                                            verbose=0)[0][0])
        assert abs(pred_after - predict) < 1e-5, (predict, pred_after)
        # Explicit HDF5 write/read test (real h5py runtime).
        h5path = Path(d) / "test.h5"
        with h5py.File(h5path, "w") as f:
            f.create_dataset("values", data=np.array([1, 2, 3], dtype=np.int32))
        with h5py.File(h5path, "r") as f:
            assert f["values"][:].tolist() == [1, 2, 3]

    wheel_lines = (EVIDENCE / "h5py_wheel_sha256.txt").read_text(encoding="utf-8").strip().splitlines()
    assert len(wheel_lines) == 1, wheel_lines
    wheel_sha256 = wheel_lines[0].split()[0]
    assert len(wheel_sha256) == 64 and all(c in "0123456789abcdef" for c in wheel_sha256)
    return {
        "status": "KERAS_RUNTIME_PASS",
        "h5py_wheel_sha256": wheel_sha256,
        "python": sys.version, "platform": platform.platform(), "backend": keras.backend.backend(),
        "versions": {name: md.version(name) for name in ("keras", "torch", "h5py", "numpy")},
        "hdf5_lib_version": h5py.version.hdf5_version,
        "module_sha256": {
            "keras_init": digest(Path(keras.__file__)),
            "h5py_init": digest(Path(h5py.__file__)),
            "torch_init": digest(Path(torch.__file__))
        },
        "source_sha256": digest(Path(__file__)),
        "gradient_expected": [-4.0, 0.0, 6.0],
        "gradient_observed": [round(float(v), 6) for v in x.grad.tolist()],
        "initial_mse": initial, "final_mse": final,
        "prediction_x3": predict, "prediction_after_reload": pred_after,
        "note": "CPU functional evidence only; NOT GPU, external expert review, or universal Keras correctness"
    }


def main():
    try:
        record = run()
    except Exception as exc:
        record = {"status": "KERAS_RUNTIME_FAIL", "error_type": type(exc).__name__,
                  "error": str(exc), "traceback": traceback.format_exc(),
                  "python": sys.version, "platform": platform.platform(),
                  "source_sha256": digest(Path(__file__))}
    RESULT.write_text(json.dumps(record, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps({k: record.get(k) for k in ("status", "versions", "backend",
                         "initial_mse", "final_mse", "prediction_x3", "error")}, ensure_ascii=False))
    return 0 if record["status"] == "KERAS_RUNTIME_PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
