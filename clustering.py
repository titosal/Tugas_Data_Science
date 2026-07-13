"""
MODUL 5: CLUSTERING (CLUSTERING DATA)
Mengelompokkan lokasi cabang Mie Gacoan menggunakan K-Means berdasarkan metrik performa.
Bahasa: Indonesia
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import os
import pickle

def run_clustering(df_clean, output_dir):
    print("\n" + "="*80)
    print("MODUL 5: CLUSTERING (CLUSTERING DATA)")
    print("="*80 + "\n")
    
    # 1. Agregasi Fitur Per Cabang
    print("[1/3] Melakukan agregasi metrik kinerja per cabang lokasi...")
    loc_stats = df_clean.groupby('Lokasi').agg({
        'Rating': ['mean', 'std', 'count'],
        'Umur Komentar (Hari)': 'mean'
    })
    loc_stats.columns = ['Rata_Rata_Rating', 'Std_Dev_Rating', 'Total_Review', 'Rata_Rata_Umur_Ulasan']
    loc_stats = loc_stats.fillna(0)
    
    # 2. Standardisasi & K-Means Clustering (K=3)
    print("[2/3] Mengelompokkan cabang dengan K-Means...")
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(loc_stats)
    
    kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
    loc_stats['Cluster'] = kmeans.fit_predict(X_scaled)
    
    # Profiling clusters
    cluster_profiles = loc_stats.groupby('Cluster').mean().round(4)
    print("\nProfil Rata-rata Fitur per Cluster:")
    print(cluster_profiles)
    
    # Labeling cluster berdasarkan rata-rata rating
    cluster_order = cluster_profiles['Rata_Rata_Rating'].sort_values(ascending=False).index.tolist()
    cluster_names = {
        cluster_order[0]: 'Excellent (Performa Tinggi)',
        cluster_order[1]: 'Average (Performa Stabil)',
        cluster_order[2]: 'Underperformer (Perlu Evaluasi)'
    }
    loc_stats['Nama_Cluster'] = loc_stats['Cluster'].map(cluster_names)
    
    print("\nPengelompokan Lokasi Cabang:")
    for cluster_id in cluster_order:
        name = cluster_names[cluster_id]
        branches = loc_stats[loc_stats['Cluster'] == cluster_id].index.tolist()
        print(f"  - {name}: {', '.join(branches)}")
        
    # Simpan hasil clustering
    loc_stats.to_csv(os.path.join(output_dir, 'hasil_clustering_cabang.csv'))
    cluster_profiles.to_csv(os.path.join(output_dir, 'profil_cluster.csv'))
    
    with open(os.path.join(output_dir, 'kmeans_model.pkl'), 'wb') as f:
        pickle.dump(kmeans, f)
    with open(os.path.join(output_dir, 'cluster_scaler.pkl'), 'wb') as f:
        pickle.dump(scaler, f)
        
    # 3. Membuat Visualisasi Cluster Scatter
    print("\n[3/3] Menghasilkan plot visualisasi clustering...")
    plt.figure(figsize=(10, 8))
    
    colors_map = {
        'Excellent (Performa Tinggi)': '#2ecc71',
        'Average (Performa Stabil)': '#3498db',
        'Underperformer (Perlu Evaluasi)': '#e74c3c'
    }
    
    for name, group in loc_stats.groupby('Nama_Cluster'):
        plt.scatter(group['Total_Review'], group['Rata_Rata_Rating'],
                    s=200, label=name, color=colors_map[name], alpha=0.8, edgecolors='black')
        
    plt.xlabel('Total Volume Review (Ulasan)', fontsize=12)
    plt.ylabel('Rata-rata Rating (Bintang)', fontsize=12)
    plt.title('Pengelompokan Lokasi Cabang Mie Gacoan (K-Means)', fontsize=14, fontweight='bold')
    plt.legend(fontsize=11, loc='lower left')
    plt.grid(True, linestyle='--', alpha=0.5)
    
    plt.tight_layout()
    viz_path = os.path.join(output_dir, 'cluster_cabang_scatter.png')
    plt.savefig(viz_path, dpi=300)
    plt.close()
    
    print(f"Grafik scatter clustering disimpan di: {viz_path}")
    print("\n" + "="*80)
    print("CLUSTERING DATA SELESAI")
    print("="*80 + "\n")
    return loc_stats, cluster_profiles

if __name__ == '__main__':
    # Test run
    df_test = pd.read_csv('D:\\Gacoan\\Tugas_Data_Science\\outputs\\cleaned_dataset.csv')
    run_clustering(df_test, 'D:\\Gacoan\\Tugas_Data_Science\\outputs')
