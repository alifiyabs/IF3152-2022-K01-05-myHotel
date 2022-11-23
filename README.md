# IF3152-2022-K01-05-myHotel

## Penjelasan Singkat
Aplikasi 'myHotel' adalah aplikasi manajemen yang digunakan oleh hotel. Dengan fitur utamanya antara lain,
* Informasi Kamar
* Check-in
* Check-out
* Tagihan
* Riwayat Kamar
* Pemesanan Makanan

## Cara Menjalankan Aplikasi
```
- Buat database dengan nama "myHotel" dan dump "database_myHotel.sql"
- Buka directory "..."
- Jalankan start.py untuk menjalankan aplikasi
```
## Daftar Modul yang Diimplementasi
### Informasi Kamar
Nama Penanggung Jawab : Joe Putera

NIM : 18217035

### Check-in
Nama Penanggung Jawab : Alifiya Brizita Shari

NIM : 18220069

### Check-out
Nama Penanggung Jawab : Theodore Justin Lionar

NIM : 18220011

### Tagihan
Nama Penanggung Jawab : Rachita Caronica Jonur

NIM : 18220091

### Riwayat Kamar
Nama Penanggung Jawab : Kyla Aisha

NIM : 18220093

### Pemesanan Makanan
Nama Penanggung Jawab : Adwa Sofia

NIM : 18220109


## Daftar Tabel Basis Data
### informasikamar
+------------+-----------+-----------+-------------------------------------------+---------------+-------------+
| nomorKamar | tipeKamar | luasKamar | fasilitas                                 | hargaPerMalam | statusKamar |
+------------+-----------+-----------+-------------------------------------------+---------------+-------------+
|        101 | Single    |        37 | Satu bed single                           |        300000 | Available   |
|        102 | Single    |        37 | Satu bed single                           |        300000 | Booked      |
|        103 | Single    |        37 | Satu bed single                           |        300000 | Available   |
|        104 | Single    |        37 | Satu bed single                           |        300000 | Available   |
|        105 | Single    |        37 | Satu bed single                           |        300000 | Available   |
|        201 | Double    |        45 | Dua bed single, ada balkon                |        600000 | Available   |
|        202 | Double    |        45 | Dua bed single, ada balkon                |        600000 | Available   |
|        203 | Double    |        45 | Dua bed single, ada balkon                |        600000 | Booked      |
|        204 | Double    |        45 | Dua bed single, ada balkon                |        600000 | Available   |
|        205 | Double    |        45 | Dua bed single, ada balkon                |        600000 | Available   |
|        301 | Deluxe    |        53 | Satu bed king, ada balkon, ada ruang tamu |       1000000 | Unavailable |
|        302 | Deluxe    |        53 | Satu bed king, ada balkon, ada ruang tamu |       1000000 | Available   |
|        303 | Deluxe    |        53 | Satu bed king, ada balkon, ada ruang tamu |       1000000 | Available   |
|        304 | Deluxe    |        53 | Satu bed king, ada balkon, ada ruang tamu |       1000000 | Booked      |
|        305 | Deluxe    |        53 | Satu bed king, ada balkon, ada ruang tamu |       1000000 | Available   |
+------------+-----------+-----------+-------------------------------------------+---------------+-------------+


### informasitamuhotel
+------------------+-----------+------------+----------------+-----------------+-----------+-----------------+----------------+------------------+--------------+
| NIK              | idCheckIn | nomorKamar | tanggalCheckIn | tanggalCheckOut | tipeKamar | namaPengunjung  | durasiMenginap | statusPengunjung | totalTagihan |
+------------------+-----------+------------+----------------+-----------------+-----------+-----------------+----------------+------------------+--------------+
| 1234567890123450 |         1 |        101 | 2022-01-01     | 2022-01-02      | Single    | Kyla Aisha      |              1 | Check-out        |       300000 |
| 1234567890123451 |         2 |        102 | 2022-02-02     | 2022-02-03      | Single    | Alifiya Brizita |              1 | Check-out        |       300000 |
| 1234567890123452 |         3 |        103 | 2022-03-03     | 2022-03-04      | Single    | Adwa Sofia      |              1 | Check-out        |       300000 |
| 1234567890123453 |         4 |        104 | 2022-04-04     | 2022-04-05      | Single    | Rachita Caron   |              1 | Check-out        |       300000 |
| 1234567890123454 |         5 |        105 | 2022-05-05     | 2022-05-06      | Single    | Aisha Kyla      |              1 | Check-out        |       300000 |
| 1234567890123455 |         6 |        203 | 2022-06-06     | 2022-06-07      | Double    | Brizita Alifiya |              1 | Check-out        |       600000 |
| 1234567890123456 |         7 |        301 | 2022-07-07     | 2022-07-08      | Deluxe    | Sofia Adwa      |              1 | Check-out        |      1000000 |
| 1234567890123457 |         8 |        302 | 2022-08-08     | 2022-08-09      | Deluxe    | Caron Rachita   |              1 | Check-out        |      1000000 |
| 1234567890123458 |         9 |        304 | 2022-09-09     | 2022-09-10      | Deluxe    | Shaky Aila      |              1 | Check-out        |      1000000 |
| 1234567890123459 |        10 |        102 | 2022-11-20     | 2022-11-21      | Single    | Brifiya Azita   |              1 | Book             |       300000 |
| 1234567890123460 |        11 |        104 | 2022-11-15     | 2022-11-16      | Single    | Racaron Chita   |              1 | Check-out        |       300000 |
| 1234567890123461 |        12 |        203 | 2022-11-20     | 2022-11-21      | Double    | Afia Sodwa      |              1 | Book             |       600000 |
| 1234567890123462 |        13 |        301 | 2022-11-15     | 2022-11-16      | Deluxe    | Jeon Jungkook   |              1 | Check-in         |      1000000 |
| 1234567890123463 |        14 |        304 | 2022-11-20     | 2022-11-21      | Deluxe    | Kim Jennie      |              1 | Book             |      1000000 |
+------------------+-----------+------------+----------------+-----------------+-----------+-----------------+----------------+------------------+--------------+


### riwayatkamar
+------------+--------------+----------------------+
| nomorKamar | totalDipesan | totalPendapatanKamar |
+------------+--------------+----------------------+
|        101 |            1 |               300000 |
|        102 |            1 |               300000 |
|        103 |            1 |               300000 |
|        104 |            2 |               600000 |
|        105 |            1 |               300000 |
|        201 |            0 |                    0 |
|        202 |            0 |                    0 |
|        203 |            1 |               600000 |
|        204 |            0 |                    0 |
|        205 |            0 |                    0 |
|        301 |            1 |              1000000 |
|        302 |            1 |              1000000 |
|        303 |            0 |                    0 |
|        304 |            1 |              1000000 |
|        305 |            0 |                    0 |
+------------+--------------+----------------------+
