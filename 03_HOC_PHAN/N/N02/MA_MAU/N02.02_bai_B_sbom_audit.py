"""N02.02: source-bound synthetic CycloneDX-style dependency-graph exercise.

Synthetic names/versions are NOT real package advisories or verified SBOM provenance.
"""
from copy import deepcopy
import json
from pathlib import Path

DEFAULT = Path(__file__).with_name("N02.02_bai_B_synthetic_sbom.json")

def validate_graph(bom):
    if bom.get("bomFormat") != "CycloneDX" or bom.get("specVersion") != "1.6":
        raise ValueError("incorrect demonstration SBOM envelope")
    root = bom["metadata"]["component"]["bom-ref"]
    refs = [root] + [c["bom-ref"] for c in bom["components"]]
    if len(refs) != len(set(refs)):
        raise ValueError("duplicate component bom-ref")
    graph = {}
    for edge in bom["dependencies"]:
        source = edge["ref"]
        if source in graph or source not in refs:
            raise ValueError("duplicate or unknown dependency source")
        targets = edge["dependsOn"]
        if any(target not in refs or target == source for target in targets):
            raise ValueError("unknown or self dependency")
        graph[source] = list(targets)
    if root not in graph:
        raise ValueError("missing root dependencies")
    visited=set()
    def walk(node, path):
        if node in path:
            raise ValueError("cycle in training dependency graph")
        for target in graph.get(node, []):
            if target not in visited:
                visited.add(target)
                walk(target, path | {node})
    walk(root,set())
    direct=set(graph[root])
    return {"root":root,"direct":direct,
            "transitive":visited-direct,"all_reachable":visited}

def remediation(old, old_ref, new_version):
    before=validate_graph(old)
    if old_ref not in before["all_reachable"]:
        raise ValueError("affected dependency not reachable")
    changed=deepcopy(old)
    component=next(c for c in changed["components"] if c["bom-ref"]==old_ref)
    name=component["name"]
    new_ref=f"pkg:pypi/{name}@{new_version}"
    component.update(version=new_version, purl=new_ref, **{"bom-ref":new_ref})
    for edge in changed["dependencies"]:
        if edge["ref"]==old_ref:
            edge["ref"]=new_ref
        edge["dependsOn"]=[new_ref if v==old_ref else v for v in edge["dependsOn"]]
    after=validate_graph(changed)
    if old_ref in after["all_reachable"] or new_ref not in after["all_reachable"]:
        raise AssertionError("advisory remediation graph failed")
    return changed

if __name__=="__main__":
    bom=json.loads(DEFAULT.read_text(encoding="utf8"))
    graph=validate_graph(bom)
    assert len(graph["direct"])==1 and len(graph["transitive"])==1
    old_ref="pkg:pypi/example-beta@1.0.0"
    updated=remediation(bom,old_ref,"1.0.1")
    assert old_ref not in validate_graph(updated)["all_reachable"]
    print("PASS N02.02")
