CREATE TABLE informasiKamar (
  nomorKamar INT PRIMARY KEY,
  tipeKamar VARCHAR(50) NOT NULL,
  luasKamar INT NOT NULL,
  fasilitas VARCHAR(1000) NOT NULL,
  hargaPerMalam INT NOT NULL,
  statusKamar VARCHAR(50) NOT NULL,
  check (statusKamar in ('Available', 'Unavailable', 'Booked'))
);

INSERT INTO informasiKamar(nomorKamar,tipeKamar,luasKamar,fasilitas,hargaPerMalam,statusKamar) VALUES (101,'Single',37,'Satu bed single',300000,'Available');
INSERT INTO informasiKamar(nomorKamar,tipeKamar,luasKamar,fasilitas,hargaPerMalam,statusKamar) VALUES (102,'Single',37,'Satu bed single',300000,'Booked');
INSERT INTO informasiKamar(nomorKamar,tipeKamar,luasKamar,fasilitas,hargaPerMalam,statusKamar) VALUES (103,'Single',37,'Satu bed single',300000,'Available');
INSERT INTO informasiKamar(nomorKamar,tipeKamar,luasKamar,fasilitas,hargaPerMalam,statusKamar) VALUES (104,'Single',37,'Satu bed single',300000,'Unavailable');
INSERT INTO informasiKamar(nomorKamar,tipeKamar,luasKamar,fasilitas,hargaPerMalam,statusKamar) VALUES (105,'Single',37,'Satu bed single',300000,'Available');
INSERT INTO informasiKamar(nomorKamar,tipeKamar,luasKamar,fasilitas,hargaPerMalam,statusKamar) VALUES (201,'Double',45,'Dua bed single, ada balkon',600000,'Available');
INSERT INTO informasiKamar(nomorKamar,tipeKamar,luasKamar,fasilitas,hargaPerMalam,statusKamar) VALUES (202,'Double',45,'Dua bed single, ada balkon',600000,'Available');
INSERT INTO informasiKamar(nomorKamar,tipeKamar,luasKamar,fasilitas,hargaPerMalam,statusKamar) VALUES (203,'Double',45,'Dua bed single, ada balkon',600000,'Booked');
INSERT INTO informasiKamar(nomorKamar,tipeKamar,luasKamar,fasilitas,hargaPerMalam,statusKamar) VALUES (204,'Double',45,'Dua bed single, ada balkon',600000,'Available');
INSERT INTO informasiKamar(nomorKamar,tipeKamar,luasKamar,fasilitas,hargaPerMalam,statusKamar) VALUES (205,'Double',45,'Dua bed single, ada balkon',600000,'Available');
INSERT INTO informasiKamar(nomorKamar,tipeKamar,luasKamar,fasilitas,hargaPerMalam,statusKamar) VALUES (301,'Deluxe',53,'Satu bed king, ada balkon, ada ruang tamu',1000000,'Unavailable');
INSERT INTO informasiKamar(nomorKamar,tipeKamar,luasKamar,fasilitas,hargaPerMalam,statusKamar) VALUES (302,'Deluxe',53,'Satu bed king, ada balkon, ada ruang tamu',1000000,'Available');
INSERT INTO informasiKamar(nomorKamar,tipeKamar,luasKamar,fasilitas,hargaPerMalam,statusKamar) VALUES (303,'Deluxe',53,'Satu bed king, ada balkon, ada ruang tamu',1000000,'Available');
INSERT INTO informasiKamar(nomorKamar,tipeKamar,luasKamar,fasilitas,hargaPerMalam,statusKamar) VALUES (304,'Deluxe',53,'Satu bed king, ada balkon, ada ruang tamu',1000000,'Booked');
INSERT INTO informasiKamar(nomorKamar,tipeKamar,luasKamar,fasilitas,hargaPerMalam,statusKamar) VALUES (305,'Deluxe',53,'Satu bed king, ada balkon, ada ruang tamu',1000000,'Available');

SELECT * FROM informasiKamar;

CREATE TABLE riwayatKamar (
  nomorKamar INT PRIMARY KEY,
  totalDipesan INT NOT NULL,
  totalPendapatanKamar INT NOT NULL,
  FOREIGN KEY (nomorKamar) REFERENCES informasiKamar(nomorKamar)
);

