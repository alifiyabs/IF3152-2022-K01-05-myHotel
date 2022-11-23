# Check In
# Nama Penanggung Jawab : Alifiya Brizita Shary
# Melakukan Check In pada Hotel, yaitu Booking Check In dan Check In Walk In

import sys
import datetime
# import mysql.connector
import tkinter as tk
import datetime
import os
from tkcalendar import Calendar
from tkinter import *
from tkinter import ttk, messagebox
from datetime import date


def homeCheckIn(halaman):
    global window
    halaman.destroy()
    window = Tk()
    window.title("myHotel")
    window.geometry("1270x690")
    window.config(bg="white")
    
    # Tampilan Judul myHotel dan Judul Check In
    showTitle(window)
    showTitleCheckIn(window)

    # Buka halaman Booking Check In
    def bukaBookingCheckIn():
        BookingCheckIn(window)
    # Buka halaman Booking Walk In
    def bukaWalkIn():
        checkInWalkIn(window)

    # Button bookingCheckIn menuju ke bookingCheckIn
    Button(window, text = "Booking Check In", font = ("Helvetica", 15, "bold"), bg="#71BC68", width = 20, height = 2, command = bukaBookingCheckIn).place(x = 450, y = 300)
    # Button checkInWalkIn menuju ke checkInWalkIn
    Button(window, text = "Check In Walk In", font = ("Helvetica", 15, "bold"), bg="#71BC68", width = 20, height = 2, command = bukaWalkIn).place(x = 750, y = 300)
    # Button kembali ke menu utama
    Button(window, text = "Kembali ke menu utama", font = ("Helvetica", 10, "bold"), bg="red", width = 10, height = 1, command = backToHomescreen).place(x = 99, y = 113, width=180, height=49)
   
    window.mainloop()

def BookingCheckIn(window):
    global screenBooking
    window.destroy()
    screenBooking = Tk()
    screenBooking.title("myHotel")
    screenBooking.geometry("1270x690")
    screenBooking.config(bg="white")

    global nikPelangganBook
    global noKamarBook
    global nikPelangganBook_var
    global noKamarBook_var
    nikPelangganBook = StringVar()
    noKamarBook = StringVar()

    # Kembali ke halaman utama Check In
    def backToHomeCheckIn():
        homeCheckIn(screenBooking)

    # Title
    (screenBooking)
    # Sectione Title
    Label(screenBooking, text = "Booking Check-In", font = ("Helvetica", 10, "bold"), bg="white").place(x = 610, y = 140)

    # Entry box NIK Pelanggan
    Label(screenBooking, text = "NIK Pelanggan", font = ("Helvetica", 15, "bold"), bg="white").place(x = 500, y = 220)
    nikPelangganBook_var = Entry(screenBooking, textvariable= nikPelangganBook,font=("Helvetica", 15), bg = "light grey", fg = "black")
    nikPelangganBook_var.place(x = 500, y = 250, width = 300, height = 30)

    # Entry box Nomor Kamar 
    Label(screenBooking, text = "Nomor Kamar ", font = ("Helvetica", 15, "bold"), bg="white").place(x = 500, y = 320)
    noKamarBook_var= Entry(screenBooking, textvariable= noKamarBook,font=("Helvetica", 15), bg = "light grey", fg = "black")
    noKamarBook_var.place(x = 500, y = 350, width = 300, height = 30)

    # Button next menuju cek ketersediaan kamar 
    Button(screenBooking, text = "Cek Kamar" ,font = ("Helvetica", 15, "bold"), bg="#71BC68", width = 10, height = 1, command = " ").place(x = 670, y = 580)
    # Button kembali ke menu utama Check In
    Button(screenBooking, text = "Kembali ke menu Check In", font = ("Helvetica", 10, "bold"), bg="red", width = 10, height = 1, command = backToHomeCheckIn).place(x = 99, y = 113, width=180, height=49)
   
    verifikasiBookingCheckIn()
    
    screenBooking.mainloop()

