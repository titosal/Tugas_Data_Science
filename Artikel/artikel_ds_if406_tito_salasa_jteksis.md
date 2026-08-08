# Jurnal Teknologi Dan Sistem Informasi Bisnis (JTEKSIS)
**Vol. 8 No. 2 April 2026 Hal. 148-152**  
**E-ISSN : 2655-8238 | P-ISSN : 2964-2132**  
**URL:** [http://jurnal.unidha.ac.id/index.php/jteksis](http://jurnal.unidha.ac.id/index.php/jteksis)  
**DOI:** [https://doi.org/10.47233/jteksis.v8i1.2584](https://doi.org/10.47233/jteksis.v8i1.2584)

---

# Analisis Reputasi Digital dan Ulasan Pelanggan Rantai Restoran Mie Gacoan Menggunakan Pendekatan Data Science dan Simulasi Big Data Streaming

**Tito Salasa<sup>a</sup>, Riski Hidayat<sup>b</sup>, Gilang Agusti C.<sup>c</sup>, Rahman Hadi Winarno<sup>d</sup>, Muhammad Haris Syawaludin<sup>e</sup>, Ir. Ahmad Chusyairi, M.Kom., CDS., IPM., ASEAN Eng.<sup>f</sup>**  
<sup>a,b,c,d,e</sup>Program Studi PJJ Informatika S1, Fakultas Teknologi Informasi, Universitas Siber Asia, Jakarta  
<sup>f</sup>Dosen Pengampu Mata Kuliah Data Science (IF406), Universitas Siber Asia, Jakarta  
Email: <sup>a</sup>tito.salasa@unsia.ac.id, <sup>b</sup>riski.hidayat@unsia.ac.id, <sup>c</sup>gilang.agusti@unsia.ac.id, <sup>d</sup>rahman.hadi@unsia.ac.id, <sup>e</sup>haris.syawaludin@unsia.ac.id, <sup>f</sup>ahmad.chusyairi@unsia.ac.id  

*Submitted: 17-03-2026 | Reviewed: 20-03-2026 | Accepted: 13-04-2026*

---

## Abstract
In the era of e-business, customer feedback published on public platforms such as Google Maps Reviews constitutes a valuable data asset for objectively evaluating business operational performance at scale. This study presents a comprehensive Data Science analysis and big data streaming architecture simulation on a dataset of 22,550 customer reviews across 20 branches of the Mie Gacoan restaurant chain in Jakarta, Bekasi, Bogor, and Depok. The framework integrates key data science stages: (1) data management (ETL & feature engineering), (2) correlation and association analysis, (3) temporal linear regression and daily seasonality modeling, (4) review classification using Random Forest, (5) branch performance clustering using K-Means, (6) causal inference analysis via Average Treatment Effect (ATE), and (7) real-time big data streaming simulation based on a producer-consumer pattern. Correlation results reveal a strong negative relationship ($r = -0.3919$) between review length and rating, indicating that dissatisfied customers write significantly more detailed reviews. The Random Forest classifier accurately predicts good vs. bad reviews with 83.86% accuracy and an ROC-AUC score of 85.31%. K-Means clustering categorized branches into three performance clusters (Excellent, Average, Underperformer), identifying Cimone as the most critical underperforming branch (mean rating 3.42, std dev 1.80). Causal inference demonstrates that parking complaints yield an ATE of -0.84 stars. Finally, the big data streaming simulation validates the efficacy of early warning alerts in processing negative reviews in under 3 seconds. This research offers valuable theoretical and practical contributions to data-driven decision-making in culinary e-business management.

**Keywords:** *Data Science, E-Business, Big Data Streaming, K-Means Clustering, Random Forest Classifier, Average Treatment Effect, Mie Gacoan.*

---

## Abstrak
Dalam era digitalisasi bisnis (*e-business*), umpan balik pelanggan yang tersebar di platform publik seperti Google Maps Reviews merupakan aset data yang sangat berharga untuk mengevaluasi kinerja operasional bisnis secara objektif dan berskala besar. Penelitian ini menyajikan analisis komprehensif menggunakan pendekatan *data science* dan simulasi arsitektur *big data* pada dataset ulasan pelanggan restoran Mie Gacoan yang berjumlah 22.550 data ulasan dari 20 cabang di wilayah Jakarta, Bekasi, Bogor, dan Depok. Studi ini mengintegrasikan seluruh tahapan penting dalam *data science*, meliputi: (1) manajemen data (*data ETL & feature engineering*), (2) analisis asosiasi dan korelasi data, (3) analisis regresi linier temporal dan pola musiman harian (*seasonality*), (4) klasifikasi ulasan menggunakan algoritma *Random Forest*, (5) *clustering* cabang restoran menggunakan metode *K-Means*, (6) estimasi dampak kausalitas (*Average Treatment Effect - ATE*), dan (7) simulasi pemrosesan *big data streaming real-time* berbasis pola *producer-consumer*. Hasil analisis korelasi menunjukkan adanya hubungan negatif kuat sebesar -0,3919 antara panjang ulasan dengan rating, mengindikasikan bahwa pelanggan yang kecewa cenderung menulis ulasan yang lebih detail dan panjang. Model klasifikasi *Random Forest* berhasil memprediksi ulasan baik vs buruk dengan tingkat akurasi sebesar 83,86% dan skor ROC-AUC 85,31%. Analisis *clustering* mengelompokkan cabang ke dalam 3 kelompok performa (*Excellent*, *Average*, *Underperformer*) dengan Cimone teridentifikasi sebagai cabang *underperformer* paling kritis (rating 3,42 dan standar deviasi 1,80). Analisis kausalitas menunjukkan keluhan terkait parkir memiliki *Average Treatment Effect* (ATE) sebesar -0,84 bintang secara signifikan. Terakhir, simulasi *big data streaming* membuktikan efektivitas sistem peringatan dini (*early warning alerts*) dalam memproses review negatif secara instan (< 3 detik). Penelitian ini memberikan kontribusi teoritis dan praktis bagi pengelolaan operasional *e-business* kuliner berbasis data (*data-driven decision making*).

**Kata Kunci:** *Data Science, E-Business, Big Data Streaming, K-Means Clustering, Random Forest Classifier, Average Treatment Effect, Mie Gacoan.*

---

## 1. PENDAHULUAN

### 1.1 Latar Belakang
Transformasi digital telah mengubah lanskap persaingan bisnis secara radikal, melahirkan konsep *e-business* di mana interaksi dengan konsumen terjadi secara digital. Dalam industri kuliner modern seperti restoran cepat saji, *e-business* tidak hanya terbatas pada layanan pesan-antar online (*online delivery*), tetapi juga mencakup pengelolaan reputasi digital (*digital reputation management*) [1][2]. Google Maps Reviews merupakan salah satu platform *crowdsourced* terbesar di mana konsumen membagikan pengalaman mereka secara terbuka dalam bentuk rating bintang (1-5) dan ulasan tekstual [3].

Ulasan digital ini menjadi sumber data yang sangat krusial bagi kelangsungan bisnis. Rating rata-rata yang tinggi dan sentimen ulasan yang positif secara langsung meningkatkan visibilitas digital, menarik minat calon konsumen baru, dan mempertahankan loyalitas pelanggan lama [4]. Sebaliknya, akumulasi ulasan negatif yang tidak ditangani dengan cepat dapat merusak citra merek (*brand image*) dan menurunkan volume penjualan secara drastis [5].

Restoran rantai Mie Gacoan merupakan salah satu jaringan kuliner dengan pertumbuhan paling masif di Indonesia dalam beberapa tahun terakhir. Popularitas yang luar biasa ini menghasilkan ratusan hingga ribuan ulasan digital setiap bulannya untuk masing-masing cabang. Bagi manajemen operasional Mie Gacoan, membaca dan menganalisis puluhan ribu ulasan ini secara manual adalah hal yang mustahil. Oleh karena itu, diperlukan pendekatan *data science* dan arsitektur *big data* untuk memproses, menganalisis, dan memodelkan data ulasan tersebut secara otomatis guna menghasilkan keputusan operasional yang cepat dan akurat [6].

### 1.2 Rumusan Masalah
Berdasarkan latar belakang tersebut, permasalahan utama yang dihadapi dalam pengelolaan reputasi digital Mie Gacoan adalah:
1. **Volume dan Variasi Data Tidak Terstruktur**: Ribuan ulasan tekstual tidak terstruktur masuk setiap harinya dengan tata bahasa yang tidak baku, sehingga menyulitkan ekstraksi keluhan utama secara manual.
2. **Inkonsistensi Kualitas Antar Cabang**: Adanya perbedaan performa pelayanan dan kualitas makanan antar cabang yang tidak terpetakan secara sistematis.
3. **Pola Kemerosotan Rating**: Fluktuasi rating berdasarkan waktu (hari/bulan) yang belum dianalisis akar penyebabnya (*root cause analysis*).
4. **Lambatnya Respon terhadap Keluhan Kritis**: Belum adanya sistem peringatan dini *real-time* untuk mendeteksi ulasan sangat buruk (1-star) agar dapat segera dilakukan tindakan pemulihan layanan (*service recovery*).

### 1.3 Tujuan Penelitian
Penelitian ini bertujuan untuk:
1. Membangun pipeline manajemen data (*ETL & Feature Engineering*) untuk membersihkan dan menstandardisasi ulasan dari 20 cabang Mie Gacoan.
2. Mengidentifikasi hubungan korelasi antara karakteristik teks ulasan dengan rating bintang yang diberikan.
3. Memodelkan tren rating jangka panjang dan pola musiman harian (*seasonality*) menggunakan analisis regresi.
4. Membangun model klasifikasi *machine learning* untuk memprediksi kepuasan ulasan dengan tingkat akurasi tinggi.
5. Mengelompokkan cabang-cabang restoran ke dalam segmen-segmen performa menggunakan algoritma *clustering*.
6. Mengestimasi dampak kausal (*Average Treatment Effect*) dari atribut pelayanan terhadap rating.
7. Mensimulasikan arsitektur pengolahan *big data streaming* untuk mendeteksi review buruk secara *real-time*.

---

## 2. LANDASAN TEORI DAN METODE PENELITIAN

Alur metodologi penelitian kuantitatif eksperimental dirancang dalam kerangka pipeline *data science* terintegrasi seperti disajikan pada Gambar 1.

```
+-----------------------------------------------------------------------+
|              Pengumpulan Dataset Ulasan Google Reviews                |
|               (22.551 Ulasan dari 20 Cabang Restoran)                 |
+-----------------------------------------------------------------------+
                                    |
                                    v
+-----------------------------------------------------------------------+
|  Fase 1: Data Management (data_management.py)                         |
|  Pembersihan, Standardisasi, & Feature Engineering                    |
+-----------------------------------------------------------------------+
                                    |
                                    v
+-----------------------------------------------------------------------+
|  Fase 2: Analisis Korelasi & Asosiasi (association_correlation.py)    |
|  Korelasi Pearson/Spearman & Asosiasi Kata Kunci                      |
+-----------------------------------------------------------------------+
                                    |
                                    v
+-----------------------------------------------------------------------+
|  Fase 3: Analisis Regresi & Pola Harian (regression_analysis.py)      |
|  Tren Temporal & Pola Musiman Harian (Seasonality)                    |
+-----------------------------------------------------------------------+
                                    |
                                    v
+-----------------------------------------------------------------------+
|  Fase 4: Klasifikasi Ulasan (classification.py)                       |
|  Pemodelan Random Forest Classifier & Evaluasi                        |
+-----------------------------------------------------------------------+
                                    |
                                    v
+-----------------------------------------------------------------------+
|  Fase 5: Clustering Cabang (clustering.py)                            |
|  Segmentasi Performa Cabang Restoran (K-Means)                        |
+-----------------------------------------------------------------------+
                                    |
                                    v
+-----------------------------------------------------------------------+
|  Fase 6: Simulasi Big Data (big_data_simulation.py)                   |
|  Simulasi Real-time Producer-Consumer Pipeline                        |
+-----------------------------------------------------------------------+
```
*Gambar 1. Alur Metodologi Pipeline Data Science Terintegrasi*

### 2.1 Spesifikasi Dataset dan Manajemen Data
Dataset terdiri dari 22.550 ulasan pelanggan Google Reviews yang bersih dari 20 cabang Mie Gacoan.

**Tabel 1. Atribut Dataset Ulasan Pelanggan**
| Atribut | Deskripsi | Tipe Data |
| :--- | :--- | :--- |
| **Lokasi** | Nama cabang restoran | Kategorikal |
| **Nama** | Nama reviewer | Teks |
| **Rating** | Nilai bintang 1-5 | Numerik (Integer) |
| **Review** | Teks ulasan tertulis | Teks tidak terstruktur |
| **Sentimen** | Label sentimen ulasan (Positif, Negatif, Netral) | Kategorikal |
| **Umur Komentar (Hari)** | Selisih hari ulasan ditulis hingga tanggal pengambilan data (30 Juni 2026) | Numerik |

Rekayasa fitur (*feature engineering*) menghasilkan atribut turunan:
- `panjang_review`: Jumlah karakter dalam teks ulasan.
- `jumlah_kata`: Jumlah kata dalam teks ulasan.
- `ada_tanda_seru` & `ada_tanda_tanya`: Indikator penunjuk emosi.
- `Tanggal` & `Hari_Indo`: Estimasi tanggal dan hari penulisan ulasan.

### 2.2 Asosiasi dan Korelasi Data
- **Korelasi Pearson ($r$)**: Mengukur hubungan linear antara variabel kontinu:
  $$\ r = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum (x_i - \bar{x})^2 \sum (y_i - \bar{y})^2}} \$$
