"""
MODUL 1: DATA MANAGEMENT (MANAJEMEN DATA)
Mengelola pembersihan data, standardisasi, dan rekayasa fitur.
Bahasa: Indonesia
"""

import pandas as pd
import numpy as np
import os

def run_data_management(data_path, output_dir):
    print("\n" + "="*80)
    print("MODUL 1: DATA MANAGEMENT (MANAJEMEN DATA)")
    print("="*80 + "\n")
    
    # Load dataset
    df = pd.read_csv(data_path)
    
    # Data Cleaning & Imputation
    print("[1/3] Melakukan pembersihan data...")
    df_clean = df.dropna(subset=['Rating', 'Review', 'Lokasi'])
    
    # Standardisasi tipe data
    df_clean['Rating'] = pd.to_numeric(df_clean['Rating'], errors='coerce')
    df_clean = df_clean.dropna(subset=['Rating'])
    df_clean['Rating'] = df_clean['Rating'].astype(int)
    
    # Rekayasa Fitur (Feature Engineering)
    print("[2/3] Melakukan rekayasa fitur tekstual...")
    df_clean['panjang_review'] = df_clean['Review'].str.len()
    df_clean['jumlah_kata'] = df_clean['Review'].str.split().str.len()
    df_clean['ada_tanda_seru'] = df_clean['Review'].str.contains(r'!', regex=True).astype(int)
    df_clean['ada_tanda_tanya'] = df_clean['Review'].str.contains(r'\?', regex=True).astype(int)
    
    # Standardisasi Waktu & Tanggal
    today = pd.to_datetime('2026-06-30')
    df_clean['Tanggal'] = today - pd.to_timedelta(df_clean['Umur Komentar (Hari)'], unit='D')
    df_clean['Hari'] = df_clean['Tanggal'].dt.day_name()
    df_clean['Bulan'] = df_clean['Tanggal'].dt.to_period('M')
    
    # Konversi Hari ke Bahasa Indonesia
    day_map = {
        'Monday': 'Senin', 'Tuesday': 'Selasa', 'Wednesday': 'Rabu',
        'Thursday': 'Kamis', 'Friday': 'Jumat', 'Saturday': 'Sabtu', 'Sunday': 'Minggu'
    }
    df_clean['Hari_Indo'] = df_clean['Hari'].map(day_map)
    
    # Simpan dataset yang telah dibersihkan
    cleaned_path = os.path.join(output_dir, 'cleaned_dataset.csv')
    df_clean.to_csv(cleaned_path, index=False)
    print(f"[3/3] Dataset berhasil dibersihkan dan disimpan di: {cleaned_path}")
    
    print(f"\nRingkasan Manajemen Data:")
    print(f"  - Baris Awal: {len(df):,}")
    print(f"  - Baris Bersih: {len(df_clean):,}")
    print(f"  - Cabang Teranalisis: {df_clean['Lokasi'].nunique()} lokasi")
    print(f"  - Fitur Baru Ditambahkan: panjang_review, jumlah_kata, ada_tanda_seru, ada_tanda_tanya, Tanggal, Hari_Indo, Bulan")
    
    print("\n" + "="*80)
    print("MANAJEMEN DATA SELESAI")
    print("="*80 + "\n")
    return df_clean

if __name__ == '__main__':
    # Test run
    os.makedirs('D:\\Gacoan\\Tugas_Data_Science\\outputs', exist_ok=True)
    run_data_management('D:\\Gacoan\\Tugas_Data_Science\\dataset\\master_dataset_merged.csv', 'D:\\Gacoan\\Tugas_Data_Science\\outputs')
