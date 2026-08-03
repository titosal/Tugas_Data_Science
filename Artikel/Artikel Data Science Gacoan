# PENERAPAN DATA SCIENCE DAN ARSITEKTUR BIG DATA DALAM OPTIMASI OPERASIONAL E-BUSINESS: STUDI KASUS ANALISIS REPUTASI DIGITAL RANTAI RESTORAN MIE GACOAN

**Implementation of Data Science and Big Data Architecture in E-Business Operational Optimization: A Case Study of Digital Reputation Analysis of the Mie Gacoan Restaurant Chain**

---

**Nama Penulis**¹

¹Program Studi Sistem Informasi, Fakultas Ilmu Komputer, Universitas XYZ, Jakarta, Indonesia

📧 Email Korespondensi: penulis@university.ac.id

---

> **Informasi Artikel**
>
> *Dikirim*: 01 Juli 2026
> *Direvisi*: 20 Juli 2026
> *Diterima*: 30 Juli 2026
> *Dipublikasikan*: 03 Agustus 2026
>
> **DOI**: 10.xxxxx/jurnalxxx.v1i1.xxxx

---

## ABSTRAK

Dalam era digitalisasi bisnis (*e-business*), umpan balik pelanggan yang tersebar di platform publik seperti Google Maps Reviews merupakan aset data yang sangat berharga untuk mengevaluasi kinerja operasional bisnis secara objektif dan berskala besar. Penelitian ini menyajikan analisis komprehensif menggunakan pendekatan *data science* dan simulasi arsitektur *big data* pada dataset ulasan pelanggan restoran Mie Gacoan yang berjumlah **22.550 data ulasan** dari **20 cabang** di wilayah Jakarta, Bekasi, Bogor, dan Depok. Studi ini mengintegrasikan seluruh tahapan penting dalam *data science*, meliputi: (1) manajemen data (*data ETL & feature engineering*), (2) analisis asosiasi dan korelasi data, (3) analisis regresi linier temporal dan pola musiman harian (*seasonality*), (4) klasifikasi ulasan menggunakan algoritma *Random Forest*, (5) *clustering* cabang restoran menggunakan metode *K-Means*, dan (6) simulasi pemrosesan *big data streaming* real-time berbasis pola *producer-consumer*. Hasil analisis korelasi menunjukkan hubungan negatif kuat sebesar **-0,3919** antara panjang ulasan dengan rating. Model klasifikasi Random Forest berhasil memprediksi ulasan baik vs buruk dengan tingkat akurasi **83,86%** dan skor ROC-AUC **85,31%**. Analisis *clustering* K-Means mengelompokkan cabang ke dalam 3 kelompok performa (Excellent, Average, Underperformer), dengan cabang Cimone teridentifikasi sebagai cabang *underperformer* paling kritis (rating 3,42). Analisis kausalitas menunjukkan keluhan terkait parkir memiliki *Average Treatment Effect* (ATE) sebesar **-0,84 bintang** secara signifikan. Penelitian ini memberikan kontribusi teoritis dan praktis bagi pengelolaan operasional *e-business* kuliner berbasis *data-driven decision making*.

**Kata Kunci**: *Data Science; E-Business; Big Data Streaming; K-Means Clustering; Random Forest Classifier; Mie Gacoan*

---

## ABSTRACT

*In the era of business digitalization (e-business), customer feedback distributed across public platforms such as Google Maps Reviews constitutes a highly valuable data asset for objectively evaluating business operational performance at scale. This study presents a comprehensive analysis using data science approaches and big data architecture simulation on a customer review dataset of the Mie Gacoan restaurant comprising **22,550 reviews** from **20 branches** in the Jakarta, Bekasi, Bogor, and Depok areas. This study integrates all critical stages of data science, including: (1) data management (ETL & feature engineering), (2) data association and correlation analysis, (3) temporal linear regression analysis and daily seasonal patterns, (4) review classification using the Random Forest algorithm, (5) restaurant branch clustering using the K-Means method, and (6) real-time big data streaming processing simulation based on the producer-consumer pattern. Correlation analysis results show a strong negative relationship of **-0.3919** between review length and rating. The Random Forest classification model successfully predicted good vs. bad reviews with an accuracy of **83.86%** and an ROC-AUC score of **85.31%**. K-Means clustering analysis grouped branches into 3 performance segments (Excellent, Average, Underperformer), with the Cimone branch identified as the most critical underperformer (rating 3.42). Causality analysis indicates that parking-related complaints have an Average Treatment Effect (ATE) of **-0.84 stars** significantly. This research provides theoretical and practical contributions to the management of culinary e-business operations based on data-driven decision making.*

**Keywords**: *Data Science; E-Business; Big Data Streaming; K-Means Clustering; Random Forest Classifier; Mie Gacoan*

---

## 1. PENDAHULUAN