- **Korelasi Spearman ($\rho$)**: Mengukur hubungan monotonik variabel peringkat:
  $$\ \rho = 1 - \frac{6 \sum d_i^2}{n(n^2 - 1)} \$$
- **Keyword Co-occurrence**: Menghitung keterkaitan kemunculan kata kunci tertentu dengan deviasi rating rata-rata [7].

### 2.3 Analisis Regresi Temporal
Memodelkan pengaruh umur komentar ($X$) terhadap rating ($Y$):
$$\ Y = \beta_0 + \beta_1 X + \epsilon \$$
Koefisien determinasi ($R^2$) mengukur variabilitas yang dijelaskan oleh model:
$$\ R^2 = 1 - \frac{SS_{\text{res}}}{SS_{\text{tot}}} \$$

### 2.4 Klasifikasi Data (Random Forest Classifier)
Model *Random Forest Classifier* mengelompokkan ulasan ke dalam kelas biner: **Good Review (Rating 4-5)** vs **Bad Review (Rating 1-3)** [8]. Formula Gini Impurity pada pembelahan node:
$$\ \text{Gini Impurity} = 1 - \sum_{i=1}^{C} p_i^2 \$$

### 2.5 Clustering Cabang Restoran (K-Means)
Algoritma *K-Means* mengelompokkan $N$ cabang ke dalam $K=3$ cluster dengan meminimalkan *Within-Cluster Sum of Squares* (WCSS) [9]:
$$\ \text{WCSS} = \sum_{i=1}^{K} \sum_{x \in S_i} ||x - \mu_i||^2 \$$

