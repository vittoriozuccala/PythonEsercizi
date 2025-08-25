# Dal video: https://www.youtube.com/watch?v=M-Hcf-YdBAA
# Velocizza l'accesso ai dati
# soprattutto nell'accesso a singole colonne

import sys
import time
import pandas as pd
import pyarrow as pw

# Base dati da: https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page
# Scarico: yellow_tripdata_2025-01.parquet

start = time.perf_counter()
df_parquet = pd.read_parquet('yellow_tripdata_2025-01.parquet')
end = time.perf_counter()

print(df_parquet)

print(f"Ho letto il file in {end-start}")

print(f"Il file, in memoria tiene {sys.getsizeof(df_parquet)/1000000}Mb")

# Pià colonne hai più l'utilizzo di parquet è funzionale
print(df_parquet.columns)

selected_columns = ['VendorID', 'payment_type', 'tip_amount']
start = time.perf_counter()
df_parquet = pd.read_parquet('yellow_tripdata_2025-01.parquet', columns=selected_columns)
end = time.perf_counter()
print(f"Ho letto il file in {end-start}")