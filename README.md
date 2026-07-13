# PROYEK DATA SCIENCE: OPTIMASI E-BUSINESS MIE GACOAN DENGAN DATA SCIENCE & BIG DATA

Proyek ini dibuat sebagai pemenuhan Tugas Besar Data Science, yang menerapkan seluruh pipeline analisis data science dan simulasi big data pada studi kasus e-business reputasi digital Mie Gacoan.

## Struktur Direktori Proyek

```
D:\Gacoan\Tugas_Data_Science\
├── dataset/
│   └── master_dataset_merged.csv      # Dataset ulasan asli (22,551 ulasan)
│
├── outputs/                           # Folder penyimpanan log, hasil, & visualisasi
│   ├── cleaned_dataset.csv            # Dataset hasil pembersihan (Modul 1)
│   ├── korelasi_pearson.csv           # Matriks korelasi (Modul 2)
│   ├── korelasi_keyword.csv           # Asosiasi keyword (Modul 2)
│   ├── heatmap_korelasi.png           # Visualisasi heatmap (Modul 2)
│   ├── statistik_rating_harian.csv    # Analisis harian (Modul 3)
│   ├── summary_regresi.csv            # Ringkasan regresi (Modul 3)
│   ├── analisis_regresi_tren.png      # Visualisasi tren (Modul 3)
│   ├── summary_klasifikasi.csv        # Evaluasi akurasi model (Modul 4)
│   ├── random_forest_model.pkl        # Model klasifikasi tersimpan (Modul 4)
│   ├── klasifikasi_model_evaluasi.png # Plot confusion matrix & ROC (Modul 4)
│   ├── hasil_clustering_cabang.csv    # Pengelompokan cabang (Modul 5)
│   ├── cluster_cabang_scatter.png     # Scatter plot cluster (Modul 5)
│   └── simulasi_stream_log.json       # Log simulasi Kafka/Spark (Modul 6)
│
├── Makalah_Data_Science.md            # Makalah Akademik lengkap (Soal No 1)
│
├── data_management.py                 # Kode Modul 1
├── association_correlation.py         # Kode Modul 2
├── regression_analysis.py             # Kode Modul 3
├── classification.py                  # Kode Modul 4
├── clustering.py                      # Kode Modul 5
├── big_data_simulation.py             # Kode Modul 6
└── run_project.py                     # Script Runner Utama Pipeline
```

## Cara Menjalankan Pipeline Proyek

1. Pastikan library Python yang dibutuhkan sudah terpasang:
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn
   ```

2. Jalankan script runner utama:
   ```bash
   python run_project.py
   ```

3. Seluruh log pemrosesan akan ditampilkan secara interaktif pada terminal, dan hasil visualisasi plot serta CSV akan ter-generate di folder `outputs/`.
