"""
SCRIPT RUNNER UTAMA: PIPELINE DATA SCIENCE INTEGRATED
Menjalankan seluruh modul proyek dari manajemen data hingga simulasi big data.
Bahasa: Indonesia
"""

import os
import pandas as pd
from data_management import run_data_management
from association_correlation import run_association_correlation
from regression_analysis import run_regression_analysis
from classification import run_classification
from clustering import run_clustering
from big_data_simulation import simulate_big_data_streaming

# Setup direktori
PROJECT_DIR = "D:\\Gacoan\\Tugas_Data_Science"
DATA_PATH = os.path.join(PROJECT_DIR, "dataset", "master_dataset_merged.csv")
OUTPUT_DIR = os.path.join(PROJECT_DIR, "outputs")
os.makedirs(OUTPUT_DIR, exist_ok=True)

print("="*80)
print("MEMULAI RUNNER PIPELINE INTEGRATED DATA SCIENCE")
print("STUDI KASUS E-BUSINESS: OPTIMASI OPERASIONAL MIE GACOAN")
print("="*80)

# 1. Modul 1: Manajemen Data
df_clean = run_data_management(DATA_PATH, OUTPUT_DIR)

# 2. Modul 2: Asosiasi & Korelasi
run_association_correlation(df_clean, OUTPUT_DIR)

# 3. Modul 3: Analisis Regresi
run_regression_analysis(df_clean, OUTPUT_DIR)

# 4. Modul 4: Klasifikasi
run_classification(df_clean, OUTPUT_DIR)

# 5. Modul 5: Clustering
run_clustering(df_clean, OUTPUT_DIR)

# 6. Modul 6: Simulasi Big Data Streaming
simulate_big_data_streaming(df_clean, OUTPUT_DIR, max_records=30)

print("="*80)
print("PIPELINE DATA SCIENCE BERHASIL DIJALANKAN 100%")
print(f"Semua log dan visualisasi tersimpan di direktori: {OUTPUT_DIR}")
print("="*80)
