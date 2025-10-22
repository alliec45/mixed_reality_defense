import sys
import numpy as np
from perfetto.trace_processor import TraceProcessor

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_trace.pftrace> <output_file.csv>")
        sys.exit(1)

    trace_file = sys.argv[1]
    output_csv = sys.argv[2]

    # Load the trace
    tp = TraceProcessor(trace=trace_file)

    # Optional: list tables
    tables = tp.query("""
        SELECT name FROM sqlite_master
        WHERE type='table'
        ORDER BY name
    """).as_pandas_dataframe()
    print("Tables:")
    print(tables.head(10))

    # Optional: list tracks
    tracks = tp.query("""
        SELECT id, name, type
        FROM track
        ORDER BY name
    """).as_pandas_dataframe()
    print("Tracks:")
    print(tracks.head(10))

    # Extract counter data
    counters_df = tp.query("""
      SELECT c.ts, c.value, ct.name AS counter_name
      FROM counter c
      JOIN counter_track ct ON c.track_id = ct.id
      ORDER BY c.ts
    """).as_pandas_dataframe()

    # Clean up and add a relative time column
    counters_df = counters_df.replace(np.nan, 0)
    counters_df["t_s"] = (counters_df["ts"] - counters_df["ts"].min()) / 1e9  # ns → s

    # Write to CSV
    counters_df.to_csv(output_csv, index=False)
    print(f"✅ CSV file saved as {output_csv}")

if __name__ == "__main__":
    main()