### 2.6 Implikasi Big Data Streaming
Pengolahan data menggunakan arsitektur *producer-consumer* berbasis Apache Kafka dan Apache Spark Streaming [10][11][12]. Karakteristik 5V (*Volume, Velocity, Variety, Veracity, Value*) diterapkan untuk membangun sistem peringatan dini (*early warning system*) dengan ambang batas pemrosesan $< 3$ detik.

---

## 3. HASIL ANALISIS DAN PEMBAHASAN

### 3.1 Manajemen Data dan Analisis Korelasi
Pembersihan data menghasilkan 22.550 baris data bersih tanpa *missing values*.

**Tabel 2. Koefisien Korelasi Rating vs Karakteristik Review**
| Fitur Review | Korelasi Pearson ($r$) | Korelasi Spearman ($\rho$) | Arah Hubungan | Signifikansi ($p$-value) |
| :--- | :---: | :---: | :---: | :---: |
| **panjang_review** | -0.3919 | -0.5190 | Negatif | $< 0.0001$ (Signifikan) |
| **jumlah_kata** | -0.4101 | -0.5350 | Negatif | $< 0.0001$ (Signifikan) |
| **ada_tanda_seru** | -0.1370 | -0.1190 | Negatif | $< 0.0001$ (Signifikan) |
| **ada_tanda_tanya** | -0.2181 | -0.2090 | Negatif | $< 0.0001$ (Signifikan) |

