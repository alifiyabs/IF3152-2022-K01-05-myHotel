# Check Out
# Penanggung jawab: Theodore Justin Lionar 18220011

# Progress: Sudah berfungsi
# Prerequisite: install tkcalendar, tkinter, mariadb, pastikan semua library ada
# Prerequisite: database mariadb dengan nama myhotel sudah ada
# Notes: Replace ***** dengan password database

import sys
from tkinter import *
from tkinter import ttk, messagebox
from tkcalendar import Calendar
from datetime import date
import tkinter as tk
import datetime
import os
import mariadb
from tagihan import infotagihan

# Layar utama menu check out
def home(layar):
    global screen
    layar.destroy()
    screen = Tk()
    screen.title("myHotel")
    screen.geometry("1270x690")
    screen.config(bg = "white")
    
    global noKamar
    global nomorKamar_var
    noKamar = StringVar()

    # Judul halaman
    showTitle(screen)
    showSectionTitle(screen)

    # Entry box nomor kamar
    Label(screen, text = "Nomor Kamar", font = ("Helvetica", 15, "bold"), bg="white").place(x = 500, y = 220)
    nomorKamar_var = Entry(screen, textvariable = noKamar, font=("Helvetica", 15), bg = "light grey", fg = "black")
    nomorKamar_var.place(x = 500, y = 250, width = 300, height = 30)

    # Button next menuju verifikasi kamar
    Button(screen, text = "Berikutnya", font = ("Helvetica", 15, "bold"), bg="#71BC68", width = 10, height = 1, command = verifyKamar).place(x = 670, y = 320)

    screen.mainloop()

def verifyKamar():
    # Buka koneksi dengan database
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
        statement = "SELECT nomorKamar, statusKamar FROM informasiKamar WHERE nomorKamar = %s AND statusKamar = %s"
        data = (int(noKamar.get()), "Unavailable",)
        cur.execute(statement, data)
        row = cur.fetchone()
        if (row == None):
            kamarInvalid(screen)
        else:
            kamarValid(screen)
    except mariadb.Error as e:
        print(f"Error retrieving entry form database: {e}")
        databaseFail(screen)
    conn.commit()

# Jika kamar valid, input data
def kamarValid(screen):
    global screen1
    screen.destroy()
    screen1 = Tk()
    screen1.title("myHotel")
    screen1.geometry("1270x690")
    screen1.config(bg = "white")

    showTitle(screen1)
    showSectionTitle(screen1)

    def ulangiCheckOut():
        ulangi(screen1)

    global NIKPelanggan
    global NIKPelanggan_var
    global cal
    NIKPelanggan = StringVar()

    # Entry box NIK
    Label(screen1, text = "NIK Pelanggan", font = ("Helvetica", 15, "bold"), bg="white").place(x = 500, y = 220)
    NIKPelanggan_var = Entry(screen1, textvariable = NIKPelanggan, font=("Helvetica", 15), bg = "light grey", fg = "black")
    NIKPelanggan_var.place(x = 500, y = 250, width = 300, height = 30)

    # Entry box tanggal check out
    Label(screen1, text = "Tanggal Check Out", font = ("Helvetica", 15, "bold"), bg="white").place(x = 500, y = 320)
    cal = Calendar(screen1, selectmode = 'day', date_pattern = 'yyyy-mm-dd')
    cal.place(x = 500, y = 350, width = 300, height = 200)

    # Button next menuju ambil tanggal dan verifikasi data
    Button(screen1, text = "Berikutnya", font = ("Helvetica", 15, "bold"), bg="#71BC68", width = 10, height = 1, command = getDate).place(x = 670, y = 580)
    
    # Button back menuju halaman utama check out
    Button(screen1, text = "Kembali", font = ("Helvetica", 15, "bold"), bg="#F4AB6A", width = 10, height = 1, command = ulangiCheckOut).place(x = 500, y = 580)

    screen1.mainloop()

# Fungsi untuk mengambil tanggal dari date picker calendar dan lanjut ke verifikasi data
def getDate():
    global tanggalCheckOut

    tanggalCheckOut = cal.get_date()
    verifyData()

# Jika kamar tidak valid (tidak ada ataupun tidak sedang digunakan)
def kamarInvalid(screen):
    Label(screen, text = "Tidak dapat melakukan check out karena kamar tidak valid!", fg = "red", font = ("Helvetica, 13")).pack()

