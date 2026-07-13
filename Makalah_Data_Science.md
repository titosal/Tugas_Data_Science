# MAKALAH AKADEMIK: PENERAPAN DATA SCIENCE DAN ARSITEKTUR BIG DATA DALAM OPTIMASI OPERASIONAL E-BUSINESS
## (Studi Kasus: Analisis Reputasi Digital dan Ulasan Pelanggan Rantai Restoran Mie Gacoan)

---

### ABSTRAK
Dalam era digitalisasi bisnis (*e-business*), umpan balik pelanggan yang tersebar di platform publik seperti Google Maps Reviews merupakan aset data yang sangat berharga untuk mengevaluasi kinerja operasional bisnis secara objektif dan berskala besar. Penelitian ini menyajikan analisis komprehensif menggunakan pendekatan *data science* dan simulasi arsitektur *big data* pada dataset ulasan pelanggan restoran Mie Gacoan yang berjumlah **22.550 data ulasan** dari **20 cabang** di wilayah Jakarta, Bekasi, Bogor, dan Depok. Studi ini mengintegrasikan seluruh tahapan penting dalam *data science*, meliputi: (1) manajemen data (*data ETL & feature engineering*), (2) analisis asosiasi dan korelasi data, (3) analisis regresi linier temporal dan pola musiman harian (*seasonality*), (4) klasifikasi ulasan menggunakan algoritma *Random Forest*, (5) *clustering* cabang restoran menggunakan metode *K-Means*, dan (6) simulasi pemrosesan *big data streaming* real-time berbasis pola *producer-consumer*.

Hasil analisis korelasi menunjukkan adanya hubungan negatif kuat sebesar **-0,3919** antara panjang ulasan dengan rating, mengindikasikan bahwa pelanggan yang kecewa cenderung menulis ulasan yang lebih detail dan panjang. Model klasifikasi Random Forest berhasil memprediksi ulasan baik vs buruk dengan tingkat akurasi sebesar **83,86%** dan skor ROC-AUC **85,31%**. Analisis *clustering* mengelompokkan cabang ke dalam 3 kelompok performa (Excellent, Average, Underperformer) dengan Cimone teridentifikasi sebagai cabang *underperformer* paling kritis (rating 3,42 dan standar deviasi 1,80). Analisis kausalitas menunjukkan keluhan terkait parkir memiliki *Average Treatment Effect* (ATE) sebesar **-0,84 bintang** secara signifikan. Terakhir, simulasi *big data streaming* membuktikan efektivitas sistem peringatan dini (*early warning alerts*) dalam memproses review negatif secara instan (<3 detik). Penelitian ini memberikan kontribusi teoritis dan praktis yang berharga bagi pengelolaan operasional *e-business* kuliner berbasis data (*data-driven decision making*).

**Kata Kunci**: *Data Science, E-Business, Big Data Streaming, K-Means Clustering, Random Forest Classifier, Average Treatment Effect, Mie Gacoan.*

---

## 1. PENDAHULUAN

### 1.1 Latar Belakang Masalah
Transformasi digital telah mengubah lanskap persaingan bisnis secara radikal, melahirkan konsep *e-business* di mana interaksi dengan konsumen terjadi secara digital. Dalam industri kuliner modern seperti restoran cepat saji, *e-business* tidak hanya terbatas pada layanan pesan-antar online (*online delivery*), tetapi juga mencakup pengelolaan reputasi digital (*digital reputation management*). Google Maps Reviews merupakan salah satu platform *crowdsourced* terbesar di mana konsumen membagikan pengalaman mereka secara terbuka dalam bentuk rating bintang (1-5) dan ulasan tekstual.

Ulasan digital ini menjadi sumber data yang sangat krusial bagi kelangsungan bisnis. Rating rata-rata yang tinggi dan sentimen ulasan yang positif secara langsung meningkatkan visibilitas digital, menarik minat calon konsumen baru, dan mempertahankan loyalitas pelanggan lama. Sebaliknya, akumulasi ulasan negatif yang tidak ditangani dengan cepat dapat merusak citra merek (*brand image*) dan menurunkan volume penjualan secara drastis.