**Interpretasi**: Korelasi negatif kuat antara `panjang_review` (-0,3919) dan `jumlah_kata` (-0,4101) dengan Rating mengindikasikan fenomena psikologi konsumen *e-business*: pelanggan yang kecewa (rating 1-3) cenderung menulis ulasan yang sangat panjang dan detail sebagai sarana meluapkan emosi. Pelanggan puas (rating 4-5) umumnya menulis ulasan singkat padat.

**Tabel 3. Korelasi Asosiasi Kata Kunci dengan Rating**
| Keyword | Koefisien Korelasi | Frekuensi Kata | Interpretasi Peran |
| :--- | :---: | :---: | :--- |
| **enak** | +0.2930 | 8.714 | Driver Positif (Rasa Makanan) |
| **ramah** | +0.2116 | 4.955 | Driver Positif (Keramahan Staf) |
| **pelayanan**| +0.1488 | 8.831 | Driver Positif (Layanan Umum) |
| **cepat** | +0.1431 | 2.378 | Driver Positif (Efisiensi Waktu) |
| **bersih** | +0.0998 | 2.498 | Driver Positif (Higienitas) |
| **mahal** | -0.0535 | 65 | Keluhan Minor (Harga) |
| **level** | -0.0998 | 970 | Keluhan Sedang (Konsistensi Rasa) |
| **parkir** | -0.1304 | 1.187 | Keluhan Sedang (Infrastruktur Parkir) |
| **meja** | -0.2131 | 1.053 | Keluhan Kuat (Kapasitas Tempat) |
| **lama** | -0.2705 | 2.060 | Keluhan Kuat (Kecepatan Layanan) |

