-- =========================================================
-- PROYEK ANALISIS DATA SPOTIFY - OKTAV PRAMUDYA
-- =========================================================


DELETE t1 FROM tabel_lagu t1
INNER JOIN tabel_lagu t2 
WHERE t1.id > t2.id 
  AND t1.track_name = t2.track_name 
  AND t1.artist_name = t2.artist_name;


SELECT track_name, artist_name, streams 
FROM tabel_lagu 
ORDER BY streams DESC 
LIMIT 5;


SELECT artist_name, COUNT(*) as total_lagu 
FROM tabel_lagu 
GROUP BY artist_name 
ORDER BY total_lagu DESC 
LIMIT 5;


SELECT mode, COUNT(*) as jumlah_lagu 
FROM tabel_lagu 
GROUP BY mode;


SELECT AVG(bpm) as rata_rata_bpm, MIN(bpm) as bpm_terlambat, MAX(bpm) as bpm_tercepat 
FROM tabel_lagu;