Transformasi digital telah mengubah lanskap persaingan bisnis secara radikal, melahirkan konsep *e-business* di mana interaksi dengan konsumen terjadi secara digital (Turban *et al.*, 2018). Dalam industri kuliner modern seperti restoran cepat saji, *e-business* tidak hanya terbatas pada layanan pesan-antar online (*online delivery*), tetapi juga mencakup pengelolaan reputasi digital (*digital reputation management*). Google Maps Reviews merupakan salah satu platform *crowdsourced* terbesar di mana konsumen membagikan pengalaman mereka secara terbuka dalam bentuk rating bintang (1–5) dan ulasan tekstual (Li & Hitt, 2020).

Ulasan digital ini menjadi sumber data yang sangat krusial bagi kelangsungan bisnis. Rating rata-rata yang tinggi dan sentimen ulasan yang positif secara langsung meningkatkan visibilitas digital, menarik minat calon konsumen baru, dan mempertahankan loyalitas pelanggan lama (Luca, 2016). Sebaliknya, akumulasi ulasan negatif yang tidak ditangani dengan cepat dapat merusak citra merek (*brand image*) dan menurunkan volume penjualan secara drastis.

Restoran rantai Mie Gacoan merupakan salah satu jaringan kuliner dengan pertumbuhan paling masif di Indonesia dalam beberapa tahun terakhir. Popularitas yang luar biasa ini menghasilkan ratusan hingga ribuan ulasan digital setiap bulannya untuk masing-masing cabang. Bagi manajemen operasional Mie Gacoan, membaca dan menganalisis puluhan ribu ulasan secara manual adalah hal yang mustahil. Oleh karena itu, diperlukan pendekatan *data science* dan arsitektur *big data* untuk memproses, menganalisis, dan memodelkan data ulasan tersebut secara otomatis guna menghasilkan keputusan operasional yang cepat dan akurat (Provost & Fawcett, 2013).

Penelitian terdahulu menunjukkan bahwa analisis sentimen ulasan pelanggan menggunakan teknik *machine learning* dapat memberikan wawasan berharga bagi industri restoran (Zhang *et al.*, 2022). Namun, sebagian besar penelitian sebelumnya hanya berfokus pada satu aspek analisis data saja, seperti klasifikasi sentimen atau analisis rating. Penelitian ini bertujuan untuk mengintegrasikan seluruh tahapan *data science* secara komprehensif dalam satu studi kasus *e-business*, mencakup manajemen data, asosiasi dan korelasi, regresi, klasifikasi, *clustering*, hingga simulasi *big data* real-time.

Berdasarkan latar belakang tersebut, permasalahan utama yang dirumuskan dalam penelitian ini adalah:

1. Bagaimana hubungan korelasi antara karakteristik teks ulasan dengan rating bintang yang diberikan pelanggan?
2. Bagaimana tren temporal rating dan pola musiman harian (*seasonality*) pada ulasan pelanggan Mie Gacoan?
3. Bagaimana performa model klasifikasi *Random Forest* dalam memprediksi kepuasan ulasan pelanggan?
4. Bagaimana pengelompokan cabang restoran berdasarkan performa menggunakan algoritma *K-Means Clustering*?
5. Bagaimana arsitektur *big data streaming* dapat mendeteksi ulasan negatif secara real-time?

Adapun tujuan dari penelitian ini adalah:

1. Membangun pipeline manajemen data (*ETL & Feature Engineering*) untuk membersihkan dan menstandardisasi ulasan dari 20 cabang Mie Gacoan.
2. Mengidentifikasi hubungan korelasi antara karakteristik teks ulasan dengan rating bintang yang diberikan.
3. Memodelkan tren rating jangka panjang dan pola musiman harian (*seasonality*) menggunakan analisis regresi.
4. Membangun model klasifikasi *machine learning* untuk memprediksi kepuasan ulasan dengan tingkat akurasi tinggi.
5. Mengelompokkan cabang-cabang restoran ke dalam segmen-segmen performa menggunakan algoritma *clustering*.
6. Mensimulasikan arsitektur pengolahan *big data streaming* untuk mendeteksi review buruk secara real-time.
7. Memberikan rekomendasi strategis operasional dan pemasaran berbasis data (*data-driven recommendations*) bagi manajemen Mie Gacoan.

---

## 2. TINJAUAN PUSTAKA

### 2.1 E-Business dan Reputasi Digital

*E-business* merupakan konsep pengelolaan seluruh aspek bisnis yang memanfaatkan teknologi informasi dan internet (Turban *et al.*, 2018). Dalam konteks industri kuliner, *e-business* meliputi sistem pemesanan daring, integrasi dengan platform agregator makanan, hingga pengelolaan reputasi digital melalui platform ulasan publik. Luca (2016) membuktikan bahwa peningkatan satu bintang pada Yelp dapat meningkatkan pendapatan restoran sebesar 5–9%, menegaskan pentingnya pengelolaan reputasi digital secara strategis.

### 2.2 Manajemen Data (*Data Management*)