Restoran rantai Mie Gacoan merupakan salah satu jaringan kuliner dengan pertumbuhan paling masif di Indonesia dalam beberapa tahun terakhir. Popularitas yang luar biasa ini menghasilkan ratusan hingga ribuan ulasan digital setiap bulannya untuk masing-masing cabang. Bagi manajemen operasional Mie Gacoan, membaca dan menganalisis puluhan ribu ulasan ini secara manual adalah hal yang mustahil. Oleh karena itu, diperlukan pendekatan *data science* dan arsitektur *big data* untuk memproses, menganalisis, dan memodelkan data ulasan tersebut secara otomatis guna menghasilkan keputusan operasional yang cepat dan akurat.

### 1.2 Identifikasi Masalah
Berdasarkan latar belakang tersebut, permasalahan utama yang dihadapi dalam pengelolaan reputasi digital Mie Gacoan adalah:
1. **Volume dan Variasi Data Tidak Terstruktur**: Ribuan ulasan tekstual tidak terstruktur masuk setiap harinya dengan tata bahasa yang tidak baku, sehingga menyulitkan ekstraksi keluhan utama secara manual.
2. **Inkonsistensi Kualitas Antar Cabang**: Adanya perbedaan performa pelayanan dan kualitas makanan antar cabang yang tidak terpetakan secara sistematis.
3. **Pola Kemerosotan Rating**: Fluktuasi rating berdasarkan waktu (hari/bulan) yang belum dianalisis akar penyebabnya (*root cause analysis*).
4. **Lambatnya Respon terhadap Keluhan Kritis**: Belum adanya sistem peringatan dini real-time untuk mendeteksi ulasan sangat buruk (1-star) agar dapat segera dilakukan tindakan pemulihan layanan (*service recovery*).

### 1.3 Tujuan Penelitian
Penelitian ini bertujuan untuk:
1. Membangun pipeline manajemen data (*ETL & Feature Engineering*) untuk membersihkan dan menstandardisasi ulasan dari 20 cabang Mie Gacoan.
2. Mengidentifikasi hubungan korelasi antara karakteristik teks ulasan dengan rating bintang yang diberikan.
3. Memodelkan tren rating jangka panjang dan pola musiman harian (*seasonality*) menggunakan analisis regresi.
4. Membangun model klasifikasi *machine learning* untuk memprediksi kepuasan ulasan dengan tingkat akurasi tinggi.
5. Mengelompokkan cabang-cabang restoran ke dalam segmen-segmen performa menggunakan algoritma *clustering*.
6. Mensimulasikan arsitektur pengolahan *big data streaming* untuk mendeteksi review buruk secara real-time.
7. Memberikan rekomendasi strategis operasional dan pemasaran berbasis data (*data-driven recommendations*) bagi manajemen Mie Gacoan.

---

## 2. LANDASAN TEORI

### 2.1 Manajemen Data (*Data Management*)
Manajemen data dalam *data science* mencakup proses ekstraksi data dari sumber (*ingestion*), pembersihan data dari *noise* (*cleaning*), transformasi data (*transformation*), dan penyimpanan data terstruktur (*storage*). Pada ulasan teks, proses pembersihan meliputi penanganan nilai kosong (*missing values*), standardisasi tipe data numerik (rating), dan ekstraksi fitur metadata tekstual seperti panjang karakter dan jumlah kata. 

### 2.2 Asosiasi dan Korelasi Data
Analisis korelasi mengukur kekuatan dan arah hubungan linear antara dua variabel kuantitatif. 
- **Korelasi Pearson ($r$)** digunakan untuk mengukur hubungan linear antara dua variabel kontinu:
  $$r = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum (x_i - \bar{x})^2 \sum (y_i - \bar{y})^2}}$$
- **Korelasi Spearman ($\rho$)** digunakan untuk mengukur hubungan monotonik antara variabel peringkat (ordinal):
  $$\rho = 1 - \frac{6 \sum d_i^2}{n(n^2 - 1)}$$
Dalam analisis teks, korelasi dan asosiasi juga digunakan untuk mengukur keterkaitan antara kemunculan kata kunci tertentu (*keyword co-occurrence*) dengan deviasi rating rata-rata.