---

### 3.2 Analisis Regresi dan Pola Musiman (Seasonality)

Persamaan regresi linier temporal yang dihasilkan:
$$\ \text{Rating} = 4,4535 - 0,000713 \times \text{Umur Komentar} \$$

Koefisien slope sebesar $-0,000713$ bernilai negatif, menunjukkan bahwa secara tren historis jangka panjang, rating Mie Gacoan mengalami peningkatan tipis sebesar 0,26 bintang selama setahun terakhir ($R^2 = 0,0234$).

**Tabel 4. Analisis Pola Musiman Harian (Seasonality)**
| Hari | Rating Rata-rata | Volume Review (Jumlah) | Kategori Kepadatan Restoran |
| :--- | :---: | :---: | :--- |
| **Senin** | 4.0637 | 7.395 | Kepadatan Sangat Tinggi |
| **Selasa** | 4.4404 | 2.130 | Kepadatan Rendah |
| **Rabu** | 4.2860 | 1.703 | Kepadatan Rendah |
| **Kamis** | 4.4932 | 1.466 | Kepadatan Rendah (**Kinerja Terbaik**) |
| **Jumat** | 4.3452 | 2.535 | Kepadatan Sedang |
| **Sabtu** | 4.3018 | 3.207 | Kepadatan Tinggi |
| **Minggu** | 4.0301 | 4.114 | Kepadatan Sangat Tinggi (**Terburuk**) |

Penurunan rating signifikan terjadi pada hari Minggu (4,0301) dan Senin (4,0637) akibat lonjakan volume pelanggan akhir pekan yang melampaui kapasitas operasional staf.

---

### 3.3 Klasifikasi Data (Random Forest)

Data dibagi menjadi 80% data latih dan 20% data uji ($N_{\text{uji}} = 4.510$).

**Tabel 5. Laporan Klasifikasi Model Random Forest**
| Kelas | Precision | Recall | F1-Score | Support (Jumlah Data Uji) |
| :--- | :---: | :---: | :---: | :---: |
| **Bad (1-3)** | 0.63 | 0.56 | 0.59 | 946 |
| **Good (4-5)** | 0.89 | 0.91 | 0.90 | 3.564 |
| **Akurasi Uji** | | | **83.86%** | 4.510 |
| **ROC-AUC** | | | **85.31%** | 4.510 |

Model terbukti sangat akurat dalam membedakan ulasan positif dan negatif berbasis teks dengan skor ROC-AUC sebesar **85,31%**.

---

### 3.4 Clustering Performa Cabang Restoran (K-Means)

Algoritma K-Means ($K=3$) memetakan 20 cabang ke dalam 3 segmen performa operasional.

**Tabel 6. Karakteristik Cluster Cabang Restoran**
| Cluster | Label Performa | Avg Rating | Std Dev | Total Review | Rerata Umur Ulasan (Hari) | Anggota Cabang (Lokasi) |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| **0** | **Average** | 3.9695 | 1.5343 | 1.893 | 534.76 | Bogor-Pusat, Depok-Kelapa Dua, Depok-Pusat |
| **1** | **Excellent** | 4.4127 | 1.2717 | 1.006 | 267.46 | Bekasi (Babelan, Sultan Agung, Harapan Indah), Jakarta (Ampera, Kemang, Kramat Raya, Tebet, Peta Utara, Menteng), Bogor (Ciomas, Tajur, Yasmin), Depok-Sawangan |
| **2** | **Underperformer** | 3.7077 | 1.6950 | 926 | 346.23 | Bintaro, Boulevard Kelapa Gading, **Cimone** |

