import pandas as pd
import time
import psutil
import os

DATA = "/data/lms_academico_500mb.csv"

def mem_mb():
    return psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024

start_mem = mem_mb()
start = time.perf_counter()

df = pd.read_csv(DATA)

resultado = (
    df[df["nota"].notna()]
    .groupby("curso")
    .agg(
        promedio_nota=("nota", "mean"),
        total_registros=("nota", "count")
    )
    .reset_index()
)

end = time.perf_counter()
end_mem = mem_mb()

print("\n[ENFOQUE TRADICIONAL - GROUPBY]")
print(resultado)

print(f"\nFilas: {len(resultado)}")
print(f"Tiempo: {end - start:.2f} s")
print(f"Memoria usada: {end_mem - start_mem:.2f} MB")
