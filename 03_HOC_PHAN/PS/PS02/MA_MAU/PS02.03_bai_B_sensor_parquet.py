"""PS02.03 B: validated UTC sensor schema, units and Parquet roundtrip."""
from __future__ import annotations
from datetime import datetime, timezone
from pathlib import Path
from tempfile import TemporaryDirectory
import hashlib
import pyarrow as pa
import pyarrow.parquet as pq

SCHEMA=pa.schema([
    pa.field("device_id",pa.string(),nullable=False),
    pa.field("timestamp",pa.timestamp("us",tz="UTC"),nullable=False),
    pa.field("value",pa.float64(),nullable=True),
    pa.field("unit",pa.string(),nullable=False),
    pa.field("quality_flag",pa.dictionary(pa.int8(),pa.string()),nullable=False),
])

def validate_rows(rows:list[dict])->list[dict]:
    if not isinstance(rows,list) or not rows:
        raise ValueError("Rows must be nonempty list")
    normalized=[]
    units=set()
    previous={}
    for row in rows:
        if not isinstance(row,dict):
            raise TypeError("Each record must be dict")
        if set(row)!={"device_id","timestamp","value","unit","quality_flag"}:
            raise ValueError("Missing/unexpected column")
        d,t,v,u,q=(row[k] for k in ("device_id","timestamp","value","unit","quality_flag"))
        if type(d) is not str or not d:
            raise ValueError("Invalid device ID")
        if not isinstance(t,datetime) or t.tzinfo is None or t.utcoffset() is None:
            raise ValueError("Timestamp must be timezone aware")
        instant=t.astimezone(timezone.utc)
        if d in previous and instant<=previous[d]:
            raise ValueError("Duplicate or nonmonotonic per-device timestamp")
        previous[d]=instant
        if u not in ("C","F"):
            raise ValueError("Unsupported unit")
        units.add(u)
        if q not in ("ok","missing"):
            raise ValueError("Invalid quality flag")
        if v is None:
            if q!="missing":raise ValueError("Null reading must have missing flag")
        elif type(v) not in (int,float) or q!="ok":
            raise ValueError("Measurement/quality mismatch")
        normalized.append({"device_id":d,"timestamp":instant,"value":v,
                           "unit":u,"quality_flag":q})
    if len(units)!=1:
        raise ValueError("Mixed units must be converted upstream")
    return normalized

def write_and_check(rows:list[dict],dest:Path)->dict:
    normalized=validate_rows(rows)
    table=pa.Table.from_pylist(normalized,schema=SCHEMA)
    pq.write_table(table,dest,compression="snappy")
    loaded=pq.read_table(dest)
    assert loaded.schema.equals(SCHEMA), loaded.schema
    assert loaded.equals(table), "Parquet content changed on roundtrip"
    assert loaded["value"].null_count==sum(r["value"] is None for r in normalized)
    return {"count":len(rows),"nulls":loaded["value"].null_count,
            "sha256":hashlib.sha256(dest.read_bytes()).hexdigest(),
            "timezone":str(loaded.schema.field("timestamp").type)}

def example_rows():
    # Two distinct instants despite repeating 01:30 local time when DST ends.
    return [
      {"device_id":"sensor-1","timestamp":datetime.fromisoformat("2026-11-01T01:30:00-04:00"),
       "value":20.0,"unit":"C","quality_flag":"ok"},
      {"device_id":"sensor-1","timestamp":datetime.fromisoformat("2026-11-01T01:30:00-05:00"),
       "value":None,"unit":"C","quality_flag":"missing"},
    ]

def demo():
    with TemporaryDirectory() as d:
        result=write_and_check(example_rows(),Path(d)/"sensor.parquet")
    assert result["nulls"]==1
    assert result["timezone"]=="timestamp[us, tz=UTC]"
    return result

if __name__=="__main__":
    print("PS02.03_SENSOR_PARQUET_PASS",demo())