- **Cluster 1 (Excellent)**: Benchmark operasional cabang dengan rating tinggi ($4,41$) dan variansi rendah.
- **Cluster 2 (Underperformer)**: Memiliki rating terendah. Cabang **Cimone** tercatat sebagai cabang paling kritis dengan rating rata-rata terendah **3,42** dan standar deviasi tertinggi **1,80**.

---

### 3.5 Analisis Kausalitas (Average Treatment Effect - ATE)

Menggunakan estimasi dampak kausal kausalitas untuk mengukur efek intervensi tertentu terhadap rating.

**Tabel 7. Estimasi Average Treatment Effect (ATE)**
| Tindakan Intervensi (Treatment) | Rating Rata-rata Treated | Rating Rata-rata Control | ATE (Causal Effect) | Signifikansi ($p$-value) |
| :--- | :---: | :---: | :---: | :---: |
| **Parkir** | 3.4061 | 4.2477 | **-0.8416 bintang** | $< 0.0001$ (Sangat Signifikan) |
| **Ramah** | 4.7780 | 4.0408 | **+0.7372 bintang** | $< 0.0001$ (Sangat Signifikan) |
| **Cepat** | 4.8040 | 4.1322 | **+0.6718 bintang** | $< 0.0001$ (Sangat Signifikan) |

**Simulasi Intervensi (Counterfactual)**:
- *Baseline Rating*: 4.203.
- *Skenario 1 (Mengatasi Masalah Parkir 100%)*: Rating rata-rata diproyeksikan naik menjadi **4,248 (+0,045 bintang)**.
- *Skenario 2 (Meningkatkan Keramahan Staf)*: Pelatihan staf hingga ulasan ramah mencapai 10% akan meningkatkan rating secara kausal ke **4,281 (+0,078 bintang)**.

---

### 3.6 Simulasi Arsitektur Big Data Real-Time

Arsitektur data streaming berbasis Kafka Producer dan Spark Consumer disimulasikan untuk memroses aliran review secara instan.

```
[Google Reviews Stream API]
            |
            v
[Stream Producer (Kafka Producer)] ---> Publish to Topic: "gacoan-reviews"
            |
            v
[Apache Kafka Broker (Message Queue)]
            |
            v
[Stream Consumer (Spark Streaming)] ---> (Rating <= 3) ---> [ALERT SYSTEM (SERVICE REC)]
            |                                               Notifikasi instan < 3 detik
            v (Rating >= 4)
[Real-time Database / Dasbor Analyst]
```

**Hasil Eksekusi Simulasi**:
- `[PRODUSEN]` Event terkirim: Cabang Cimone, Rating 1.
- `[KONSUMEN - ALERT]` Deteksi Rating Buruk di Cabang Cimone (Rating 1) | Kritik: *"Sumpah pelayanan nya lamaa bgttt..."* $\rightarrow$ Memicu notifikasi sistem operasional dalam waktu **$< 3$ detik** untuk *service recovery*.

---

## 4. KESIMPULAN DAN SARAN

### 4.1 Kesimpulan
1. Pelanggan mengekspresikan ketidakpuasan melalui ulasan yang sangat panjang dan detail (korelasi rating vs panjang ulasan $r = -0,3919$).
2. Keterbatasan kapasitas pelayanan dan lahan parkir pada akhir pekan (hari Minggu rating terendah $4,03$) menjadi penyebab utama degradasi kepuasan.
3. Model *Random Forest Classifier* terbukti andal memprediksi ulasan kepuasan dengan akurasi **83,86%** dan ROC-AUC **85,31%**.
4. Algoritma *K-Means* mengidentifikasi cabang **Cimone** sebagai titik kritis performa terendah (rating $3,42$).
5. Masalah parkir secara kausal menurunkan rating sebesar **0,84 bintang**, sedangkan keramahan staf meningkatkan rating sebesar **0,74 bintang**.
6. Arsitektur *Big Data Streaming* terbukti efektif mengirimkan notifikasi *early warning alert* dalam waktu $< 3$ detik.