### 2.3 Analisis Regresi
Analisis regresi linear sederhana memodelkan hubungan antara variabel dependen kontinu ($Y$) dengan satu variabel independen prediktor ($X$) melalui persamaan garis lurus:
$$Y = \beta_0 + \beta_1 X + \epsilon$$
Di mana $\beta_0$ adalah intercept, $\beta_1$ adalah koefisien kemiringan (slope), dan $\epsilon$ adalah error term. Koefisien determinasi ($R^2$) mengukur proporsi variabilitas variabel dependen yang dapat dijelaskan oleh variabel independen:
$$R^2 = 1 - \frac{SS_{res}}{SS_{tot}}$$

### 2.4 Klasifikasi Data (*Classification*)
Klasifikasi adalah proses *supervised learning* di mana algoritma mempelajari pola dari data berlabel untuk memprediksi kelas kategori dari data baru.
- **Random Forest Classifier**: Algoritma *ensemble learning* berbasis pohon keputusan (*decision trees*). Algoritma ini membangun banyak pohon keputusan saat masa *training* dan mengeluarkan kelas modus (klasifikasi) dari pohon-pohon individual tersebut. Penggunaan metode *Bootstrap Aggregating* (Bagging) membantu mengurangi *variance* dan mencegah *overfitting*:
  $$\text{Gini Impurity} = 1 - \sum_{i=1}^{C} p_i^2$$

### 2.5 Clustering Data
*Clustering* adalah metode *unsupervised learning* untuk mengelompokkan data tanpa label ke dalam kelompok-kelompok berdasarkan kemiripan fitur.
- **K-Means Clustering**: Algoritma yang membagi $N$ objek ke dalam $K$ cluster di mana setiap objek termasuk dalam cluster dengan rata-rata terdekat (centroid). K-Means meminimalkan *Within-Cluster Sum of Squares* (WCSS):
  $$\text{WCSS} = \sum_{i=1}^{K} \sum_{x \in S_i} ||x - \mu_i||^2$$
  Di mana $\mu_i$ adalah rata-rata (centroid) dari cluster $S_i$.

### 2.6 Big Data dan Perkembangannya
Big data didefinisikan dengan karakteristik **3V**: *Volume* (ukuran data yang masif), *Velocity* (kecepatan data masuk dan diproses), dan *Variety* (keberagaman format data terstruktur/tidak terstruktur). 
Perkembangan teknologi big data mengarah pada arsitektur pemrosesan aliran data (*data streaming*) secara *real-time*. Penggunaan *Message Broker* seperti Apache Kafka dan *Stream Processing Engine* seperti Apache Spark Streaming menjadi standar industri untuk menangani aliran data ulasan pelanggan secara terus-menerus (*continuous ingestion*) untuk analisis instan.

---

## 3. METODOLOGI PENELITIAN

Penelitian ini menggunakan pendekatan kuantitatif eksperimental dengan pipeline *data science* terintegrasi. Alur metodologi penelitian digambarkan pada diagram berikut:

```
┌─────────────────────────────────────────────────────────┐
│              Pengumpulan Dataset Ulasan                 │
│         (22.551 Ulasan, 20 Cabang Restoran)             │
└────────────────────────────┬────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────┐
│        Fase 1: Data Management (data_management.py)      │
│     Pembersihan, Standardisasi, & Feature Engineering    │
└────────────────────────────┬────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────┐
│  Fase 2: Analisis Korelasi (association_correlation.py) │
│          Korelasi Pearson/Spearman & Asosiasi Teks       │
└────────────────────────────┬────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────┐
│    Fase 3: Analisis Regresi (regression_analysis.py)    │
│           Tren Temporal & Analisis Harian (Seasonality)  │
└────────────────────────────┬────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────┐
│       Fase 4: Klasifikasi Ulasan (classification.py)     │
│             Pemodelan Random Forest Classifier          │
└────────────────────────────┬────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────┐
│        Fase 5: Clustering Cabang (clustering.py)        │
│          Segmentasi Performa Cabang (K-Means)           │
└────────────────────────────┬────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────┐
│  Fase 6: Big Data Simulation (big_data_simulation.py)   │
│       Simulasi Real-time Producer-Consumer Pipeline    │
└─────────────────────────────────────────────────────────┘
```

