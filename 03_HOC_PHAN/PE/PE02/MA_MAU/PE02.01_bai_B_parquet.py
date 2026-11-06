"""PE02.01 B: real PyArrow Parquet nullable/dtype/timezone roundtrip."""
from __future__ import annotations
from datetime import datetime, timedelta, timezone
from pathlib import Path
from tempfile import TemporaryDirectory
import pyarrow as pa
import pyarrow.parquet as pq

SCHEMA=pa.schema([
    pa.field("sensor_id",pa.string(),nullable=False),
    pa.field("timestamp",pa.timestamp("us",tz="UTC"),nullable=False),
    pa.field("value",pa.float64(),nullable=True),
])

def create_table(n:int=10000)->pa.Table:
    if type(n) is not int or n<1:raise ValueError("n must be positive int")
    base=datetime(2026,11,6,tzinfo=timezone.utc)
    rows={
      "sensor_id":["dev-001"]*n,
      "timestamp":[base+timedelta(seconds=i) for i in range(n)],
      "value":[None if i%13==0 else float(i%17) for i in range(n)],
    }
    return pa.Table.from_pydict(rows,schema=SCHEMA)

def roundtrip(table:pa.Table,folder:Path)->dict:
    if not isinstance(table,pa.Table) or not table.schema.equals(SCHEMA):
        raise ValueError("Wrong schema")
    outputs={}
    for codec in ("snappy","NONE"):
        path=folder/("readings_"+codec+".parquet")
        pq.write_table(table,path,compression=codec)
        actual=pq.read_table(path)
        assert actual.schema.equals(SCHEMA), (codec,actual.schema)
        assert actual.equals(table), codec
        assert actual["value"].null_count==table["value"].null_count
        outputs[codec]=path.stat().st_size
    return outputs

def demo():
    table=create_table()
    assert len(table)==10000
    assert table["value"].null_count>0
    assert SCHEMA.field("sensor_id").nullable is False
    assert SCHEMA.field("value").nullable is True
    assert SCHEMA.field("timestamp").type == pa.timestamp("us",tz="UTC")
    with TemporaryDirectory() as d:
        sizes=roundtrip(table,Path(d))
    return {"rows":len(table),"null_count":table["value"].null_count,
            "snappy_size":sizes["snappy"],"uncompressed_size":sizes["NONE"]}

if __name__=="__main__":
    print("PE02.01_PARQUET_SCHEMA_PASS",demo())
