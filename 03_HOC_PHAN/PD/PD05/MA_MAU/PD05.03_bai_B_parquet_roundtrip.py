"""PD05.03 B: real nullable int and timezone-aware Parquet roundtrip."""
from datetime import datetime, timezone
from pathlib import Path
from tempfile import TemporaryDirectory
import pyarrow as pa
import pyarrow.parquet as pq

SCHEMA = pa.schema([
    pa.field("qty", pa.int64(), nullable=True),
    pa.field("ts", pa.timestamp("us", tz="UTC"), nullable=False),
])

def make_table(qty, timestamps):
    if len(qty) != len(timestamps) or not timestamps:
        raise ValueError("nonempty equal-length columns are required")
    if any(t.tzinfo is None or t.utcoffset() is None for t in timestamps):
        raise ValueError("timestamps must have a timezone")
    times = [t.astimezone(timezone.utc) for t in timestamps]
    return pa.Table.from_arrays(
        [pa.array(qty, type=pa.int64()),
         pa.array(times, type=pa.timestamp("us", tz="UTC"))],
        schema=SCHEMA,
    )

def roundtrip(table, output_path):
    output_path = Path(output_path)
    pq.write_table(table, output_path, compression="snappy")
    restored = pq.read_table(output_path)
    if not restored.schema.equals(SCHEMA):
        raise AssertionError("schema changed after roundtrip")
    if not restored.equals(table):
        raise AssertionError("data or null bitmap changed")
    return restored

if __name__ == "__main__":
    original = make_table(
        [None, 0, 12],
        [datetime(2026, 1, day, tzinfo=timezone.utc) for day in (1, 2, 3)],
    )
    assert original["qty"].null_count == 1
    with TemporaryDirectory() as temp:
        result = roundtrip(original, Path(temp) / "table.parquet")
        assert result.schema.equals(SCHEMA)
        assert result["ts"].type == pa.timestamp("us", tz="UTC")
        assert result["qty"].null_count == 1
    print("PASS PD05.03")
