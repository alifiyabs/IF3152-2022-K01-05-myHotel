# Check In
# Penanggung Jawab: 18220069 Alifiya Brizita Shary

import sys
import datetime
import mysql.connector
import tkinter as tk
import datetime
import os
from tkcalendar import Calendar
from tkinter import *
from tkinter import ttk, messagebox
from datetime import date


def homeCheckIn(halaman):
    global screen
    halaman.destroy()
    screen = Tk()
    screen.title("myHotel")
    screen.geometry("1270x690")
    screen.config(bg="white")
        
    # Title
    Label(screen, text = "myHotel", font = ("Helvetica", 20, "bold"), bg="white").place(x = 610, y = 100)
    # Section Title
    Label(screen, text = "Check In", font = ("Helvetica", 12, "bold"), bg="white").place(x = 610, y = 140)
        
    # Button bookingCheckIn menuju ke bookingCheckIn
    Button(screen, text = "Booking Check In", font = ("Helvetica", 15, "bold"), bg="#71BC68", width = 10, height = 1, command = BookingCheckIn).place(x = 250, y = 300)

    # Button checkInWalkIn menuju ke checkInWalkIn
    Button(screen, text = "Check In Walk In", font = ("Helvetica", 15, "bold"), bg="#71BC68", width = 10, height = 1, command = "verifyBooking").place(x = 750, y = 300)
        
    screen.mainloop()

def BookingCheckIn(screen):
    global screenBooking
    screen.destroy()
    screenBooking = Tk()
    screenBooking.title("myHotel")
    screenBooking.geometry("1270x690")
    screenBooking.config(bg="white")

    global nikPelanggan
    global noKamar
    global inputNikPelanggan
    global inputnoKamar
    nikPelanggan = StringVar()
    noKamar = StringVar()


    # Title
    Label(screenBooking, text = "myHotel", font = ("Helvetica", 20, "bold"), bg="white").place(x = 610, y = 100)
    # Sectione Title
    Label(screenBooking, text = "Booking Check In", font = ("Helvetica", 12, "bold"), bg="white").place(x = 610, y = 140)

    # Entry box NIK Pelanggan
    Label(screenBooking, text = "NIK Pelanggan", font = ("Helvetica", 15, "bold"), bg="white").place(x = 500, y = 220)
    inputNikPelanggan = Entry(screenBooking, textvariable= nikPelanggan,font=("Helvetica", 15), bg = "light grey", fg = "black")
    inputNikPelanggan.place(x = 500, y = 250, width = 300, height = 30)

    # Entry box Nomor Kamar 
    Label(screenBooking, text = "Nomor Kamar ", font = ("Helvetica", 15, "bold"), bg="white").place(x = 500, y = 240)
    inputNikPelanggan = Entry(screenBooking, textvariable= nikPelanggan,font=("Helvetica", 15), bg = "light grey", fg = "black")
    inputNikPelanggan.place(x = 500, y = 270, width = 300, height = 30)

    # Button next menuju cek ketersediaan kamar 
    Button(screenBooking, text = "Cek Kamar",font = ("Helvetica", 15, "bold"), bg="#71BC68", width = 10, height = 1, command = verifyBookingCheckIn).place(x = 500, y = 320)

    screenBooking.mainloop()

def verifyBookingCheckIn():
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
        data = (int(nikPelanggan.get()), int(noKamar.get()), "Book",)
        cur.execute(statement, data)
        row = cur.fetchone()
        if (row == None):
            Label(screen, text = "Tidak dapat melakukan check in karena nomor kamar tidak valid!", fg = "red", font = ("Helvetica, 13")).pack()
        else:
            checkInValid(screen)
    
    except mysql.connector.Error as e:
        print(f"Error retrieving entry form database: {e}")


def checkInValid(screen):
    global screenValid
    screen.destroy()
    screenValid = Tk()
    screenValid.title("myHotel")
    screenValid.geometry("1270x690")
    screenValid.config(bg = "white")

    # Title
    Label(screenValid, text = "myHotel", font = ("Helvetica", 20, "bold"), bg="white").place(x = 610, y = 100)
    # Section Title
    Label(screenValid, text = "Check In", font = ("Helvetica", 12, "bold"), bg="white").place(x = 610, y = 140)
    # Section Title
    Label(screenValid, text = "Detail Pesanan Pengunjung", font = ("Helvetica", 10, "bold"), bg="white").place(x = 610, y = 180)

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
        statement = "SELECT nomorKamar, namaPengunjung, NIK FROM informasiTamuHotel WHERE NIK = %s AND nomorKamar = %s AND statusPengunjung = %s"
        data = (int(nikPelanggan.get()), int(noKamar.get()), "Book")

    except mysql.connector.Error as e:
        print(f"Error retrieving entry from Database: {e}")
    
    # Tampilkan informasi dalam bentuk Tabel
    columns = (1,2,3)
    tree = ttk.Treeview(screenValid, height = 1, columns = columns, show = 'headings')
    tree.place(x = 40, y = 220)
    tree.heading(1, text = "Nomor Kamar")
    tree.heading(2, text = "Nama Tamu")
    tree.heading(3, text = "NIK Tamu")

    i = 1
    for (nomorKamar, namaPengunjung, NIK, tanggalCheckIn) in cur:
        tree.insert(parent='', index=i, text='', values = (nomorKamar, namaPengunjung, NIK, tanggalCheckIn))
        i += 1
    
    conn.commit()