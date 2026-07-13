"""
MODUL 4: CLASSIFICATION (KLASIFIKASI DATA)
Membangun model Random Forest Classifier untuk prediksi ulasan baik vs buruk.
Bahasa: Indonesia
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score, roc_curve
import os
import pickle

def run_classification(df_clean, output_dir):
    print("\n" + "="*80)
    print("MODUL 4: CLASSIFICATION (KLASIFIKASI DATA)")
    print("="*80 + "\n")
    
    # 1. Encoding & Split Data
    print("[1/3] Mempersiapkan data ulasan untuk klasifikasi...")
    le_lokasi = LabelEncoder()
    df_clean['lokasi_encoded'] = le_lokasi.fit_transform(df_clean['Lokasi'])
    
    # Target: 1 = Ulasan Baik (Rating >= 4), 0 = Ulasan Buruk (Rating <= 3)
    df_clean['target'] = (df_clean['Rating'] >= 4).astype(int)
    
    feature_cols = ['panjang_review', 'jumlah_kata', 'ada_tanda_seru', 'ada_tanda_tanya', 'lokasi_encoded']
    X = df_clean[feature_cols].values
    y = df_clean['target'].values
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    
    # 2. Training Random Forest
    print("[2/3] Melatih model Random Forest Classifier...")
    rf = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
    rf.fit(X_train, y_train)
    
    # Evaluasi Model
    y_pred = rf.predict(X_test)
    y_prob = rf.predict_proba(X_test)[:, 1]
    
    acc_train = rf.score(X_train, y_train)
    acc_test = rf.score(X_test, y_test)
    roc_auc = roc_auc_score(y_test, y_prob)
    
    print(f"  Akurasi Training: {acc_train:.4%}")
    print(f"  Akurasi Testing: {acc_test:.4%}")
    print(f"  ROC-AUC Score: {roc_auc:.4%}")
    
    print("\nLaporan Klasifikasi Detail:")
    print(classification_report(y_test, y_pred, target_names=['Bad (1-3)', 'Good (4-5)']))
    
    # Simpan hasil metrik klasifikasi
    metrics_summary = pd.DataFrame({
        'Metric': ['Training Accuracy', 'Testing Accuracy', 'ROC-AUC Score'],
        'Value': [acc_train, acc_test, roc_auc]
    })
    metrics_summary.to_csv(os.path.join(output_dir, 'summary_klasifikasi.csv'), index=False)
    
    # Simpan model dan encoder
    with open(os.path.join(output_dir, 'random_forest_model.pkl'), 'wb') as f:
        pickle.dump(rf, f)
    with open(os.path.join(output_dir, 'label_encoder_lokasi.pkl'), 'wb') as f:
        pickle.dump(le_lokasi, f)
        
    # 3. Membuat Visualisasi Confusion Matrix & ROC Curve
    print("\n[3/3] Menghasilkan plot evaluasi model...")
    cm = confusion_matrix(y_test, y_pred)
    
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))
    
    # Confusion Matrix
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=axes[0],
                xticklabels=['Bad', 'Good'], yticklabels=['Bad', 'Good'])
    axes[0].set_title('Confusion Matrix Klasifikasi', fontsize=12, fontweight='bold')
    axes[0].set_xlabel('Prediksi')
    axes[0].set_ylabel('Sebenarnya')
    
    # ROC Curve
    fpr, tpr, _ = roc_curve(y_test, y_prob)
    axes[1].plot(fpr, tpr, color='darkorange', lw=3, label=f'ROC Curve (AUC = {roc_auc:.4f})')
    axes[1].plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
    axes[1].set_xlabel('False Positive Rate')
    axes[1].set_ylabel('True Positive Rate')
    axes[1].set_title('Receiver Operating Characteristic (ROC)', fontsize=12, fontweight='bold')
    axes[1].legend(loc="lower right")
    
    plt.tight_layout()
    viz_path = os.path.join(output_dir, 'klasifikasi_model_evaluasi.png')
    plt.savefig(viz_path, dpi=300)
    plt.close()
    
    print(f"Grafik evaluasi klasifikasi disimpan di: {viz_path}")
    print("\n" + "="*80)
    print("KLASIFIKASI DATA SELESAI")
    print("="*80 + "\n")
    return rf, metrics_summary

if __name__ == '__main__':
    # Test run
    df_test = pd.read_csv('D:\\Gacoan\\Tugas_Data_Science\\outputs\\cleaned_dataset.csv')
    run_classification(df_test, 'D:\\Gacoan\\Tugas_Data_Science\\outputs')
