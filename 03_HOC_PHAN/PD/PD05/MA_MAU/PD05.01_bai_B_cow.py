"""PD05.01 B: contrast pandas 3.x Copy-on-Write and .loc edits."""
import json
import warnings
import pandas as pd

def compare_edits():
    if int(pd.__version__.split(".")[0]) < 3:
        raise RuntimeError("B exercise requires pandas 3.x")
    original = pd.DataFrame({"x": [1, 2, 3]})
    view = original[["x"]]
    view.loc[0, "x"] = 99
    assert original["x"].tolist() == [1, 2, 3]
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        original[original["x"] > 0]["x"] = 100
    assert original["x"].tolist() == [1, 2, 3]
    original.loc[original["x"] > 0, "x"] = 42
    assert original["x"].tolist() == [42, 42, 42]
    return {"pandas_version":pd.__version__, "copy_value":int(view.loc[0,"x"]),
            "original_after_chained": [1, 2, 3],
            "original_after_loc":original["x"].tolist(),
            "warnings": [type(w.message).__name__ for w in caught]}

if __name__ == "__main__":
    print(json.dumps(compare_edits(),ensure_ascii=False))
    print("PASS PD05.01")
