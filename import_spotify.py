import pandas as pd
import mysql.connector

try:
    
    nama_file = 'Spotify Most Streamed Songs.csv'
    df = pd.read_csv(nama_file, encoding='utf-8')
    print(f"📄 Berhasil membaca file CSV. Menemukan {len(df)} baris data.")

    
    df.columns = df.columns.str.strip()

    
    df['streams'] = pd.to_numeric(df['streams'], errors='coerce')

    
    db = mysql.connector.connect(
        host="localhost",
        user="root",       
        password="",       
        database="db_spotify_baru" 
    )
    cursor = db.cursor()
    print("🔌 Berhasil terhubung ke database `db_spotify_baru`.")

    print("🚀 Sedang memasukkan data ke tabel `tabel_lagu`, harap tunggu...")

    
    for index, row in df.iterrows():
        query = """
        INSERT INTO tabel_lagu (
            track_name, artist_name, artist_count, released_year, 
            released_month, released_day, in_spotify_playlists, 
            in_spotify_charts, streams, in_apple_playlists, in_apple_charts, 
            bpm, musical_key, mode
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        
        streams_val = int(row['streams']) if pd.notnull(row['streams']) else 0

        val = (
            str(row['track_name']), 
            str(row['artist(s)_name']), 
            int(row['artist_count']), 
            int(row['released_year']),
            int(row['released_month']), 
            int(row['released_day']), 
            int(row['in_spotify_playlists']),
            int(row['in_spotify_charts']), 
            streams_val, 
            int(row['in_apple_playlists']), 
            int(row['in_apple_charts']),
            int(row['bpm']), 
            str(row['key']) if pd.notnull(row['key']) else None, 
            str(row['mode'])
        )
        
        cursor.execute(query, val)

    
    db.commit()
    print(f"🎉 SUKSES! {len(df)} data lagu Spotify telah tersimpan sempurna di database baru!")

except mysql.connector.Error as err:
    print(f"❌ Terjadi kesalahan pada database: {err}")
except FileNotFoundError:
    print(f"❌ File '{nama_file}' tidak ditemukan.")
except Exception as e:
    print(f"❌ Terjadi error: {e}")

finally:
    if 'db' in locals() and db.is_connected():
        cursor.close()
        db.close()
        print("🔒 Koneksi database ditutup dengan aman.")