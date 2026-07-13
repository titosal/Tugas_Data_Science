"""
MODUL 3: REGRESSION ANALYSIS (ANALISIS REGRESI)
Memodelkan tren temporal dan pola musiman rating.
Bahasa: Indonesia
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
import os

def run_regression_analysis(df_clean, output_dir):
    print("\n" + "="*80)
    print("MODUL 3: REGRESSION ANALYSIS (ANALISIS REGRESI)")
    print("="*80 + "\n")
    
    # 1. Regresi Tren Umur Komentar (Waktu) terhadap Rating
    print("[1/3] Melakukan estimasi parameter regresi linear...")
    X_time = df_clean[['Umur Komentar (Hari)']].values
    y_rating = df_clean['Rating'].values
    
    lr = LinearRegression()
    lr.fit(X_time, y_rating)
    
    slope = lr.coef_[0]
    intercept = lr.intercept_
    r_sq = lr.score(X_time, y_rating)
    
    print(f"  Model Linier: Rating = {intercept:.4f} + ({slope:.6f} * Umur_Komentar)")
    print(f"  Koefisien Determinasi (R^2): {r_sq:.6f}")
    
    # 2. Analisis Musiman Harian (Seasonality)
    print("\n[2/3] Menganalisis perbedaan rata-rata rating harian...")
    day_order = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu']
    day_stats = df_clean.groupby('Hari_Indo')['Rating'].agg(['mean', 'count']).reindex(day_order)
    
    print("\nStatistik Rating Harian:")
    print(day_stats.round(4))
    
    # Simpan hasil analisis regresi dan harian
    day_stats.to_csv(os.path.join(output_dir, 'statistik_rating_harian.csv'))
    
    regression_summary = pd.DataFrame({
        'Parameter': ['Intercept', 'Slope (Umur Komentar)', 'R_Squared'],
        'Value': [intercept, slope, r_sq]
    })
    regression_summary.to_csv(os.path.join(output_dir, 'summary_regresi.csv'), index=False)
    
    # 3. Membuat Visualisasi Tren Temporal dan Harian
    print("\n[3/3] Menghasilkan plot tren dan pola harian...")
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))
    
    # Plot Rata-rata Rating Harian
    sns.barplot(x=day_stats.index, y=day_stats['mean'], ax=axes[0], palette='viridis')
    axes[0].set_title('Rata-rata Rating berdasarkan Hari', fontsize=12, fontweight='bold')
    axes[0].set_xlabel('Hari')
    axes[0].set_ylabel('Rating Rata-rata')
    axes[0].set_ylim(3.8, 4.6)
    for i, val in enumerate(day_stats['mean']):
        axes[0].text(i, val + 0.01, f"{val:.3f}", ha='center', fontweight='bold')
        
    # Plot Garis Regresi Linier
    sample_df = df_clean.sample(min(1000, len(df_clean)), random_state=42)
    axes[1].scatter(sample_df['Umur Komentar (Hari)'], sample_df['Rating'], alpha=0.3, color='blue', label='Data Sampel')
    x_vals = np.linspace(X_time.min(), X_time.max(), 100).reshape(-1, 1)
    y_vals = lr.predict(x_vals)
    axes[1].plot(x_vals, y_vals, color='red', linewidth=3, label='Garis Regresi')
    axes[1].set_title('Regresi Rating vs Umur Ulasan (Hari)', fontsize=12, fontweight='bold')
    axes[1].set_xlabel('Umur Ulasan (Hari)')
    axes[1].set_ylabel('Rating')
    axes[1].legend()
    
    plt.tight_layout()
    viz_path = os.path.join(output_dir, 'analisis_regresi_tren.png')
    plt.savefig(viz_path, dpi=300)
    plt.close()
    
    print(f"Grafik regresi dan musiman disimpan di: {viz_path}")
    print("\n" + "="*80)
    print("ANALISIS REGRESI SELESAI")
    print("="*80 + "\n")
    return lr, day_stats

if __name__ == '__main__':
    # Test run
    df_test = pd.read_csv('D:\\Gacoan\\Tugas_Data_Science\\outputs\\cleaned_dataset.csv')
    run_regression_analysis(df_test, 'D:\\Gacoan\\Tugas_Data_Science\\outputs')