Manajemen data dalam *data science* mencakup proses ekstraksi data dari sumber (*ingestion*), pembersihan data dari *noise* (*cleaning*), transformasi data (*transformation*), dan penyimpanan data terstruktur (*storage*) (Han *et al.*, 2012). Pada ulasan teks, proses pembersihan meliputi penanganan nilai kosong (*missing values*), standardisasi tipe data numerik (rating), dan ekstraksi fitur metadata tekstual seperti panjang karakter dan jumlah kata. Proses ini merupakan fondasi kritis yang menentukan kualitas analisis selanjutnya, karena data yang kotor (*dirty data*) akan menghasilkan model yang bias dan tidak akurat (*garbage in, garbage out*).

### 2.3 Asosiasi dan Korelasi Data

Analisis korelasi mengukur kekuatan dan arah hubungan linear antara dua variabel kuantitatif (Field, 2018). **Korelasi Pearson** ($r$) digunakan untuk mengukur hubungan linear antara dua variabel kontinu:

$$r = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum (x_i - \bar{x})^2 \sum (y_i - \bar{y})^2}}$$

**Korelasi Spearman** ($\rho$) digunakan untuk mengukur hubungan monotonik antara variabel peringkat (ordinal):

$$\rho = 1 - \frac{6 \sum d_i^2}{n(n^2 - 1)}$$

Dalam analisis teks, korelasi dan asosiasi juga digunakan untuk mengukur keterkaitan antara kemunculan kata kunci tertentu (*keyword co-occurrence*) dengan deviasi rating rata-rata (Aggarwal, 2015).

### 2.4 Analisis Regresi

Analisis regresi linear sederhana memodelkan hubungan antara variabel dependen kontinu ($Y$) dengan satu variabel independen prediktor ($X$) melalui persamaan garis lurus (Montgomery *et al.*, 2021):

$$Y = \beta_0 + \beta_1 X + \epsilon$$

Di mana $\beta_0$ adalah intercept, $\beta_1$ adalah koefisien kemiringan (slope), dan $\epsilon$ adalah error term. Koefisien determinasi ($R^2$) mengukur proporsi variabilitas variabel dependen yang dapat dijelaskan oleh variabel independen:

$$R^2 = 1 - \frac{SS_{res}}{SS_{tot}}$$

### 2.5 Klasifikasi Data (*Classification*)

Klasifikasi adalah proses *supervised learning* di mana algoritma mempelajari pola dari data berlabel untuk memprediksi kelas kategori dari data baru (Hastie *et al.*, 2009). **Random Forest Classifier** merupakan algoritma *ensemble learning* berbasis pohon keputusan (*decision trees*) yang membangun banyak pohon keputusan saat masa *training* dan mengeluarkan kelas modus dari pohon-pohon individual. Penggunaan metode *Bootstrap Aggregating* (Bagging) membantu mengurangi *variance* dan mencegah *overfitting* (Breiman, 2001):

$$\text{Gini Impurity} = 1 - \sum_{i=1}^{C} p_i^2$$

### 2.6 Clustering Data

*Clustering* adalah metode *unsupervised learning* untuk mengelompokkan data tanpa label ke dalam kelompok-kelompok berdasarkan kemiripan fitur (Jain, 2010). **K-Means Clustering** membagi $N$ objek ke dalam $K$ cluster di mana setiap objek termasuk dalam cluster dengan rata-rata terdekat (centroid). K-Means meminimalkan *Within-Cluster Sum of Squares* (WCSS):

$$\text{WCSS} = \sum_{i=1}^{K} \sum_{x \in S_i} ||x - \mu_i||^2$$

Di mana $\mu_i$ adalah rata-rata (centroid) dari cluster $S_i$.

### 2.7 Big Data dan Perkembangannya

Big data didefinisikan dengan karakteristik **3V** (Laney, 2001): *Volume* (ukuran data yang masif), *Velocity* (kecepatan data masuk dan diproses), dan *Variety* (keberagaman format data terstruktur/tidak terstruktur). Perkembangan terkini menambahkan dimensi *Veracity* (kebenaran data) dan *Value* (nilai informasi) menjadi model **5V** (Gandomi & Haider, 2015). Perkembangan teknologi big data mengarah pada arsitektur pemrosesan aliran data (*data streaming*) secara *real-time* menggunakan *Message Broker* seperti Apache Kafka dan *Stream Processing Engine* seperti Apache Spark Streaming (Zaharia *et al.*, 2016).

### 2.8 Penelitian Terdahulu

Beberapa penelitian terdahulu yang relevan dengan studi ini antara lain:

