import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. KONEKSI KE DATABASE MYSQL XAMPP
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="db_spotify_baru"
    )
    print("⚡ Koneksi database berhasil untuk pembuatan grafik!")
except mysql.connector.Error as err:
    print(f"❌ Gagal konek database: {err}")
    exit()

# 2. TARIK DATA MENGGUNAKAN CURSOR (Bebas dari UserWarning Pandas)
cursor = conn.cursor()

# Query A: Top 5 Lagu
query_lagu = """
SELECT track_name, streams FROM tabel_lagu 
ORDER BY streams DESC LIMIT 5;
"""
cursor.execute(query_lagu)
data_lagu = cursor.fetchall()
columns_lagu = [desc[0] for desc in cursor.description]
df_lagu = pd.DataFrame(data_lagu, columns=columns_lagu)

# Query B: Distribusi Mode (Major vs Minor)
query_mode = """
SELECT mode, COUNT(*) as jumlah FROM tabel_lagu 
GROUP BY mode;
"""
cursor.execute(query_mode)
data_mode = cursor.fetchall()
columns_mode = [desc[0] for desc in cursor.description]
df_mode = pd.DataFrame(data_mode, columns=columns_mode)

# Tutup cursor dan koneksi database
cursor.close()
conn.close()


# 3. ATUR TEMA LUXURY DARK MODE (Hitam & Emas/Kuning)
plt.style.use('dark_background')
plt.rcParams['figure.facecolor'] = '#111111'
plt.rcParams['axes.facecolor'] = '#111111'

# Membuat kanvas berukuran besar yang muat 2 grafik bersebelahan
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# PERBAIKAN: Mengganti pad=20 menjadi y=0.98 agar kompatibel dengan Matplotlib terbaru
fig.suptitle('SPOTIFY GLOBAL HITS DATA ANALYSIS', fontsize=18, fontweight='bold', color='#FFD700', y=0.98)


# DIAGRAM 1: BAR CHART (TOP 5 LAGU TERPOPULER)
# Mengonversi streams ke tipe data float dan jadikan satuan Miliar
df_lagu['streams'] = df_lagu['streams'].astype(float)
df_lagu['streams_miliar'] = df_lagu['streams'] / 1_000_000_000

sns.barplot(
    x='streams_miliar', 
    y='track_name', 
    data=df_lagu, 
    ax=ax1, 
    palette=['#FFD700', '#FFCC00', '#FFAA00', '#FF8800', '#FF6600'] # Gradasi emas
)
ax1.set_title('Top 5 Lagu Paling Banyak Diputar di Dunia', fontsize=13, fontweight='bold', color='#FFFFFF', pad=10)
ax1.set_xlabel('Total Streams (Dalam Miliar)', fontsize=11, color='#BBBBBB')
ax1.set_ylabel('Judul Lagu', fontsize=11, color='#BBBBBB')
ax1.grid(axis='x', linestyle='--', alpha=0.3, color='#555555')


# DIAGRAM 2: PIE CHART (PERSENTASE MAJOR VS MINOR)
warna_pie = ['#FFD700', '#444444'] # Emas untuk Major, Abu Gelap untuk Minor
ax2.pie(
    df_mode['jumlah'], 
    labels=df_mode['mode'], 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=warna_pie,
    textprops={'fontsize': 12, 'fontweight': 'bold', 'color': '#FFFFFF'},
    wedgeprops={'edgecolor': '#111111', 'linewidth': 2}
)
ax2.set_title('Proporsi Tangga Nada: Major vs Minor', fontsize=13, fontweight='bold', color='#FFFFFF', pad=10)


# 4. SIMPAN HASIL GRAFIK MENJADI GAMBAR PNG
plt.tight_layout()
output_image = 'spotify_insights_chart.png'
plt.savefig(output_image, dpi=300, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close()

print(f"🎉 SUKSES! Grafik mewah berhasil dibuat dan disimpan dengan nama: '{output_image}'")