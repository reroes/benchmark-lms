import polars as pl
import time
import psutil
import os

DATA = "/data/lms_academico_500mb.csv"

def mem_mb():
    return psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024

start_mem = mem_mb()
start = time.perf_counter()

resultado = (
    pl.scan_csv(DATA)
    .filter(pl.col("nota").is_not_null())
    .group_by("curso")
    .agg([
        pl.col("nota").mean().alias("promedio_nota"),
        pl.col("nota").count().alias("total_registros")
    ])
    .collect()
)

end = time.perf_counter()
end_mem = mem_mb()

print("\n[ENFOQUE MODERNO - GROUPBY]")
print(resultado)

print(f"\nFilas: {resultado.height}")
print(f"Tiempo: {end - start:.2f} s")
print(f"Memoria usada: {end_mem - start_mem:.2f} MB")