def checkInWalkIn(window):
    global screenWalkIn
    window.destroy()
    screenWalkIn = Tk()
    screenWalkIn.title("myHotel")
    screenWalkIn.geometry("1270x690")
    screenWalkIn.config(bg="white")

    global noKamarWalkIn
    global noKamarWalkIn_var
    noKamarWalkIn = StringVar()

    # Buka halaman isi data pengunjung
    def bukaIsiDataPengunjung():
        isiDataPengunjung(screenWalkIn)
    
    # Kembali ke halaman utama Check In
    def backToHomeCheckIn():
        homeCheckIn(screenWalkIn)

    # Entry nomor kamar
    showTitle(screenWalkIn)
    Label(screenWalkIn, text = "Check-In Walk In", font = ("Helvetica", 10, "bold"), bg="white").place(x = 610, y = 140)

    Label(screenWalkIn, text = "Nomor Kamar", font = ("Helvetica", 15, "bold"), bg="white").place(x = 500, y = 220)
    noKamarWalkIn_var = Entry(screenWalkIn, textvariable = noKamarWalkIn, font=("Helvetica", 15), bg = "light grey", fg = "black")
    noKamarWalkIn_var.place(x = 500, y = 250, width = 300, height = 30)

    # Button Cek ketersediaan kamar
    Button(screenWalkIn, text = "Cek Kamar" ,font = ("Helvetica", 15, "bold"), bg="#71BC68", width = 10, height = 1, command =  bukaIsiDataPengunjung).place(x = 670, y = 580)
    # Button kembali ke menu utama Check In
    Button(screenWalkIn, text = "Kembali ke menu Check In", font = ("Helvetica", 10, "bold"), bg="red", width = 10, height = 1, command = backToHomeCheckIn).place(x = 99, y = 113, width=180, height=49)
   
    verifikasiCheckInWalkIn()

    screenWalkIn.mainloop()

def verifikasiBookingCheckIn():
    # Buka koneksi dengan database mysql

    try:
        conn = mysql.connector.connect (
            user = 'root',
            password = 'Bel2022Fiy@',
            host = 'localhost',
            database = 'myHotel'
        )
    except mysql.connector.Error as e:
        print(f"Error connecting to Mysql Platform: {e}")
        sys.exit(1)
    
    # Execute Query
    cur = conn.cursor()
    try:
        statement = "SELECT NIK, nomorKamar, statusPengunjung FROM informasiTamuHotel WHERE NIK = %s AND nomorKamar = %s AND statusPengunjung = %s"
        data = (int(nikPelangganBook.get()), int(noKamarBook.get()), "Book",)
        cur.execute(statement, data)
    except mysql.connector.Error as e:
        print(f"Error retrieving entry form database: {e}")

def verifikasiCheckInWalkIn():
    
    # Buka koneksi dengan database mysql

    try:
        conn = mysql.connector.connect (
            user = 'root',
            password = 'Bel2022Fiy@',
            host = 'localhost',
            database = 'myHotel'
        )
    except mysql.connector.Error as e:
        print(f"Error connecting to Mysql Platform: {e}")
        sys.exit(1)
    
    # Execute Query
    cur = conn.cursor()
    try:
        statement = "SELECT nomorKamar FROM informasiKamar WHERE nomorKamar = %s AND statusKamar = %s"
        data = (int(noKamarWalkIn_var.get()), "Available",)
        cur.execute(statement, data)
    except mysql.connector.Error as e:
        print(f"Error retrieving entry form database: {e}")

