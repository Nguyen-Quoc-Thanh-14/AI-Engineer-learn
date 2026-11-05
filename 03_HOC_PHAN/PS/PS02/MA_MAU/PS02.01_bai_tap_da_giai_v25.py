"""PS02.01 corrected: Monte Carlo pi, repeated runs, and SVG error bars."""
from random import Random
from statistics import mean,pstdev
import math
import xml.etree.ElementTree as ET
from pathlib import Path
import tempfile

def estimate_pi(n:int, seed:int)->float:
    if type(n) is not int or n<=0:raise ValueError("n must be positive integer")
    r=Random(seed)
    return 4*sum(r.random()**2 + r.random()**2<=1.0 for _ in range(n))/n

def compare_sample_sizes(sizes=(100,1000,5000),runs=12):
    if type(runs) is not int or runs<2:raise ValueError("need at least 2 runs")
    if any(type(n) is not int or n<=0 for n in sizes):raise ValueError("positive sample sizes required")
    result=[]
    for n in sizes:
        samples=[estimate_pi(n,100+s) for s in range(runs)]
        avg=mean(samples)
        margin=1.96*pstdev(samples)/math.sqrt(runs)
        result.append({"n":n,"runs":runs,"mean_pi":avg,
                       "half_width_95pct_normal_approx":margin,"abs_error":abs(avg-math.pi)})
    return result

def render_error_bars_svg(results):
    svg=ET.Element("svg",{"xmlns":"http://www.w3.org/2000/svg",
                          "viewBox":"0 0 640 280"})
    # X axis equally spaced by category N; Y axis on range 2..4 to show uncertainty.
    for i,row in enumerate(results):
        x=100+190*i
        y=lambda v: 240-(v-2.0)*100
        mid=y(row["mean_pi"])
        margin=row["half_width_95pct_normal_approx"]*100
        ET.SubElement(svg,"line",{"x1":str(x),"y1":f"{mid-margin:.3f}",
                                  "x2":str(x),"y2":f"{mid+margin:.3f}",
                                  "stroke":"black","stroke-width":"2"})
        ET.SubElement(svg,"circle",{"cx":str(x),"cy":f"{mid:.3f}",
                                    "r":"5","fill":"black"})
        ET.SubElement(svg,"text",{"x":str(x),"y":"260","text-anchor":"middle"}).text=f"N={row['n']}"
    y_pi=240-(math.pi-2.0)*100
    ET.SubElement(svg,"line",{"x1":"40","y1":f"{y_pi:.3f}","x2":"600",
                               "y2":f"{y_pi:.3f}","stroke":"gray","stroke-dasharray":"4,4"})
    return ET.tostring(svg,encoding="unicode")

def check():
    rows=compare_sample_sizes()
    assert len(rows)==3
    assert all(r["runs"]==12 and r["half_width_95pct_normal_approx"]>0 for r in rows)
    assert 2.0<rows[-1]["mean_pi"]<4.0
    svg=render_error_bars_svg(rows)
    root=ET.fromstring(svg)
    assert root.tag.endswith("svg")
    assert len([e for e in root if e.tag=="{http://www.w3.org/2000/svg}circle"])==3
    for bad in (0,-1,True):
        try:estimate_pi(bad,1)
        except ValueError:pass
        else:raise AssertionError(repr(bad))
if __name__=="__main__":
    check()
    rows=compare_sample_sizes()
    with tempfile.TemporaryDirectory() as d:
        p=Path(d)/"pi_error_bars.svg"
        p.write_text(render_error_bars_svg(rows),encoding="utf8")
        assert p.stat().st_size>100
    print("PASS PS02.01",rows)