INSERT INTO riwayatKamar(nomorKamar,totalDipesan,totalPendapatanKamar) VALUES (101,1,300000);
INSERT INTO riwayatKamar(nomorKamar,totalDipesan,totalPendapatanKamar) VALUES (102,1,300000);
INSERT INTO riwayatKamar(nomorKamar,totalDipesan,totalPendapatanKamar) VALUES (103,1,300000);
INSERT INTO riwayatKamar(nomorKamar,totalDipesan,totalPendapatanKamar) VALUES (104,1,300000);
INSERT INTO riwayatKamar(nomorKamar,totalDipesan,totalPendapatanKamar) VALUES (105,1,300000);
INSERT INTO riwayatKamar(nomorKamar,totalDipesan,totalPendapatanKamar) VALUES (201,0,0);
INSERT INTO riwayatKamar(nomorKamar,totalDipesan,totalPendapatanKamar) VALUES (202,0,0);
INSERT INTO riwayatKamar(nomorKamar,totalDipesan,totalPendapatanKamar) VALUES (203,1,600000);
INSERT INTO riwayatKamar(nomorKamar,totalDipesan,totalPendapatanKamar) VALUES (204,0,0);
INSERT INTO riwayatKamar(nomorKamar,totalDipesan,totalPendapatanKamar) VALUES (205,0,0);
INSERT INTO riwayatKamar(nomorKamar,totalDipesan,totalPendapatanKamar) VALUES (301,1,1000000);
INSERT INTO riwayatKamar(nomorKamar,totalDipesan,totalPendapatanKamar) VALUES (302,1,1000000);
INSERT INTO riwayatKamar(nomorKamar,totalDipesan,totalPendapatanKamar) VALUES (303,0,0);
INSERT INTO riwayatKamar(nomorKamar,totalDipesan,totalPendapatanKamar) VALUES (304,1,1000000);
INSERT INTO riwayatKamar(nomorKamar,totalDipesan,totalPendapatanKamar) VALUES (305,0,0);

SELECT * FROM riwayatKamar;

CREATE TABLE informasiTamuHotel (
  NIK BIGINT UNIQUE NOT NULL,
  idCheckIn SERIAL NOT NULL,
  nomorKamar INT NOT NULL,
  tanggalCheckIn DATE NOT NULL,
  tanggalCheckOut DATE NOT NULL,
  tipeKamar VARCHAR(50) NOT NULL,
  namaPengunjung VARCHAR(50) NOT NULL,
  durasiMenginap INT NOT NULL,
  statusPengunjung VARCHAR(50) NOT NULL,
  totalTagihan INT NOT NULL,
  check (statusPengunjung in ('Check-in', 'Check-out', 'Book')),
  FOREIGN KEY (nomorKamar) REFERENCES informasiKamar(nomorKamar),
  PRIMARY KEY (NIK, nomorKamar, tanggalCheckIn)
);