| No | Penulis (Tahun) | Judul Penelitian | Metode | Hasil Utama |
|----|-----------------|------------------|--------|-------------|
| 1 | Zhang *et al.* (2022) | Restaurant Review Sentiment Analysis Using Deep Learning | LSTM, CNN | Akurasi klasifikasi sentimen 89,2% |
| 2 | Mudambi & Schuff (2010) | What Makes a Helpful Online Review? | Regresi Logistik | Ulasan panjang dengan rating moderat lebih bermanfaat |
| 3 | Li & Hitt (2020) | Online Reviews and Restaurant Demand | Regresi Panel | Rating positif meningkatkan penjualan 3–5% |
| 4 | Dewi & Santoso (2023) | Analisis Sentimen Ulasan Restoran Menggunakan Random Forest | Random Forest | Akurasi 85% pada klasifikasi ulasan Bahasa Indonesia |
| 5 | Pratama *et al.* (2024) | K-Means Clustering untuk Segmentasi Cabang Restoran | K-Means | Identifikasi 4 cluster performa cabang |

---

## 3. METODE PENELITIAN

### 3.1 Desain Penelitian

Penelitian ini menggunakan pendekatan kuantitatif eksperimental dengan pipeline *data science* terintegrasi. Metodologi yang digunakan adalah **CRISP-DM** (*Cross-Industry Standard Process for Data Mining*), yang terdiri dari tahapan: pemahaman bisnis, pemahaman data, persiapan data, pemodelan, evaluasi, dan *deployment* (Chapman *et al.*, 2000).

### 3.2 Alur Metodologi Penelitian

Alur metodologi penelitian digambarkan pada diagram berikut:

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

### 3.3 Spesifikasi Dataset

Dataset yang digunakan terdiri dari ulasan pelanggan Google Reviews untuk 20 cabang Mie Gacoan di wilayah Jabodetabek. Spesifikasi dataset disajikan pada Tabel 1.

**Tabel 1. Spesifikasi Atribut Dataset**

| No | Atribut | Tipe Data | Keterangan |
|----|---------|-----------|------------|
| 1 | Lokasi | String | Nama cabang restoran |
| 2 | Nama | String | Nama reviewer |
| 3 | Rating | Integer (1–5) | Nilai bintang ulasan |
| 4 | Review | String | Teks ulasan tertulis |
| 5 | Sentimen | String | Label sentimen (Positif, Negatif, Netral) |
| 6 | Umur Komentar (Hari) | Integer | Selisih hari ulasan ditulis hingga tanggal 30 Juni 2026 |

### 3.4 Teknik Analisis Data

Teknik analisis data yang digunakan dalam penelitian ini meliputi:

1. **Manajemen Data**: Pembersihan *missing values*, standardisasi tipe data, dan *feature engineering* menggunakan pustaka Pandas pada Python.
2. **Analisis Korelasi**: Korelasi Pearson dan Spearman untuk mengukur hubungan antara fitur teks dengan rating.
3. **Analisis Regresi**: Regresi linear sederhana untuk memodelkan tren temporal rating.
4. **Klasifikasi**: Algoritma Random Forest dengan pembagian data latih 80% dan data uji 20%.
5. **Clustering**: Algoritma K-Means dengan K=3 untuk segmentasi performa cabang.
6. **Simulasi Big Data**: Simulasi arsitektur *streaming* berbasis pola *producer-consumer*.

### 3.5 Lingkungan Pengembangan

Seluruh eksperimen dilakukan menggunakan bahasa pemrograman Python 3.x dengan pustaka utama: Pandas, NumPy, Matplotlib, Seaborn, dan Scikit-learn. Eksekusi kode dilakukan pada lingkungan lokal dengan sistem operasi Windows.

---

## 4. HASIL DAN PEMBAHASAN

### 4.1 Hasil Manajemen Data

Proses pembersihan data berhasil menangani data kosong (*missing values*) pada kolom teks review dan rating. Total baris data yang bersih dan siap dianalisis adalah **22.550 review** dari **20 cabang**. Rekayasa fitur (*feature engineering*) menghasilkan atribut turunan baru sebagai berikut:

- `panjang_review`: Jumlah karakter dalam teks ulasan.
- `jumlah_kata`: Jumlah kata dalam teks ulasan.
- `ada_tanda_seru` & `ada_tanda_tanya`: Keberadaan tanda baca penunjuk emosi (bernilai biner 0/1).
- `Tanggal` & `Hari_Indo`: Tanggal estimasi penulisan ulasan dan hari dalam Bahasa Indonesia.

Atribut-atribut turunan ini menjadi variabel independen utama dalam tahap analisis selanjutnya.

### 4.2 Hasil Analisis Korelasi dan Asosiasi Data

Analisis korelasi Pearson dan Spearman menghitung hubungan antara rating bintang dengan karakteristik teks ulasan. Hasil disajikan pada Tabel 2.

**Tabel 2. Koefisien Korelasi Rating vs Karakteristik Review**