# Verifikasi data tamu dan kamar
def verifyData():
    global tanggalCheckOut_date

    # Koneksi dengan database
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
        databaseFail(screen1)
    
    # Execute query
    cur = conn.cursor()
    try:
        statement = "SELECT tanggalCheckIn, tanggalCheckOut, durasiMenginap FROM informasiTamuHotel WHERE NIK = %s AND nomorKamar = %s"
        data = (int(NIKPelanggan.get()), int(noKamar.get()),)
        cur.execute(statement, data)
        row = cur.fetchone()
        if (row == None):
            tamuInvalid(screen1)
        else: 
            # Ambil tanggal check out database
            statement = "SELECT tanggalCheckOut FROM informasiTamuHotel WHERE NIK = %s AND nomorKamar = %s"
            data = (int(NIKPelanggan.get()), int(noKamar.get()),)
            cur.execute(statement, data)
            row = cur.fetchone()
            for x in row:
                tanggalCheckOutVerify = x

            # Ambil tanggal check in database
            statement = "SELECT tanggalCheckIn FROM informasiTamuHotel WHERE NIK = %s AND nomorKamar = %s"
            data = (int(NIKPelanggan.get()), int(noKamar.get()),)
            cur.execute(statement, data)
            row = cur.fetchone()
            for x in row:
                tanggalCheckInVerify = x

            tanggalCheckOut_date = (datetime.datetime.strptime(tanggalCheckOut, '%Y-%m-%d')).date()

            # Cek apakah tanggal benar sesuai dengan database
            if (tanggalCheckOut_date == tanggalCheckOutVerify):
                validateCheckOut(screen1)
            else:
                if (tanggalCheckOut_date <= tanggalCheckInVerify):
                    waktuInvalid(screen1)
                elif (tanggalCheckOut_date > tanggalCheckOutVerify):
                    waktuInvalid(screen1)
                else:
                    waktuInvalid2(screen1)
    except mariadb.Error as e:
        print(f"Error retrieving entry form database: {e}")
        databaseFail(screen1)
    conn.commit()

# Validasi perlakuan check out
def validateCheckOut(screen1):
    global screen2
    screen1.destroy()
    screen2 = Tk()
    screen2.title("myHotel")
    screen2.geometry("1270x690")
    screen2.config(bg = "white")

    showTitle(screen2)
    showSectionTitle(screen2)
    
    def ulangiCheckOut():
        ulangi(screen2)
    
    def confirmationCheckOut():
        confirmCheckOut(screen2)

    # Cetak informasi kamar yang akan di-check out
    cetakValidateCheckOut()
    

    # Button next menuju konfirmasi check out
    Button(screen2, text = "Berikutnya", font = ("Helvetica", 15, "bold"), bg="#71BC68", width = 10, height = 1, command = confirmationCheckOut).place(x = 670, y = 580)
    
    # Button back menuju halaman utama check out
    Button(screen2, text = "Kembali", font = ("Helvetica", 15, "bold"), bg="#F4AB6A", width = 10, height = 1, command = ulangiCheckOut).place(x = 500, y = 580)

    screen2.mainloop()

# Cetak informasi kamar yang akan di-check out
def cetakValidateCheckOut():
    infotagihan(NIKPelanggan, noKamar, screen2)

# Mengonfirmasi perlakuan check out
def confirmCheckOut(screen2):
    global screen3
    screen2.destroy()
    screen3 = Tk()
    screen3.title("myHotel")
    screen3.geometry("1270x690")
    screen3.config(bg = "white")

    showTitle(screen3)
    showSectionTitle(screen3)

    def returntoValidateCheckOut():
        validateCheckOut(screen3)
    
    Label(screen3, text = "Lakukan check out?", font = ("Helvetica", 15, "bold"), bg="white").place(x = 550, y = 220)
    
    # Button ya untuk melakukan proses check out
    Button(screen3, text = "Ya", font = ("Helvetica", 15, "bold"), bg="#71BC68", width = 10, height = 1, command = processCheckOut).place(x = 670, y = 580)
    
    # Button tidak untuk kembali ke halaman validasi check out
    Button(screen3, text = "Tidak", font = ("Helvetica", 15, "bold"), bg="#F4AB6A", width = 10, height = 1, command = returntoValidateCheckOut).place(x = 500, y = 580)

    screen3.mainloop()