INSERT INTO informasiTamuHotel(NIK,idCheckIn,nomorKamar,tanggalCheckIn,tanggalCheckOut,tipeKamar,namaPengunjung,durasiMenginap,statusPengunjung,totalTagihan) VALUES ('1234567890123450',DEFAULT,101,'2022-01-01','2022-01-02','Single','Kyla Aisha',1,'Check-out',300000);
INSERT INTO informasiTamuHotel(NIK,idCheckIn,nomorKamar,tanggalCheckIn,tanggalCheckOut,tipeKamar,namaPengunjung,durasiMenginap,statusPengunjung,totalTagihan) VALUES ('1234567890123451',DEFAULT,102,'2022-02-02','2022-02-03','Single','Alifiya Brizita',1,'Check-out',300000);
INSERT INTO informasiTamuHotel(NIK,idCheckIn,nomorKamar,tanggalCheckIn,tanggalCheckOut,tipeKamar,namaPengunjung,durasiMenginap,statusPengunjung,totalTagihan) VALUES ('1234567890123452',DEFAULT,103,'2022-03-03','2022-03-04','Single','Adwa Sofia',1,'Check-out',300000);
INSERT INTO informasiTamuHotel(NIK,idCheckIn,nomorKamar,tanggalCheckIn,tanggalCheckOut,tipeKamar,namaPengunjung,durasiMenginap,statusPengunjung,totalTagihan) VALUES ('1234567890123453',DEFAULT,104,'2022-04-04','2022-04-05','Single','Rachita Caron',1,'Check-out',300000);
INSERT INTO informasiTamuHotel(NIK,idCheckIn,nomorKamar,tanggalCheckIn,tanggalCheckOut,tipeKamar,namaPengunjung,durasiMenginap,statusPengunjung,totalTagihan) VALUES ('1234567890123454',DEFAULT,105,'2022-05-05','2022-05-06','Single','Aisha Kyla',1,'Check-out',300000);
INSERT INTO informasiTamuHotel(NIK,idCheckIn,nomorKamar,tanggalCheckIn,tanggalCheckOut,tipeKamar,namaPengunjung,durasiMenginap,statusPengunjung,totalTagihan) VALUES ('1234567890123455',DEFAULT,203,'2022-06-06','2022-06-07','Double','Brizita Alifiya',1,'Check-out',600000);
INSERT INTO informasiTamuHotel(NIK,idCheckIn,nomorKamar,tanggalCheckIn,tanggalCheckOut,tipeKamar,namaPengunjung,durasiMenginap,statusPengunjung,totalTagihan) VALUES ('1234567890123456',DEFAULT,301,'2022-07-07','2022-07-08','Deluxe','Sofia Adwa',1,'Check-out',1000000);
INSERT INTO informasiTamuHotel(NIK,idCheckIn,nomorKamar,tanggalCheckIn,tanggalCheckOut,tipeKamar,namaPengunjung,durasiMenginap,statusPengunjung,totalTagihan) VALUES ('1234567890123457',DEFAULT,302,'2022-08-08','2022-08-09','Deluxe','Caron Rachita',1,'Check-out',1000000);
INSERT INTO informasiTamuHotel(NIK,idCheckIn,nomorKamar,tanggalCheckIn,tanggalCheckOut,tipeKamar,namaPengunjung,durasiMenginap,statusPengunjung,totalTagihan) VALUES ('1234567890123458',DEFAULT,304,'2022-09-09','2022-09-10','Deluxe','Shaky Aila',1,'Check-out',1000000);
INSERT INTO informasiTamuHotel(NIK,idCheckIn,nomorKamar,tanggalCheckIn,tanggalCheckOut,tipeKamar,namaPengunjung,durasiMenginap,statusPengunjung,totalTagihan) VALUES ('1234567890123459',DEFAULT,102,'2022-11-20','2022-11-21','Single','Brifiya Azita',1,'Book',300000);
INSERT INTO informasiTamuHotel(NIK,idCheckIn,nomorKamar,tanggalCheckIn,tanggalCheckOut,tipeKamar,namaPengunjung,durasiMenginap,statusPengunjung,totalTagihan) VALUES ('1234567890123460',DEFAULT,104,'2022-11-15','2022-11-16','Single','Racaron Chita',1,'Check-in',300000);
INSERT INTO informasiTamuHotel(NIK,idCheckIn,nomorKamar,tanggalCheckIn,tanggalCheckOut,tipeKamar,namaPengunjung,durasiMenginap,statusPengunjung,totalTagihan) VALUES ('1234567890123461',DEFAULT,203,'2022-11-20','2022-11-21','Double','Afia Sodwa',1,'Book',600000);
INSERT INTO informasiTamuHotel(NIK,idCheckIn,nomorKamar,tanggalCheckIn,tanggalCheckOut,tipeKamar,namaPengunjung,durasiMenginap,statusPengunjung,totalTagihan) VALUES ('1234567890123462',DEFAULT,301,'2022-11-15','2022-11-16','Deluxe','Jeon Jungkook',1,'Check-in',1000000);
INSERT INTO informasiTamuHotel(NIK,idCheckIn,nomorKamar,tanggalCheckIn,tanggalCheckOut,tipeKamar,namaPengunjung,durasiMenginap,statusPengunjung,totalTagihan) VALUES ('1234567890123463',DEFAULT,304,'2022-11-20','2022-11-21','Deluxe','Kim Jennie',1,'Book',1000000);

SELECT * FROM informasiTamuHotel;