def isiDataPengunjung(screenWalkIn):
    global screenFillData
    screenWalkIn.destroy()
    screenFillData = Tk()
    screenFillData.title("myHotel")
    screenFillData.geometry("1270x690")
    screenFillData.config(bg = "white")

    showTitle(screenFillData)
    Label(screenFillData, text = "Isi data pengunjung", font = ("Helvetica", 10, "bold"), bg="white").place(x = 610, y = 140)

    global nikPelangganFill
    global NIKPelangganFill_var
    global namaPengunjungFill
    global namaPengunjungFill_var
    global calendar
    nikPelangganFill = StringVar()
    namaPengunjungFill = StringVar()

    # Entry box NIK
    Label(screenFillData, text = "NIK Pelanggan", font = ("Helvetica", 15, "bold"), bg="white").place(x = 500, y = 220)
    nikPelangganFill_var = Entry(screenFillData, textvariable = nikPelangganFill, font=("Helvetica", 15), bg = "light grey", fg = "black")
    nikPelangganFill_var.place(x = 500, y = 250, width = 300, height = 30)

    # Entry box Nama Pelanggan
    Label(screenFillData, text = "Nama Pelanggan", font = ("Helvetica", 15, "bold"), bg="white").place(x = 500, y = 320)
    namaPengunjungFill_var = Entry(screenFillData, textvariable = nikPelangganFill, font=("Helvetica", 15), bg = "light grey", fg = "black")
    namaPengunjungFill_var.place(x = 500, y = 250, width = 300, height = 30)

    # Entry box tanggal check in
    Label(screenFillData, text = "Tanggal Check Out", font = ("Helvetica", 15, "bold"), bg="white").place(x = 500, y = 320)
    cal = Calendar(screenFillData, selectmode = 'day', date_pattern = 'yyyy-mm-dd')
    cal.place(x = 500, y = 350, width = 300, height = 200)

    # Button next menuju ambil tanggal dan verifikasi data
    Button(screenFillData, text = "Berikutnya", font = ("Helvetica", 15, "bold"), bg="#71BC68", width = 10, height = 1, command = " ").place(x = 670, y = 580)
    
    # Button back menuju halaman utama check out
    Button(screenFillData, text = "Kembali", font = ("Helvetica", 15, "bold"), bg="#F4AB6A", width = 10, height = 1, command = " ").place(x = 500, y = 580)

    screenFillData.mainloop()


def getCheckInDate():
    global tglCheckIn
    global calendar

    tglCheckIn = calendar.get_date()

def validateCheckInBooking():

    # Connect to database
    try:
        conn = mysql.connector.connect (
            user = 'root',
            password = 'Bel2022Fiy@',
            host = 'localhost',
            database = 'myHotel'
        )
    except mysql.connector.Error as e:
        print(f"Error connecting to Mysql Platform: {e}")
        sys.exit(1)

    cur = conn.cursor()
    try:
        statement = "SELECT nomorKamar, namaPengunjung, NIK, tanggalCheckIn, tanggalCheckOut FROM informasiTamuHotel WHERE NIK = %s AND nomorKamar = %s AND statusPengunjung = %s"
        data = (int(nikPelangganBook.get()), int(noKamarBook.get()), "Book")
        cur.execute(statement, data)
    except mysql.connector.Error as e:
        print(f"Error retrieving entry from Database: {e}")
    
    # Tampilkan informasi dalam bentuk Tabel
    columns = (1,2,3,4,5)
    tree = ttk.Treeview(screenBookValid, height = 1, columns = columns, show = 'headings')
    tree.place(x = 40, y = 220)
    tree.heading(1, text = "Nomor Kamar")
    tree.heading(2, text = "Nama Tamu")
    tree.heading(3, text = "NIK Tamu")
    tree.heading(4, text = "Tanggal Check In")
    tree.heading(5, text = "Tanggal Check Out")


    i = 1
    for (nomorKamar, namaPengunjung, NIK, tanggalCheckIn, tanggalCheckOut) in cur:
        tree.insert(parent='', index=i, text='', values = (nomorKamar, namaPengunjung, NIK, tanggalCheckIn, tanggalCheckOut))
        i += 1
    
    conn.commit()

def validateCheckInWalkIn():

    # Connect to database
    try:
        conn = mysql.connector.connect (
            user = 'root',
            password = 'Bel2022Fiy@',
            host = 'localhost',
            database = 'myHotel'
        )
    except mysql.connector.Error as e:
        print(f"Error connecting to Mysql Platform: {e}")
        sys.exit(1)

    cur = conn.cursor()
    try:
        statement = "SELECT nomorKamar, namaPengunjung, NIK, tanggalCheckIn, tanggalCheckOut FROM informasiTamuHotel WHERE NIK = %s AND nomorKamar = %s AND statusPengunjung = %s"
        data = (int(nikPelangganBook.get()), int(noKamarBook.get()), "Book")
        cur.execute(statement, data)
    except mysql.connector.Error as e:
        print(f"Error retrieving entry from Database: {e}")
    
    # Tampilkan informasi dalam bentuk Tabel
    columns = (1,2,3,4,5)
    tree = ttk.Treeview(screenBookValid, height = 1, columns = columns, show = 'headings')
    tree.place(x = 40, y = 220)
    tree.heading(1, text = "Nomor Kamar")
    tree.heading(2, text = "Nama Tamu")
    tree.heading(3, text = "NIK Tamu")
    tree.heading(4, text = "Tanggal Check In")
    tree.heading(5, text = "Tanggal Check Out")


    i = 1
    for (nomorKamar, namaPengunjung, NIK, tanggalCheckIn, tanggalCheckOut) in cur:
        tree.insert(parent='', index=i, text='', values = (nomorKamar, namaPengunjung, NIK, tanggalCheckIn, tanggalCheckOut))
        i += 1
    
    conn.commit()