# Proses update database untuk melakukan check out
def processCheckOut():
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
        databaseFail(screen3)

    # Execute query
    cur = conn.cursor()
    try:
        # Update status pengunjung dari sedang check in menjadi sedang check out
        statement = "UPDATE informasiTamuHotel SET statusPengunjung = %s WHERE NIK = %s AND nomorKamar = %s"
        data = ("Check-out", int(NIKPelanggan.get()), int(noKamar.get()),)
        cur.execute(statement, data)

        # Update status kamar dari unavailable menjadi available
        cur = conn.cursor()
        statement = "UPDATE informasiKamar SET statusKamar = %s WHERE nomorKamar = %s"
        data = ("Available", int(noKamar.get()),)
        cur.execute(statement, data)

        # Ambil nilai tagihan tamu saat ini
        cur = conn.cursor()
        statement = "SELECT totalTagihan FROM informasiTamuHotel WHERE NIK = %s AND nomorKamar = %s"
        data = (int(NIKPelanggan.get()), int(noKamar.get()),)
        cur.execute(statement, data)
        row = cur.fetchone()
        for x in row:
            tagihan = x

        # Update riwayat kamar dari jumlah dipesan dan total pendapatan kamar berdasarkan tagihan tamu
        cur = conn.cursor()
        statement = "UPDATE riwayatKamar SET totalDipesan = (totalDipesan + %s), totalPendapatanKamar = (totalPendapatanKamar + %s) WHERE nomorKamar = %s"
        data = (1, tagihan, int(noKamar.get()),)
        cur.execute(statement, data)
    except mariadb.Error as e:
        print(f"Error updating or retrieving entry form database: {e}")
        databaseFail(screen3)

    conn.commit()
    successCheckOut(screen3)

# Menampilkan status sukses melakukan check out
def successCheckOut(screen3):
    global screen4
    screen3.destroy()
    screen4 = Tk()
    screen4.title("myHotel")
    screen4.geometry("1270x690")
    screen4.config(bg = "white")

    showTitle(screen4)
    showSectionTitle(screen4)

    def checkOutAgain():
        home(screen4)
    
    def finishCheckOut():
        screen4.destroy()

    Label(screen4, text = "Check out berhasil dilakukan!", font = ("Helvetica", 15, "bold"), bg="white").place(x = 510, y = 220)
    
    # Button selesai untuk keluar (nanti kembali ke main menu)
    Button(screen4, text = "Selesai", font = ("Helvetica", 15, "bold"), bg="#71BC68", width = 10, height = 1, command = finishCheckOut).place(x = 670, y = 580)
    
    # Button kembali untuk menuju ke halaman utama check out
    Button(screen4, text = "Kembali", font = ("Helvetica", 15, "bold"), bg="#F4AB6A", width = 10, height = 1, command = checkOutAgain).place(x = 500, y = 580)

    screen4.mainloop()

# Text tamu invalid karena identitas yang salah
def tamuInvalid(screen):
    Label(screen, text = "Tidak dapat melakukan check out karena identitas tamu tidak tepat!", fg = "red", font = ("Helvetica, 13")).pack()

# Text input waktu invalid karena tidak melakukan check out di waktu yang seharusnya
def waktuInvalid (screen):
    Label(screen, text = "Waktu check out invalid!", fg = "red", font = ("Helvetica, 13")).pack()

# Text input waktu invalid karena melakukan check out terlebih dahulu dibanding pesanan
def waktuInvalid2 (screen):
    Label(screen, text = "Belum waktunya check out!", fg = "red", font = ("Helvetica, 13")).pack()

# Menampilkan ulang halaman utama check out 
def ulangi (screen):
    home(screen)

# Tampilan saat koneksi atau operasi ke database gagal
def databaseFail(screen):
    global screen5
    screen.destroy()
    screen5 = Tk()
    screen5.title("myHotel")
    screen5.geometry("1270x690")
    screen5.config(bg = "white")   

    showTitle(screen5)
    showSectionTitle(screen5)

    def ulangiCheckOut():
        ulangi(screen5)

    Label(screen5, text = "Kegagalan Sistem!", font = ("Helvetica", 15, "bold"), bg="white").place(x = 555, y = 220)
    Button(screen5, text = "Kembali", font = ("Helvetica", 15, "bold"), bg="#F4AB6A", width = 10, height = 1, command = ulangiCheckOut).place(x = 500, y = 580)

    screen5.mainloop()

# Menampilkan judul aplikasi
def showTitle(screen):
    Label(screen, text = "myHotel", font = ("Helvetica", 20, "bold"), bg="white").place(x = 590, y = 100)

# Menampilkan judul section check out
def showSectionTitle(screen):
    Label(screen, text = "Check-Out", font = ("Helvetica", 10, "bold"), bg="white").place(x = 610, y = 140)