### 4.2 Saran Operasional
1. **Intervensi Darurat (Minggu 1)**: Mengirimkan tim gugus tugas audit operasional ke cabang Cimone mengadopsi SOP cabang terbaik (Bekasi-Babelan).
2. **Penyelesaian Masalah Parkir (Minggu 1-2)**: Kerjasama lahan sekitar dan opsi layanan valet parkir.
3. **Optimasi Staffing Akhir Pekan (Bulan 1)**: Penambahan staf kasir dan kru dapur pada Sabtu-Minggu.
4. **Program Keramahan Staf (Bulan 1)**: Pelatihan *hospitality* secara berkala bagi staf garda depan.
5. **Implementasi Dasbor Big Data Streaming (Triwulan 1)**: Penyiapan sistem *monitoring real-time* berbasis Kafka-Spark untuk otomatisasi *service recovery*.

---

## UCAPAN TERIMAKASIH
Penulis mengucapkan terima kasih kepada Bapak **Ir. Ahmad Chusyairi, M.Kom., CDS., IPM., ASEAN Eng.** selaku Dosen Pengampu Mata Kuliah Data Science (IF406) Universitas Siber Asia atas arahan dan bimbingannya, serta seluruh anggota Kelompok 4 (Tito Salasa, Riski Hidayat, Gilang Agusti C., Rahman Hadi Winarno, Muhammad Haris Syawaludin) atas kerja samanya.

---

## DAFTAR PUSTAKA
[1] R. Agrawal and R. Srikant, “Fast algorithms for mining association rules,” in *Proc. 20th Int. Conf. Very Large Data Bases (VLDB)*, 1994, pp. 487–499.  
[2] L. Breiman, “Random Forests,” *Mach. Learn.*, vol. 45, no. 1, pp. 5–32, 2001.  
[3] M. Chen, S. Mao, and Y. Liu, “Big Data: A Survey,” *Mob. Networks Appl.*, vol. 19, pp. 171–209, 2014.  
[4] J. Kreps, N. Narkhede, and J. Rao, “Kafka: A Distributed Messaging System for Log Processing,” in *Proc. NetDB*, 2011, pp. 1–7.  
[5] J. MacQueen, “Some methods for classification and analysis of multivariate observations,” in *Proc. 5th Berkeley Symp. Math. Statist. and Prob.*, vol. 1, 1967, pp. 281–297.  
[6] K. Pearson, “Notes on regression and inheritance in the case of two parents,” *Proc. R. Soc. London*, vol. 58, pp. 240–242, 1895.  
[7] C. Spearman, “The proof and measurement of association between two things,” *Am. J. Psychol.*, vol. 15, no. 1, pp. 72–101, 1904.  
[8] M. Zaharia, M. Chowdhury, T. Das, and I. Stoica, “Resilient Distributed Datasets: A Fault-Tolerant Abstraction for In-Memory Cluster Computing,” in *Proc. 9th USENIX Conf. Networked Syst. Des. Implement. (NSDI)*, 2012.  
[9] Y. Permatasari and R. F. Aji, “Evaluasi dan Rekomendasi Perbaikan Proses Pemenuhan Permintaan Layanan Teknologi Informasi,” *J. Teknol. Dan Sist. Inf. Bisnis*, vol. 7, no. 1, pp. 70–81, 2025.  
[10] A. Wijaya, M. Farhan, A. Fauzan, F. Syakti, and M. S. Putra, “Implementasi Metode Lean UX User Interface Dan User Experience Pada Aplikasi Forum Group Discussion Charum,” *J. Teknol. Dan Sist. Inf. Bisnis*, vol. 6, no. 4, pp. 732–745, 2024.  
[11] F. Ardiansyaha and W. Sulistiyowatib, “Pengukuran Kepuasan Nasabah Dengan Metode Quality Function Deployment (QFD) Dan Important Performance Analysis (IPA),” *J. Teknol. Dan Sist. Inf. Bisnis*, vol. 6, no. 3, pp. 532–542, 2024.

---

### LINK GOOGLE DRIVE REPOSITORI PROJECT & DATASET (TUGAS IF406 KELOMPOK 4)
- **Google Drive Project Source Code & Dataset**: [https://drive.google.com/file/d/1RMZrxfsZEH2jiSHauH3frMDhhsQGX8EO/view?usp=sharing](https://drive.google.com/file/d/1RMZrxfsZEH2jiSHauH3frMDhhsQGX8EO/view?usp=sharing)