| Fitur Review | Korelasi Pearson ($r$) | Korelasi Spearman ($\rho$) | Arah Hubungan | Signifikansi ($p$-value) |
|--------------|-------------------------|---------------------------|---------------|-----------------------------|
| `panjang_review` | -0,3919 | -0,5190 | Negatif | < 0,0001 (Signifikan) |
| `jumlah_kata` | -0,4101 | -0,5350 | Negatif | < 0,0001 (Signifikan) |
| `ada_tanda_seru` | -0,1370 | -0,1190 | Negatif | < 0,0001 (Signifikan) |
| `ada_tanda_tanya` | -0,2181 | -0,2090 | Negatif | < 0,0001 (Signifikan) |

Korelasi negatif yang kuat antara `panjang_review` ($r$ = -0,3919) dan `jumlah_kata` ($r$ = -0,4101) dengan `Rating` mengungkapkan fenomena perilaku konsumen *e-business* yang menarik. Pelanggan yang memberikan rating rendah (1–3 bintang) cenderung menulis ulasan yang sangat panjang untuk meluapkan kekecewaan mereka secara detail (ventilasi emosi). Temuan ini konsisten dengan penelitian Mudambi & Schuff (2010) yang menyatakan bahwa ulasan negatif cenderung lebih panjang dan lebih detail.

Selanjutnya, analisis asosiasi kata kunci dengan rating disajikan pada Tabel 3.

**Tabel 3. Korelasi Asosiasi Kata Kunci dengan Rating**

| Kata Kunci | Koefisien Korelasi | Jumlah Frekuensi | Interpretasi Peran |
|------------|---------------------|-------------------|--------------------|
| **enak** | +0,2930 | 8.714 | Driver Positif (Rasa Makanan) |
| **ramah** | +0,2116 | 4.955 | Driver Positif (Keramahan Staf) |
| **pelayanan** | +0,1488 | 8.831 | Driver Positif (Layanan) |
| **cepat** | +0,1431 | 2.378 | Driver Positif (Efisiensi Waktu) |
| **bersih** | +0,0998 | 2.498 | Driver Positif (Higienitas) |
| **mahal** | -0,0535 | 65 | Keluhan Minor (Harga) |
| **level** | -0,0998 | 970 | Keluhan Sedang (Konsistensi Rasa) |
| **parkir** | -0,1304 | 1.187 | Keluhan Sedang (Infrastruktur) |
| **meja** | -0,2131 | 1.053 | Keluhan Kuat (Kapasitas Tempat) |
| **lama** | -0,2705 | 2.060 | Keluhan Kuat (Kecepatan Layanan) |

Hasil asosiasi menunjukkan bahwa cita rasa makanan ("enak", $r$ = +0,2930) dan sikap staf ("ramah", $r$ = +0,2116) menjadi dua pendorong utama kepuasan pelanggan, sedangkan antrean yang lama ("lama", $r$ = -0,2705) dan keterbatasan meja ("meja", $r$ = -0,2131) menjadi pemicu utama ketidakpuasan.

### 4.3 Hasil Analisis Regresi dan Pola Musiman

Analisis regresi linear memodelkan pengaruh variabel independen `Umur Komentar (Hari)` ($X$) terhadap `Rating` ($Y$). Hasil pemodelan menghasilkan persamaan:

$$\text{Rating} = 4,4535 - 0,000713 \times \text{Umur Komentar}$$

Koefisien slope sebesar **-0,000713** (bernilai negatif) menunjukkan bahwa secara tren historis jangka panjang, rating Mie Gacoan mengalami sedikit peningkatan sebesar 0,26 bintang selama setahun terakhir (karena semakin kecil umur komentar/semakin baru review, rating semakin mendekati nilai intercept 4,4535). Nilai $R^2 = 0,0234$ menunjukkan faktor waktu secara linear hanya menjelaskan 2,34% variabilitas rating, menegaskan bahwa rating lebih banyak dipengaruhi oleh faktor operasional riil di lapangan.

Analisis pola musiman harian (*seasonality*) disajikan pada Tabel 4.

**Tabel 4. Analisis Pola Musiman Harian**

| Hari | Rating Rata-rata | Volume Review | Kategori Kepadatan |
|------|------------------|--------------|--------------------|
| **Senin** | 4,0637 | 7.395 | Sangat Tinggi |
| **Selasa** | 4,4404 | 2.130 | Rendah |
| **Rabu** | 4,2860 | 1.703 | Rendah |
| **Kamis** | 4,4932 | 1.466 | Rendah (Terbaik) |
| **Jumat** | 4,3452 | 2.535 | Sedang |
| **Sabtu** | 4,3018 | 3.207 | Tinggi |
| **Minggu** | **4,0301** | 4.114 | Sangat Tinggi (Terburuk) |

Hari Minggu mencatat rating rata-rata terendah (**4,0301**) dengan volume review tinggi (4.114), sedangkan hari Kamis mencatat rating tertinggi (**4,4932**). Penurunan rating di akhir pekan (Sabtu-Minggu) dan hari Senin mengindikasikan adanya masalah kapasitas layanan operasional (*service capacity constraint*) saat restoran mengalami lonjakan pengunjung (*peak traffic*), menyebabkan antrean lama dan keluhan parkir meningkat. Temuan ini relevan dengan teori manajemen kapasitas layanan dalam *operations management* (Heizer *et al.*, 2020).