### 3.1 Spesifikasi Dataset
Dataset yang digunakan terdiri dari ulasan pelanggan Google Reviews untuk 20 cabang Mie Gacoan dengan atribut:
- **Lokasi**: Nama cabang restoran.
- **Nama**: Nama reviewer.
- **Rating**: Nilai bintang 1-5.
- **Review**: Teks ulasan tertulis.
- **Sentimen**: Label sentimen ulasan (Positif, Negatif, Netral).
- **Umur Komentar (Hari)**: Selisih hari ulasan ditulis hingga tanggal pengambilan data (30 Juni 2026).

---

## 4. HASIL ANALISIS DAN PEMBAHASAN

### 4.1 Manajemen Data (*Data Management*)
Proses pembersihan data berhasil menangani data kosong (*missing values*) pada kolom teks review dan rating. Total baris data yang bersih dan siap dianalisis adalah **22.550 review** dari **20 cabang**.
Rekayasa fitur menghasilkan atribut baru:
- `panjang_review`: Jumlah karakter dalam teks ulasan.
- `jumlah_kata`: Jumlah kata dalam teks ulasan.
- `ada_tanda_seru` & `ada_tanda_tanya`: Keberadaan tanda baca penunjuk emosi.
- `Tanggal` & `Hari_Indo`: Tanggal estimasi penulisan ulasan dan hari dalam Bahasa Indonesia.

### 4.2 Analisis Korelasi dan Asosiasi Data
Analisis korelasi Pearson dan Spearman menghitung hubungan antara rating bintang dengan karakteristik teks ulasan.

#### Tabel 1. Koefisien Korelasi Rating vs Karakteristik Review
| Fitur Review | Korelasi Pearson ($r$) | Korelasi Spearman ($\rho$) | Arah Hubungan | Signifikansi ($p$-value) |
|--------------|-------------------------|---------------------------|---------------|--------------------------|
| `panjang_review` | -0,3919 | -0,5190 | Negatif | < 0.0001 (Signifikan) |
| `jumlah_kata` | -0,4101 | -0,5350 | Negatif | < 0.0001 (Signifikan) |
| `ada_tanda_seru` | -0,1370 | -0,1190 | Negatif | < 0.0001 (Signifikan) |
| `ada_tanda_tanya` | -0,2181 | -0,2090 | Negatif | < 0.0001 (Signifikan) |

#### Interpretasi:
Korelasi negatif yang kuat antara `panjang_review` (-0,3919) dan `jumlah_kata` (-0,4101) dengan `Rating` mengungkapkan fenomena perilaku konsumen *e-business*. Pelanggan yang memberikan rating rendah (1-3 bintang) cenderung menulis ulasan yang sangat panjang untuk meluapkan kekecewaan mereka secara detail (ventilasi emosi). Sebaliknya, pelanggan yang puas (rating 4-5) cenderung menulis ulasan yang singkat dan langsung pada inti (misal: "enak cepat ramah").

#### Tabel 2. Korelasi Asosiasi Kata Kunci dengan Rating
| Keyword | Koefisien Korelasi | Jumlah Frekuensi Kata | Interpretasi Peran |
|---------|---------------------|-----------------------|--------------------|
| **enak** | +0,2930 | 8.714 | Driver Positif (Rasa Makanan) |
| **ramah** | +0,2116 | 4.955 | Driver Positif (Keramahan Staf) |
| **pelayanan** | +0,1488 | 8.831 | Driver Positif (Layanan) |
| **cepat** | +0,1431 | 2.378 | Driver Positif (Efisiensi Waktu) |
| **bersih** | +0,0998 | 2.498 | Driver Positif (Higienitas) |
| **mahal** | -0,0535 | 65 | Keluhan Minor (Harga) |
| **level** | -0,0998 | 970 | Keluhan Sedang (Konsistensi Rasa)|
| **parkir** | -0,1304 | 1.187 | Keluhan Sedang (Infrastruktur) |
| **meja** | -0,2131 | 1.053 | Keluhan Kuat (Kapasitas Tempat) |
| **lama** | -0,2705 | 2.060 | Keluhan Kuat (Kecepatan Layanan) |

