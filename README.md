# FaceClean – Denoising Autoencoder for Face Images
FaceClean adalah aplikasi full‑stack yang melakukan pembersihan noise (denoising) pada citra wajah menggunakan Convolutional Autoencoder di sisi backend, dan antarmuka web interaktif di sisi frontend.

## Fitur Utama
- Landing page modern dengan penjelasan singkat sistem dan tombol Start.
- Halaman denoising:
  - Upload / drag & drop gambar wajah (JPG, JPEG, PNG).
  - Proses denoising melalui endpoint `/api/denoise`.
  - Tampilkan perbandingan Input (Noisy) dan Output (Denoised).
  - Tombol download hasil denoising.
- Arsitektur terpisah:
  - `backend/` untuk API model autoencoder.
  - `frontend/` untuk UI (Next.js App Router).

## Menjalankan Backend
1. Masuk ke folder backend
2. pip install -r requirements.txt
3. python app.py


## Menjalankan Frontend
1. Di terminal baru, masuk ke folder `frontend`
2. Install dependency
3. Jalankan development server: npm run dev
4. Buka browser
    - `/`          → Landing page FaceClean.
    - `/denoise`   → Halaman upload & denoising.

    Pastikan backend sudah berjalan agar endpoint `/api/denoise` bisa merespons dengan benar.

## Konfigurasi Endpoint API
Secara default, route frontend `/api/denoise` di `frontend/app/api/denoise/route.ts` meneruskan request ke backend Python. Jika port backend berbeda, sesuaikan URL di file tersebut.


## Cara Pakai Aplikasi
1. Buka `http://localhost:3000`.
2. Klik tombol **Start** untuk menuju halaman denoising.
3. Upload atau drag & drop gambar wajah ber‑noise (JPG/PNG).
4. Klik **Upload & Denoise**.
5. Tunggu proses selesai, lalu lihat perbandingan Input dan Output.
6. Klik **Download** untuk menyimpan hasil citra yang sudah dibersihkan.

## Lisensi & Kredit Aset
- Model dan kode mengikuti lisensi tugas/penelitian yang kamu gunakan.
- Ilustrasi 3D pada landing page diambil dari sumber bebas (Unsplash/IconScout/Icons8). Cantumkan kredit sesuai lisensi aset yang dipakai.

Link collab untuk Training:
https://colab.research.google.com/drive/1fI8DbDtjAGXTbbZHLj74x8eKDIAAf24H?usp=sharing


