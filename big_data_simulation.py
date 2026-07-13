"""
MODUL 6: BIG DATA SIMULATION (SIMULASI PRODUSEN-KONSUMEN STREAMING)
Mensimulasikan arsitektur big data streaming untuk pemrosesan review real-time.
Bahasa: Indonesia
"""

import pandas as pd
import numpy as np
import time
import json
import os
import random

def simulate_big_data_streaming(df_clean, output_dir, max_records=20):
    print("\n" + "="*80)
    print("MODUL 6: BIG DATA SIMULATION (SIMULASI STREAMING)")
    print("="*80 + "\n")
    
    # Simpan skema stream JSON untuk verifikasi arsitektur
    stream_file = os.path.join(output_dir, 'simulasi_stream_log.json')
    if os.path.exists(stream_file):
        os.remove(stream_file)
        
    print(f"[1/3] Memulai simulasi Produsen Data (Review Generator)...")
    print(f"  Produsen mensimulasikan ingestion data Google Reviews secara real-time...")
    
    sample_records = df_clean.sample(min(max_records, len(df_clean)), random_state=42)
    
    producer_buffer = []
    for idx, row in sample_records.iterrows():
        # Buat message payload seperti Kafka event
        event_message = {
            'timestamp': pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S'),
            'lokasi': row['Lokasi'],
            'rating': int(row['Rating']),
            'review_text': str(row['Review']),
            'metadata': {
                'panjang_karakter': int(row['panjang_review']),
                'jumlah_kata': int(row['jumlah_kata'])
            }
        }
        producer_buffer.append(event_message)
        print(f"  [PRODUSEN] Event terkirim ke queue: Lokasi={event_message['lokasi']}, Rating={event_message['rating']}")
        time.sleep(0.05) # Simulasi delay streaming
        
    # 2. Simulasi Consumer (Konsumen Data)
    print("\n[2/3] Memulai Consumer (Ingestion & Real-time Analytics)...")
    print("  Konsumen memproses stream dan menyaring alert ulasan buruk (Rating <= 3) secara instan...")
    
    alerts_triggered = 0
    with open(stream_file, 'w', encoding='utf-8') as f:
        for msg in producer_buffer:
            # Simulasi analisis real-time
            is_anomaly = msg['rating'] <= 3
            msg['real_time_analysis'] = {
                'is_alert_triggered': is_anomaly,
                'sentiment_flag': 'NEGATIF' if is_anomaly else 'POSITIF'
            }
            
            # Tulis ke file log streaming
            f.write(json.dumps(msg) + "\n")
            
            if is_anomaly:
                alerts_triggered += 1
                print(f"  [KONSUMEN - ALERT] Deteksi Rating Buruk di Cabang: {msg['lokasi']} (Rating {msg['rating']}) | Kritik: '{msg['review_text'][:50]}...'")
            else:
                print(f"  [KONSUMEN - INFO] Review diproses: Cabang={msg['lokasi']} | Sentiment=POSITIF")
                
    # 3. Hasil Simulasi
    print(f"\n[3/3] Simulasi big data streaming selesai.")
    print(f"  - Total Event Diproses: {len(producer_buffer)}")
    print(f"  - Total Alert Peringatan Dini Dipicu: {alerts_triggered}")
    print(f"  - Log streaming berhasil disimpan di: {stream_file}")
    
    print("\n" + "="*80)
    print("SIMULASI BIG DATA SELESAI")
    print("="*80 + "\n")
    return stream_file

if __name__ == '__main__':
    # Test run
    df_test = pd.read_csv('D:\\Gacoan\\Tugas_Data_Science\\outputs\\cleaned_dataset.csv')
    simulate_big_data_streaming(df_test, 'D:\\Gacoan\\Tugas_Data_Science\\outputs')