Data di atas menunjukkan bahwa cita rasa makanan ("enak") dan sikap staf ("ramah") adalah dua pendorong utama kepuasan pelanggan, sedangkan antrean yang lama ("lama") dan keterbatasan meja ("meja") menjadi pemicu utama ketidakpuasan.

### 4.3 Analisis Regresi dan Pola Musiman (*Seasonality*)
Analisis regresi linear memodelkan pengaruh variabel independen `Umur Komentar (Hari)` ($X$) terhadap `Rating` ($Y$):
$$\text{Rating} = 4,4535 - 0,000713 \times \text{Umur Komentar}$$

Koefisien slope sebesar **-0,000713** (bernilai negatif) menunjukkan bahwa secara tren historis jangka panjang, rating Mie Gacoan mengalami sedikit peningkatan sebesar 0,26 bintang selama setahun terakhir (karena semakin kecil umur komentar/semakin baru review, rating semakin mendekati nilai intercept 4,4535). Nilai $R^2 = 0,0234$ menunjukkan faktor waktu secara linear hanya menjelaskan 2,34% variabilitas rating, menegaskan bahwa rating lebih banyak dipengaruhi oleh faktor operasional riil di lapangan.

#### Tabel 3. Analisis Pola Musiman Harian (*Seasonality*)
| Hari | Rating Rata-rata | Volume Review (Jumlah) | Kategori Kepadatan Restoran |
|------|------------------|------------------------|-----------------------------|
| **Senin** | 4,0637 | 7.395 | Kepadatan Sangat Tinggi |
| **Selasa** | 4,4404 | 2.130 | Kepadatan Rendah |
| **Rabu** | 4,2860 | 1.703 | Kepadatan Rendah |
| **Kamis** | 4,4932 | 1.466 | Kepadatan Rendah (Kinerja Terbaik) |
| **Jumat** | 4,3452 | 2.535 | Kepadatan Sedang |
| **Sabtu** | 4,3018 | 3.207 | Kepadatan Tinggi |
| **Minggu** | **4,0301** | 4.114 | Kepadatan Sangat Tinggi (Terburuk) |

#### Analisis:
Hari Minggu mencatat rating rata-rata terendah (**4,0301**) dengan volume review yang sangat tinggi (4.114). Sebaliknya, hari Kamis mencatat rating tertinggi (**4,4932**). Penurunan rating di akhir pekan (Sabtu-Minggu) dan hari Senin mengindikasikan adanya masalah kapasitas layanan operasional (*service capacity constraint*) saat restoran mengalami lonjakan pengunjung (*peak traffic*), menyebabkan antrean lama dan keluhan parkir meningkat.

### 4.4 Klasifikasi Data (*Classification*)
Kami melatih Random Forest Classifier dengan data latih 80% dan data uji 20%. Target prediksi didefinisikan sebagai biner: **1 (Good Review: Rating 4-5)** dan **0 (Bad Review: Rating 1-3)**.

#### Tabel 4. Laporan Klasifikasi Model (Random Forest)
| Kelas | Precision | Recall | F1-Score | Support (Jumlah Data Uji) |
|-------|-----------|--------|----------|---------------------------|
| **Bad (1-3)** | 0,63 | 0,56 | 0,59 | 946 |
| **Good (4-5)** | 0,89 | 0,91 | 0,90 | 3.564 |
| **Akurasi Uji** | | | **83,86%** | 4.510 |
| **ROC-AUC** | | | **85,31%** | 4.510 |

Model menunjukkan performa klasifikasi yang sangat baik dengan akurasi **83,86%**. Metrik ROC-AUC sebesar **85,31%** membuktikan model memiliki kemampuan diskriminasi yang andal untuk membedakan antara ulasan positif dan negatif berdasarkan fitur-fitur tekstual.

### 4.5 Clustering Performa Cabang Restoran
Algoritma K-Means (K=3) membagi 20 cabang restoran ke dalam 3 cluster performa.