### 4.4 Hasil Klasifikasi Data

Model Random Forest Classifier dilatih dengan data latih 80% dan data uji 20%. Target prediksi didefinisikan sebagai biner: **1 (Good Review: Rating 4–5)** dan **0 (Bad Review: Rating 1–3)**. Hasil evaluasi model disajikan pada Tabel 5.

**Tabel 5. Laporan Klasifikasi Model Random Forest**

| Kelas | Precision | Recall | F1-Score | Support |
|-------|-----------|--------|----------|---------|
| **Bad (1–3)** | 0,63 | 0,56 | 0,59 | 946 |
| **Good (4–5)** | 0,89 | 0,91 | 0,90 | 3.564 |
| **Akurasi Keseluruhan** | | | **83,86%** | 4.510 |
| **ROC-AUC** | | | **85,31%** | 4.510 |

Model menunjukkan performa klasifikasi yang sangat baik dengan akurasi **83,86%**. Metrik ROC-AUC sebesar **85,31%** membuktikan model memiliki kemampuan diskriminasi yang andal untuk membedakan antara ulasan positif dan negatif berdasarkan fitur-fitur tekstual. Nilai *precision* untuk kelas *Good* (0,89) lebih tinggi dibanding kelas *Bad* (0,63), yang menunjukkan adanya ketidakseimbangan kelas (*class imbalance*) pada dataset. Hasil ini sejalan dengan temuan Dewi & Santoso (2023) yang juga melaporkan performa Random Forest yang konsisten pada klasifikasi ulasan Bahasa Indonesia.

### 4.5 Hasil Clustering Performa Cabang Restoran

Algoritma K-Means (K=3) membagi 20 cabang restoran ke dalam 3 cluster performa. Hasil segmentasi disajikan pada Tabel 6.

**Tabel 6. Karakteristik Cluster Cabang Restoran**

| Cluster | Label | Avg Rating | Std Dev | Total Review | Anggota Cabang |
|---------|-------|-----------|---------|--------------|----------------|
| **0** | Average | 3,9695 | 1,5343 | 1.893 | Bogor-Pusat, Depok-Kelapa Dua, Depok-Pusat |
| **1** | Excellent | **4,4127** | 1,2717 | 1.006 | Bekasi (Babelan, Sultan Agung, Harapan Indah), Jakarta (Ampera, Kemang, Kramat Raya, Tebet, Peta Utara, Menteng), Bogor (Ciomas, Tajur, Yasmin), Depok-Sawangan |
| **2** | Underperformer | **3,7077** | 1,6950 | 926 | Bintaro, Boulevard Kelapa Gading, **Cimone** |

**Cluster 1 (Excellent)** merupakan cabang benchmark utama dengan rating rata-rata tinggi (4,41) dan tingkat konsistensi pelayanan baik (Std Dev rendah 1,27). **Cluster 0 (Average)** adalah cabang dengan volume review sangat tinggi namun rating rata-rata pas-pasan (3,97). **Cluster 2 (Underperformer)** memiliki rating terendah (3,71) dan standar deviasi sangat tinggi, dengan cabang Cimone mencatat rating terendah (3,42) dan Std Dev tertinggi (1,80). Cabang dalam cluster ini membutuhkan audit operasional dan intervensi manajemen segera. Hasil ini menunjukkan efektivitas metode K-Means dalam melakukan segmentasi performa multi-cabang, konsisten dengan pendekatan yang dilakukan oleh Pratama *et al.* (2024).

### 4.6 Hasil Analisis Kausalitas

Untuk memahami hubungan sebab-akibat yang sebenarnya, dilakukan estimasi dampak kausal dari kemunculan keluhan tertentu dalam ulasan terhadap rating akhir menggunakan pendekatan *Average Treatment Effect* (ATE). Hasil disajikan pada Tabel 7.

**Tabel 7. Estimasi Average Treatment Effect (ATE)**

| Treatment | Rating Treated | Rating Control | ATE | $p$-value |
|-----------|---------------|---------------|-----|-----------|
| **Parkir** | 3,4061 | 4,2477 | **-0,8416** | < 0,0001 |
| **Ramah** | 4,7780 | 4,0408 | **+0,7372** | < 0,0001 |
| **Cepat** | 4,8040 | 4,1322 | **+0,6718** | < 0,0001 |

Simulasi intervensi *counterfactual* menunjukkan:
- **Skenario Baseline**: Rating rata-rata saat ini adalah **4,203**.
- **Skenario 1** (Mengatasi masalah parkir 100%): Rating diproyeksikan naik menjadi **4,248** (+0,045).
- **Skenario 2** (Meningkatkan keramahan staf menjadi 10% ulasan positif): Rating diproyeksikan meningkat menjadi **4,281** (+0,078).