def showCheckInBookingValid(screenBooking):
    global screenBookValid
    screenBooking.destroy()
    screenBookValid = Tk()
    screenBookValid.title("myHotel")
    screenBookValid.geometry("1270x690")
    screenBookValid.config(bg = "white")

    # Title
    showTitle(screenBookValid)
    # Section Title
    Label(screenBookValid, text = "Check In", font = ("Helvetica", 12, "bold"), bg="white").place(x = 610, y = 140)
    # Section Title
    Label(screenBookValid, text = "Detail Pesanan Pengunjung", font = ("Helvetica", 10, "bold"), bg="white").place(x = 610, y = 180)

    # Menampilkan data check in pengunjung yang valid
    validateCheckInBooking()

    screenBookValid.mainloop()

def showCheckInWalkInValid(screenFillData):
    global screenWalkInValid
    screenFillData.destroy()
    screenWalkInValid = Tk()
    screenWalkInValid.title("myHotel")
    screenWalkInValid.geometry("1270x690")
    screenWalkInValid.config(bg = "white")

    # Title
    showTitle(screenWalkInValid)
    # Section Title
    Label(screenWalkInValid, text = "Check In", font = ("Helvetica", 12, "bold"), bg="white").place(x = 610, y = 140)
    # Section Title
    Label(screenWalkInValid, text = "Detail Pesanan Pengunjung", font = ("Helvetica", 10, "bold"), bg="white").place(x = 610, y = 180)

    # Menampilkan data check in pengunjung yang valid
    validateCheckInWalkIn()

    screenWalkInValid.mainloop()

def prosesCheckIn():
    # Koneksi ke database
    try:
        conn = mysql.connector.connect (
            user = 'root',
            password = 'Bel2022Fiy@',
            host = 'localhost',
            database = 'myHotel'
        )
    except mysql.connector.Error as e:
        print(f"Error connecting to Mysql Platform: {e}")
        sys.exit(1)
    
    cur = conn.cursor()
    try:
        # Update status pengunjung check in booking menjadi check in pada tabel informasi tamu hotel
        statement = "UPDATE informasiTamuHotel SET statusPengunjung = %s WHERE NIK = %s AND nomorKamar = %s"
        data = ("Check-in", int(nikPelangganBook.get()), int(noKamarBook.get()),)
        cur.execute(statement, data)

        # Update status kamar dari available menjadi unavailable pada Booking Check In pada tabel informasi kamar
        cur = conn.cursor()
        statement = "UPDATE informasiKamar SET statusKamar = %s WHERE nomorKamar = %s"
        data = ("Unavailable", int(noKamarBook.get()),)
        cur.execute(statement, data)

        # Insert data pengunjung baru pada tabel informasi tamu hotel
        cur = conn.cursor()
        statement = "INSERT INTO informasiTamuHotel (NIK, nomorKamar, tanggalCheckIn, tanggalCheckOut, namaPengunjung, statusPengunjung) VALUES (%s, %s, %s, %s, %s, %s)"
        value = ("")

    except mysql.connector.Error as e:
        print(f"Error updating or retrieving entry form database: {e}")

    conn.commit()

def backToHomescreen():
    from home import homescreen
    homescreen(window)

def showTitle(screen):
    Label(screen, text = "myHotel", font = ("Helvetica", 20, "bold"), bg="white").place(x = 590, y = 100)

def showTitleCheckIn(screen):
    Label(screen, text = "Check-In", font = ("Helvetica", 25, "bold"), bg="white").place(x = 610, y = 140)