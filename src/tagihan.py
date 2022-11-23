# Tagihan
# Penanggung jawab: Rachita Caronica Jonur 18220091

# Progress: Sudah berfungsi
# Prerequisite: Install tkinter dan mariadb (beserta seluruh library yang diperlukan)
# Prerequisite: Database mariadb dengan nama myhotel sudah ada
# Notes: Replace password database, serta ganti port database jika diperlukan

import sys 
import mariadb
import tkinter as tk
from checkOut import *

class Tagihan():
    def __init__(self, noKamar, NIKPelanggan):
        self.noKamar = noKamar
        self.NIKPelanggan = NIKPelanggan

    def infotagihan(self, screen):
        # Koneksi ke database
        try:
            conn = mariadb.connect (
                user = 'root',
                password = '',
                host = 'localhost',
                port = 3306,
                database = 'myhotel'
            )
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            databaseFail(screen)

        # Execute query
        cur = conn.cursor()
        try:
            # Mengambil informasi kamar tamu yang diperlukan
            statement = "SELECT nomorKamar, namaPengunjung, NIK, tanggalCheckIn, tanggalCheckOut, totalTagihan FROM informasiTamuHotel WHERE NIK = %s AND nomorKamar = %s"
            data = (int(self.NIKPelanggan.get()), int(self.noKamar.get()),)
            cur.execute(statement, data)
            
            for data_tamu in cur:
                nomorKamarVal = data_tamu[0]
                namaPengunjungVal = data_tamu[1]
                NIKVal = data_tamu[2]
                tanggalCheckInVal = data_tamu[3]
                tanggalCheckOutVal = data_tamu[4]
                totalTagihanVal = data_tamu[5]

            lf = tk.LabelFrame(screen, bg='white', padx=5, pady=10)
            # lf.grid(row=0, column=0, padx=0, pady=35, sticky=CENTER)
            lf.place(anchor="c", relx=.5, rely=.5)
            
            Label(lf, text= "Nomor Kamar", font = ("Helvetica", 13), bg= 'white').grid(row=0, column=0, padx=20, pady=5, sticky='W')
            Label(lf, text= "Nama Tamu", font = ("Helvetica", 13), bg= 'white').grid(row=1, column=0, padx=20, pady=5, sticky='W')
            Label(lf, text= "NIK Tamu", font = ("Helvetica", 13), bg= 'white').grid(row=2, column=0, padx=20, pady=5, sticky='W')
            Label(lf, text= "Tanggal Check In", font = ("Helvetica", 13), bg= 'white').grid(row=3, column=0, padx=20, pady=5, sticky='W')
            Label(lf, text= "Tanggal Check Out", font = ("Helvetica", 13), bg= 'white').grid(row=4, column=0, padx=20, pady=5, sticky='W')
            Label(lf, text= "Total Tagihan", font = ("Helvetica", 13), bg= 'white').grid(row=5, column=0, padx=20, pady=5, sticky='W')

            Label(lf, text=nomorKamarVal, font = ("Helvetica", 13), bg= 'white').grid(row=0, column=1, padx=20, pady=5, sticky='E')
            Label(lf, text=namaPengunjungVal, font = ("Helvetica", 13), bg= 'white').grid(row=1, column=1, padx=20, pady=5, sticky='E')
            Label(lf, text=NIKVal, font = ("Helvetica", 13), bg= 'white').grid(row=2, column=1, padx=20, pady=5, sticky='E')
            Label(lf, text=tanggalCheckInVal, font = ("Helvetica", 13), bg= 'white').grid(row=3, column=1, padx=20, pady=5, sticky='E')
            Label(lf, text=tanggalCheckOutVal, font = ("Helvetica", 13), bg= 'white').grid(row=4, column=1, padx=20, pady=5, sticky='E')
            Label(lf, text=totalTagihanVal, font = ("Helvetica", 13), bg= 'white').grid(row=5, column=1, padx=20, pady=5, sticky='E')

        except mariadb.Error as e:
            print(f"Error retrieving entry form database: {e}")
            databaseFail(screen)

        conn.commit()