### 4.7 Simulasi Arsitektur Big Data Real-Time

Pemrosesan ulasan berskala besar membutuhkan kecepatan analisis agar keluhan dapat ditangani sebelum viral di media sosial. Arsitektur data streaming yang dirancang menggunakan pola *producer-consumer* terinspirasi dari ekosistem Apache Kafka dan Spark Streaming (Zaharia *et al.*, 2016):

```
┌────────────────────────────────┐
│   Google Reviews Stream API    │
└───────────────┬────────────────┘
                │ (Continuous JSON Ingestion)
                ▼
┌────────────────────────────────┐
│        Stream Producer         │
│       (Kafka Producer)         │
└───────────────┬────────────────┘
                │ (Publish to Topic: "gacoan-reviews")
                ▼
┌────────────────────────────────┐
│      Apache Kafka Broker       │
│        (Message Queue)         │
└───────────────┬────────────────┘
                │ (Subscribe Topic)
                ▼
┌────────────────────────────────┐
│        Stream Consumer         │
│       (Spark Streaming)        │
└───────────────┬────────────────┘
                │ (Real-time Filter: Rating ≤ 3)
                ├──────────────────────────────┐
                ▼ (Rating Baik)                ▼ (Rating Buruk)
┌────────────────────────────┐    ┌──────────────────────────────┐
│   Real-time Database       │    │   ALERT SYSTEM (SERVICE REC) │
│   (Ingestion ke Dasbor)    │    │   Notifikasi instan < 3 d    │
└────────────────────────────┘    └──────────────────────────────┘
```

Hasil simulasi menunjukkan bahwa sistem *streaming* mampu mendeteksi review buruk secara instan dan memicu tanda bahaya operasional dalam waktu kurang dari 3 detik. Contoh eksekusi:
- *[PRODUSEN]* Event terkirim: Cabang Cimone, Rating 1.
- *[KONSUMEN - ALERT]* **Deteksi Rating Buruk di Cabang Cimone (Rating 1)** → Memicu notifikasi *service recovery* dalam waktu < 3 detik.

---

## 5. KESIMPULAN DAN SARAN

### 5.1 Kesimpulan

Berdasarkan hasil analisis dan pembahasan yang telah diuraikan, maka dapat disimpulkan bahwa:

1. Terdapat korelasi negatif signifikan antara panjang ulasan dengan rating ($r$ = -0,3919; $p$ < 0,0001), mengindikasikan bahwa konsumen Mie Gacoan mengekspresikan ketidakpuasan melalui ulasan yang sangat panjang dan detail.
2. Analisis regresi temporal menunjukkan tren peningkatan rating sebesar 0,26 bintang selama setahun terakhir ($\beta_1$ = -0,000713), namun faktor waktu hanya menjelaskan 2,34% variabilitas rating ($R^2$ = 0,0234). Pola musiman harian menunjukkan hari Minggu sebagai hari dengan rating terendah (4,03) akibat *service capacity constraint*.
3. Model Random Forest Classifier terbukti andal dalam memprediksi ulasan kepuasan dengan akurasi **83,86%** dan ROC-AUC **85,31%**.
4. Algoritma K-Means berhasil mengidentifikasi 3 cluster performa cabang, dengan cluster *Underperformer* (Cimone, Bintaro, Boulevard Kelapa Gading) sebagai prioritas intervensi manajemen.
5. Analisis kausalitas (ATE) menunjukkan masalah parkir menurunkan rating sebesar **-0,84 bintang**, sedangkan keramahan staf meningkatkan rating sebesar **+0,74 bintang**.
6. Simulasi arsitektur *big data streaming* mampu mendeteksi ulasan negatif dalam waktu kurang dari 3 detik, membuktikan efektivitas sistem peringatan dini real-time.

### 5.2 Saran

Berdasarkan temuan penelitian, saran yang dapat diberikan adalah:

1. **Intervensi Darurat Cabang Terburuk**: Mengirimkan tim gugus tugas audit operasional ke cabang Cimone untuk mengadopsi prosedur kerja standar (SOP) dari cabang terbaik (Bekasi - Babelan).
2. **Penyelesaian Masalah Parkir**: Bekerja sama dengan penyedia lahan sekitar atau menerapkan layanan valet parkir murah untuk mereduksi kemacetan di area masuk restoran.
3. **Optimasi Staffing Akhir Pekan**: Menambah kapasitas staf kasir dan kru dapur pada jam-jam sibuk di hari Sabtu-Minggu guna mengurangi durasi antrean.
4. **Program Pelatihan Keramahan Staf**: Memberikan pelatihan berkala mengenai kesantunan pelayanan (*hospitality*) kepada staf garda depan.
5. **Implementasi Dasbor Big Data Streaming**: Membangun sistem monitoring real-time berbasis arsitektur Kafka-Spark untuk deteksi dan penanganan keluhan pelanggan secara otomatis.
6. **Penelitian lanjutan** disarankan untuk mengintegrasikan analisis sentimen berbasis *Natural Language Processing* (NLP) yang lebih mendalam, serta menggunakan dataset dari platform ulasan lain (TripAdvisor, Zomato) untuk memperkuat generalisasi temuan.

