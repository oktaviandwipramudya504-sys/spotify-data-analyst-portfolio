# Spotify Most Streamed Songs Analysis 🎵📊

Repository ini berisi proyek analisis data Spotify menggunakan **Python** untuk proses ETL (Extract, Transform, Load) dan **MySQL/SQL** untuk pembersihan data ganda serta penarikan insight bisnis global.

---

## 🛠️ Tech Stack & Tools Used
* **Language:** Python 3.x
* **Libraries:** Pandas, MySQL Connector
* **Database:** MySQL (XAMPP / phpMyAdmin)
* **Dataset:** Spotify Most Streamed Songs (953 rows)
* **Code Editor:** Sublime Text & VS Code

---

## 📁 Struktur Proyek
* `import_spotify.py` : Script Python untuk membaca file CSV, membersihkan tipe data kolom, dan melakukan migrasi data secara otomatis ke database MySQL.
* `query_analisis.sql` : Kumpulan query SQL untuk analisis data terpopuler, analisis karakteristik lagu (BPM), dan segmentasi pasar.
* `grafik.py` : Script Python untuk membuat visualisasi data tren industri musik.
* `README.md` : Dokumentasi lengkap hasil analisis proyek.

---

## 🚀 Siklus Eksekusi Proyek (Pipeline)

### 1. Database Setup
Membuat database bernama `db_spotify_baru` dan struktur tabel `tabel_lagu` di phpMyAdmin untuk menampung data mentah.

### 2. Data Ingestion (ETL via Python)
Menjalankan script Python untuk mengotomatisasi pemindahan data dari file CSV ke SQL. Script ini menangani konversi tipe data angka agar tidak terjadi eror saat proses *insert*.

### 3. Data Cleansing (SQL)
Mendeteksi dan menghapus data duplikat yang kembar di database menggunakan perintah pintar `DELETE INNER JOIN` berbasis ID unik:
```sql
DELETE t1 FROM tabel_lagu t1
INNER JOIN tabel_lagu t2 
WHERE t1.id > t2.id 
  AND t1.track_name = t2.track_name 
  AND t1.artist_name = t2.artist_name;
