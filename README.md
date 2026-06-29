# PBL - Compression Image Using PCA
**Kelompok 1 · Informatika 2025D · Universitas Sebelas Maret (2026)**

---

## Deskripsi Singkat

Repositori ini berisi aplikasi web interaktif untuk **Kompresi Citra** berbasis metode **Principal Component Analysis (PCA)**. Aplikasi ini dirancang dengan antarmuka modern menggunakan **Flask** sebagai *backend* dan *Cyberpunk Glassmorphism UI* pada *frontend*-nya.

Proyek ini dikembangkan sebagai bagian dari **Project Based Learning (PBL)** untuk mata kuliah **Aljabar Linear** di Program Studi Informatika, Universitas Sebelas Maret.

### Cara Kerja Program

1. **Pemisahan Channel Warna:** Gambar RGB yang diunggah diekstraksi ke dalam 3 matriks channel terpisah (Red, Green, Blue).

2. **Reduksi Dimensi (Per Channel):** Menghitung nilai rata-rata (*mean*) dan memusatkan data (*centering*).
   * Menghitung Matriks Kovarian (*Covariance Matrix*).
   * Mencari nilai eigen (*eigenvalues*) dan vektor eigen (*eigenvectors*).
   * Mengurutkan dan mengambil *K* komponen utama terbesar sesuai input *slider* pengguna.
3. **Rekonstruksi & Penggabungan:** Gambar dibangun ulang dari komponen utama yang terpilih, digabungkan kembali menjadi citra RGB, dan dioptimalkan ukurannya.

---

## Teknologi yang Digunakan

| Komponen | Teknologi / Library | Deskripsi Fungsi |
| :--- | :--- | :--- |
| **Backend Core** | Python & Flask | Menangani rute aplikasi, *file handling*, dan API kompresi. |
| **Komputasi Matriks** | NumPy | Komputasi aljabar linear (Matriks Kovarian, Eigen, Dot Product). |
| **Image Processing** | Pillow (PIL) | Membuka, memanipulasi, dan menyimpan format gambar citra. |
| **Frontend UI** | HTML5, CSS3, JavaScript | Antarmuka interaktif responsif dengan visualisasi *real-time* dan otomatis membuka browser saat dijalankan. |

---

##  Fitur Utama Aplikasi

* **Dynamic K-Value Slider:** Mengatur jumlah komponen utama (*K*) secara *real-time* (1 s d. 250).
* **Live Analytics Dashboard:** Menampilkan info ruang penyimpanan dihemat (KB/%), waktu eksekusi matriks (ms), dan persentase perbedaan piksel secara instan.
* **Side-by-Side Visual Comparison:** Membandingkan gambar asli dan hasil rekonstruksi PCA secara langsung.
* **Direct Download:** Mengunduh hasil kompresi langsung dari halaman web setelah proses komputasi selesai.

---

## Struktur Direktori Proyek

```text
📂 pca-image-compressor/
│
├── 📂 templates/
│   └── 📄 index.html        # Antarmuka Frontend (HTML & CSS)
│
├── 📂 static/               # Tempat penyimpanan gambar sementara (Otomatis dibuat)
│
├── 📄 app.py                # Server Utama Backend Flask
├── 📄 pca_compressor.py     # Modul Logika Matematika PCA
└── 📄 README.md             # Dokumentasi Proyek
```

---

## Cara Menginstal dan Menjalankan

### 1. Clone Repositori
Buka terminal atau command prompt, lalu jalankan perintah berikut untuk mengkloning repositori:

```bash
git clone https://github.com/mfthlbibi/PBL.git
cd PBL
```

### 2. Instal Dependensi
Pastikan Anda sudah menginstal Python di perangkat Anda (disarankan versi 3.8 ke atas). Kemudian, instal beberapa library Python yang dibutuhkan dengan perintah:

```bash
pip install numpy Pillow flask
```

### 3. Jalankan Aplikasi
Eksekusi file utama app.py untuk memulai server lokal Flask:

```Bash
python app.py
```

 Catatan: Setelah perintah di atas dijalankan, aplikasi akan otomatis membuka browser bawaan Anda dan mengarah ke alamat http://127.0.0.1:5000/ dalam waktu sekitar 1.25 detik.

---

## Anggota Kelompok

* **Rasyid Yusuf Sugiyono** - `L0125028`
* **Gilang Ridho Wicaksana** - `L0125044`
* **Miftahul Habibi** - `L0125084`
