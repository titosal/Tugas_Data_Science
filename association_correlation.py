"""
MODUL 2: ASSOCIATION & CORRELATION DATA (ASOSIASI & KORELASI DATA)
Menganalisis hubungan antar fitur dan asosiasi teks ulasan.
Bahasa: Indonesia
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import re
from collections import Counter

def run_association_correlation(df_clean, output_dir):
    print("\n" + "="*80)
    print("MODUL 2: ASSOCIATION & CORRELATION DATA")
    print("="*80 + "\n")
    
    # 1. Pearson & Spearman Correlation
    print("[1/3] Menghitung korelasi statistik...")
    cols_to_corr = ['Rating', 'panjang_review', 'jumlah_kata', 'ada_tanda_seru', 'ada_tanda_tanya']
    pearson_matrix = df_clean[cols_to_corr].corr(method='pearson')
    spearman_matrix = df_clean[cols_to_corr].corr(method='spearman')
    
    # Simpan hasil korelasi
    pearson_matrix.to_csv(os.path.join(output_dir, 'korelasi_pearson.csv'))
    spearman_matrix.to_csv(os.path.join(output_dir, 'korelasi_spearman.csv'))
    
    print("  Korelasi Pearson (Rating vs Fitur):")
    print(pearson_matrix['Rating'].round(4))
    
    # 2. Analisis Asosiasi Kata (Co-occurrence)
    print("\n[2/3] Melakukan analisis asosiasi teks ulasan...")
    keywords = ['enak', 'parkir', 'pelayanan', 'ramah', 'cepat', 'mahal', 'level', 'meja', 'lama', 'bersih']
    keyword_correlations = []
    
    for kw in keywords:
        has_kw = df_clean['Review'].str.contains(kw, case=False, na=False).astype(int)
        corr_val = df_clean['Rating'].corr(has_kw)
        keyword_correlations.append({
            'Keyword': kw,
            'Correlation': corr_val,
            'Count': has_kw.sum()
        })
        
    kw_df = pd.DataFrame(keyword_correlations).sort_values('Correlation', ascending=False)
    kw_df.to_csv(os.path.join(output_dir, 'korelasi_keyword.csv'), index=False)
    
    print("\nAsosiasi Keyword dengan Rating:")
    print(kw_df.to_string(index=False))
    
    # 3. Membuat Visualisasi Heatmap Korelasi
    print("\n[3/3] Menghasilkan visualisasi korelasi...")
    plt.figure(figsize=(10, 8))
    sns.heatmap(pearson_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1, fmt=".4f")
    plt.title('Matriks Korelasi Pearson (Fitur & Rating)', fontsize=14, fontweight='bold')
    plt.tight_layout()
    viz_path = os.path.join(output_dir, 'heatmap_korelasi.png')
    plt.savefig(viz_path, dpi=300)
    plt.close()
    
    print(f"Heatmap korelasi disimpan di: {viz_path}")
    print("\n" + "="*80)
    print("ASOSIASI & KORELASI DATA SELESAI")
    print("="*80 + "\n")
    return pearson_matrix, kw_df

if __name__ == '__main__':
    # Test run
    df_test = pd.read_csv('D:\\Gacoan\\Tugas_Data_Science\\outputs\\cleaned_dataset.csv')
    run_association_correlation(df_test, 'D:\\Gacoan\\Tugas_Data_Science\\outputs')