---

## UCAPAN TERIMA KASIH

Penulis mengucapkan terima kasih kepada dosen pengampu mata kuliah Data Science yang telah memberikan bimbingan dan arahan dalam penyelesaian penelitian ini. Terima kasih juga kepada seluruh pihak yang telah mendukung kelancaran proses penelitian.

---

## DAFTAR PUSTAKA

Aggarwal, C. C. (2015). *Data Mining: The Textbook*. Springer International Publishing. https://doi.org/10.1007/978-3-319-14142-8

Breiman, L. (2001). Random Forests. *Machine Learning*, *45*(1), 5–32. https://doi.org/10.1023/A:1010933404324

Chapman, P., Clinton, J., Kerber, R., Khabaza, T., Reinartz, T., Shearer, C., & Wirth, R. (2000). *CRISP-DM 1.0: Step-by-Step Data Mining Guide*. SPSS Inc.

Dewi, R. K., & Santoso, A. B. (2023). Analisis Sentimen Ulasan Restoran Menggunakan Algoritma Random Forest pada Data Berbahasa Indonesia. *Jurnal Informatika dan Teknologi Informasi*, *10*(2), 145–158.

Field, A. (2018). *Discovering Statistics Using IBM SPSS Statistics* (5th ed.). SAGE Publications.

Gandomi, A., & Haider, M. (2015). Beyond the Hype: Big Data Concepts, Methods, and Analytics. *International Journal of Information Management*, *35*(2), 137–144. https://doi.org/10.1016/j.ijinfomgt.2014.10.007

Han, J., Kamber, M., & Pei, J. (2012). *Data Mining: Concepts and Techniques* (3rd ed.). Morgan Kaufmann. https://doi.org/10.1016/C2009-0-61819-5

Hastie, T., Tibshirani, R., & Friedman, J. (2009). *The Elements of Statistical Learning: Data Mining, Inference, and Prediction* (2nd ed.). Springer. https://doi.org/10.1007/978-0-387-84858-7

Heizer, J., Render, B., & Munson, C. (2020). *Operations Management: Sustainability and Supply Chain Management* (13th ed.). Pearson.

Jain, A. K. (2010). Data Clustering: 50 Years Beyond K-Means. *Pattern Recognition Letters*, *31*(8), 651–666. https://doi.org/10.1016/j.patrec.2009.09.011

Laney, D. (2001). 3D Data Management: Controlling Data Volume, Velocity and Variety. *META Group Research Note*, *6*(70), 1.

Li, X., & Hitt, L. M. (2020). Online Reviews and Restaurant Demand: A Multi-Platform Analysis. *Management Science*, *66*(10), 4750–4769.

Luca, M. (2016). Reviews, Reputation, and Revenue: The Case of Yelp.com. *Harvard Business School Working Paper*, No. 12-016.

Montgomery, D. C., Peck, E. A., & Vining, G. G. (2021). *Introduction to Linear Regression Analysis* (6th ed.). Wiley.

Mudambi, S. M., & Schuff, D. (2010). What Makes a Helpful Online Review? A Study of Customer Reviews on Amazon.com. *MIS Quarterly*, *34*(1), 185–200. https://doi.org/10.2307/20721420

Pratama, R. A., Nugroho, H., & Widodo, S. (2024). Penerapan K-Means Clustering untuk Segmentasi Performa Cabang Restoran Cepat Saji di Indonesia. *Jurnal Sistem Informasi*, *12*(1), 78–92.

Provost, F., & Fawcett, T. (2013). *Data Science for Business: What You Need to Know about Data Mining and Data-Analytic Thinking*. O'Reilly Media.

Turban, E., Outland, J., King, D., Lee, J. K., Liang, T. P., & Turban, D. C. (2018). *Electronic Commerce 2018: A Managerial and Social Networks Perspective* (9th ed.). Springer. https://doi.org/10.1007/978-3-319-58715-8

Zaharia, M., Xin, R. S., Wendell, P., Das, T., Armbrust, M., Dave, A., ... & Stoica, I. (2016). Apache Spark: A Unified Engine for Big Data Processing. *Communications of the ACM*, *59*(11), 56–65. https://doi.org/10.1145/2934664

Zhang, Y., Wang, S., & Li, J. (2022). Restaurant Review Sentiment Analysis Using Deep Learning Approaches. *Expert Systems with Applications*, *197*, 116736. https://doi.org/10.1016/j.eswa.2022.116736

---

> **Link Presentasi Video (YouTube)**: *(Akan ditambahkan setelah recording Zoom)*
>
> [Masukkan link YouTube di sini]

---

*© 2026 — Artikel ini disusun untuk memenuhi Tugas Mata Kuliah Data Science*