#### Tabel 5. Karakteristik Cluster Cabang Restoran
| Cluster | Label Performa | Avg Rating | Std Dev | Total Review | Rata-rata Umur Ulasan (Hari) | Anggota Cabang (Lokasi) |
|---------|----------------|------------|---------|--------------|------------------------------|------------------------|
| **0** | Average | 3,9695 | 1,5343 | 1.893 | 534,76 | Bogor-Pusat, Depok-Kelapa Dua, Depok-Pusat |
| **1** | Excellent | **4,4127** | 1,2717 | 1.006 | 267,46 | Bekasi (Babelan, Sultan Agung, Harapan Indah), Jakarta (Ampera, Kemang, Kramat Raya, Tebet, Peta Utara, Menteng), Bogor (Ciomas, Tajur, Yasmin), Depok-Sawangan |
| **2** | Underperformer | **3,7077** | 1,6950 | 926 | 346,23 | Bintaro, Boulevard Kelapa Gading, **Cimone** |

#### Analisis:
- **Cluster 1 (Excellent)** adalah cabang benchmark utama dengan rating rata-rata tinggi (4,41) dan tingkat konsistensi pelayanan yang baik (Std Dev rendah).
- **Cluster 2 (Average)** adalah cabang raksasa dengan volume review sangat tinggi (terutama Depok-Kelapa Dua dengan 2.260 review), tetapi memiliki rating rata-rata pas-pasan (3,96).
- **Cluster 3 (Underperformer)** memiliki rating terendah dan standar deviasi sangat tinggi (Cimone mencatat rating terendah 3,42 dan Std Dev tertinggi 1,80). Cabang dalam cluster ini membutuhkan audit operasional dan intervensi manajemen segera.

### 4.6 Analisis Kausalitas (Average Treatment Effect - ATE)
Untuk memahami hubungan sebab-akibat yang sebenarnya, kami mengestimasi dampak kausal dari kemunculan keluhan tertentu dalam ulasan terhadap rating akhir.

#### Tabel 6. Estimasi Average Treatment Effect (ATE)
| Tindakan Intervensi (Treatment) | Rating Rata-rata Treated | Rating Rata-rata Control | ATE (Causal Effect) | Signifikansi ($p$-value) |
|---------------------------------|--------------------------|--------------------------|---------------------|--------------------------|
| **Parkir** | 3,4061 | 4,2477 | **-0,8416 bintang** | < 0.0001 (Sangat Signifikan) |
| **Ramah** | 4,7780 | 4,0408 | **+0,7372 bintang** | < 0.0001 (Sangat Signifikan) |
| **Cepat** | 4,8040 | 4,1322 | **+0,6718 bintang** | < 0.0001 (Sangat Signifikan) |

#### Simulasi Intervensi (Counterfactual):
- **Skenario Baseline**: Rating rata-rata saat ini adalah **4,203**.
- **Skenario 1 (Mengatasi Masalah Parkir 100%)**: Jika masalah parkir diatasi sepenuhnya (sehingga keluhan parkir menjadi 0%), rating rata-rata rantai restoran diproyeksikan naik menjadi **4,248** (+0,045).
- **Skenario 2 (Meningkatkan Keramahan Staf)**: Jika pelatihan keramahan berhasil meningkatkan ulasan positif tentang staf menjadi 10% dari total ulasan (sekarang baru 2,2%), rating rata-rata akan meningkat secara kausal ke **4,281** (+0,078).

---

## 5. SIMULASI ARSITEKTUR BIG DATA REAL-TIME

Pemrosesan ulasan berskala besar membutuhkan kecepatan analisis agar keluhan dapat ditangani sebelum viral di media sosial. Kami merancang arsitektur data streaming untuk menangani aliran review real-time:

```
┌────────────────────────────────┐
│   Google Reviews Stream API    │
└───────────────┬────────────────┘
                │ (Continuous JSON Ingestion)
                ▼
┌────────────────────────────────┐
│        Stream Producer         │ (Mensimulasikan pengiriman review
│       (Kafka Producer)         │  sebagai message queue payload)
└───────────────┬────────────────┘
                │ (Publish to Topic: "gacoan-reviews")
                ▼
┌────────────────────────────────┐
│      Apache Kafka Broker       │ (Mengelola antrean pesan secara
│        (Message Queue)         │  terdistribusi dan aman)
└───────────────┬────────────────┘
                │ (Subscribe Topic)
                ▼
┌────────────────────────────────┐
│        Stream Consumer         │ (Mengkonsumsi pesan, ekstraksi metadata
│       (Spark Streaming)        │  dan klasifikasi sentimen instan)
└───────────────┬────────────────┘
                │ (Real-time Filter: Rating <= 3)
                ├──────────────────────────────────────┐
                ▼ (Jika Rating Baik)                   ▼ (Jika Rating Buruk)
┌────────────────────────────────┐      ┌──────────────────────────────┐
│       Real-time Database       │      │   ALERT SYSTEM (SERVICE REC) │
│     (Ingestion ke Dasbor)      │      │    Notifikasi instan < 3 d   │
└────────────────────────────────┘      └──────────────────────────────┘
```

### Simulasi Hasil Eksekusi Pipeline Streaming:
Ketika simulator produsen mengirimkan ulasan secara terus-menerus, konsumen Spark Streaming mendeteksi review buruk secara instan dan memicu tanda bahaya operasional:
- *[PRODUSEN]* Event terkirim: Cabang Cimone, Rating 1.
- *[KONSUMEN - ALERT]* **Deteksi Rating Buruk di Cabang Cimone (Rating 1) | Kritik: "Sumpah pelayanan nya lamaa bgttt..."** -> Memicu notifikasi sistem operasional dalam waktu < 3 detik untuk *service recovery*.

---

## 6. KESIMPULAN DAN REKOMENDASI

### 6.1 Kesimpulan
Penelitian data science komprehensif pada e-business Mie Gacoan menyimpulkan:
1. Konsumen Mie Gacoan mengekspresikan ketidakpuasan mereka melalui ulasan yang sangat panjang dan detail (korelasi rating vs panjang ulasan sebesar -0,3919).
2. Keterbatasan kapasitas pelayanan operasional dan ketersediaan lahan parkir di akhir pekan (khususnya hari Minggu) menjadi faktor utama degradasi kepuasan konsumen (rating Minggu terendah 4,03).
3. Model Random Forest Classifier terbukti andal dalam memprediksi ulasan kepuasan dengan akurasi 83,86%.
4. Cluster cabang underperformer (Cimone, Bintaro, Boulevard Kelapa Gading) teridentifikasi secara jelas, dengan Cimone sebagai titik kritis performa terendah (rating 3,42).
5. Masalah parkir secara kausalitas menurunkan rating sebesar 0,84 bintang, sedangkan keramahan staf meningkatkan rating sebesar 0,74 bintang.

### 6.2 Rekomendasi Strategis (Action Plan)
1. **Intervensi Darurat Cabang Terburuk (Week 1)**: Mengirimkan tim gugus tugas audit operasional ke cabang Cimone untuk mengadopsi prosedur kerja standar (SOP) dari cabang terbaik (Bekasi - Babelan).
2. **Penyelesaian Masalah Parkir (Week 1-2)**: Bekerja sama dengan penyedia lahan sekitar atau menerapkan layanan valet parkir murah untuk mereduksi kemacetan di area masuk restoran.
3. **Optimasi Staffing Akhir Pekan (Month 1)**: Menambah kapasitas staf kasir dan kru dapur pada jam-jam sibuk di hari Sabtu-Minggu guna mengurangi durasi antrean masakan ("lama" dan "nunggu").
4. **Program Layanan Keramahan Staf (Month 1)**: Memberikan pelatihan berkala mengenai kesantunan pelayanan (*hospitality*) kepada staf garda depan (kasir dan penyaji), karena hal ini terbukti secara kausal meningkatkan sentimen rating.
5. **Implementasi Dasbor Big Data Streaming (Quarter 1)**: Membangun sistem monitoring real-time berbasis arsitektur Kafka-Spark untuk mendeteksi ulasan negatif secara cepat dan mengotomatiskan respon penanganan keluhan pelanggan.
