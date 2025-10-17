from perfetto.trace_processor import TraceProcessor
import numpy as np

tp = TraceProcessor(trace="com.oculus.panelapp.library_Unknown Device_2025-10-13_13-37-24.pftrace")
tables = tp.query("""
    SELECT name FROM sqlite_master
    WHERE type='table'
    ORDER BY name
""").as_pandas_dataframe()
print(tables.head(10))

tracks = tp.query("""
    SELECT id, name, type
    FROM track
    ORDER BY name
""").as_pandas_dataframe()
print(tracks.head(10))

counters_df = tp.query("""
  SELECT c.ts, c.value, ct.name AS counter_name
  FROM counter c
  JOIN counter_track ct ON c.track_id = ct.id
  ORDER BY c.ts
""").as_pandas_dataframe()

# clean up and add a relative time column
counters_df = counters_df.replace(np.nan, 0)
counters_df["t_s"] = (counters_df["ts"] - counters_df["ts"].min()) / 1e9  # ns → seconds

# create CSV
counters_df.to_csv("kitchen_5.csv", index=False)