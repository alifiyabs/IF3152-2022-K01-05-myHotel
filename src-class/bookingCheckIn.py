# Booking Check In
# Nama Penanggung Jawab : Alifiya Brizita Shary
# Melakukan Check In pada Hotel, yaitu Booking Check In dan Check In Walk In
# Menggunakan warna-warna yang sudah dilabeli hex color

import sys
import datetime
# import mariadb
import tkinter as tk
from datetime import datetime
import os
import mysql.connector
# from tkcalendar import Calendar
from tkinter import *
from tkinter import ttk, messagebox
from datetime import date

class BookingCheckIn():

    def BookingCheckIn(self, window):
        global screenBooking
        window.destroy()
        screenBooking = Tk()
        screenBooking.title("myHotel")
        screenBooking.geometry("1270x690")
        screenBooking.config(bg="#F7F0F5")

        global nikPelangganBook
        global noKamarBook
        global nikPelangganBook_var
        global noKamarBook_var
        nikPelangganBook = StringVar()
        noKamarBook = StringVar()

        def backToHomeCheckIn():
            from checkIn import CheckIn
            CheckIn().homeCheckIn(screenBooking)

        # Title
        self.showTitle(screenBooking)
        # Sectione Title
        Label(screenBooking, text = "Booking Check-In", font = ("Helvetica", 10, "bold"), bg="#F7F0F5").place(x = 635, y = 140,anchor="center")

        # Entry box NIK Pelanggan
        Label(screenBooking, text = "NIK Pelanggan", font = ("Helvetica", 12, "bold"), bg="#F7F0F5").place(x = 485, y = 220)
        nikPelangganBook_var = Entry(screenBooking, textvariable= nikPelangganBook,font=("Helvetica", 12), bg = "#DECBB7", fg = "black")
        nikPelangganBook_var.place(x = 635, y = 250, width = 300, height = 30,anchor="n")

        # Entry box Nomor Kamar 
        Label(screenBooking, text = "Nomor Kamar ", font = ("Helvetica", 12, "bold"), bg="#F7F0F5").place(x = 485, y = 300)
        noKamarBook_var= Entry(screenBooking, textvariable= noKamarBook,font=("Helvetica", 12), bg = "#DECBB7", fg = "black")
        noKamarBook_var.place(x = 635, y = 330, width = 300, height = 30,anchor="n")

        # Button next menuju cek ketersediaan kamar 
        Button(screenBooking, text = "Cek Kamar" ,font = ("Helvetica", 12, "bold"), bg="#DECBB7", width = 10, height = 1, command = self.verifikasiBookingCheckIn).place(x = 670, y = 400)
        # Button kembali ke menu utama Check In
        Button(screenBooking, text = "Kembali", font = ("Helvetica", 12, "bold"), bg="#FF595E", width = 10, height = 1, command = backToHomeCheckIn).place(x = 485, y = 400)
    
        
        screenBooking.mainloop()


    def verifikasiBookingCheckIn(self):
        # Buka koneksi dengan database mysql

        #try:
        #    conn = mariadb.connect (
        #        user = 'root',
        #       password = '*****',
        #        host = 'localhost',
        #       database = 'myHotel'
        #    )
        #except mariadb.Error as e:
         #   print(f"Error connecting to Mysql Platform: {e}")
          #  sys.exit(1)
        
        try:
            conn = mysql.connector.connect (
                user = 'root',
                password = 'Bel2022Fiy@',
                host = 'localhost',
                database = 'myHotel',
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
            row = cur.fetchone()
            if (row == None):
                Label(screenBooking, text = "Tidak dapat melakukan check in karena kamar tidak valid!", fg = "red", font = ("Helvetica, 13")).pack()
            else:
                self.showCheckInBookingValid(screenBooking)
        except mysql.connector.Error as e:
            print(f"Error retrieving entry form database: {e}")

    def validateCheckInBooking(self):

        # Connect to database
                #try:
        #    conn = mariadb.connect (
        #        user = 'root',
        #       password = '*****',
        #        host = 'localhost',
        #       database = 'myHotel'
        #    )
        #except mariadb.Error as e:
         #   print(f"Error connecting to Mysql Platform: {e}")
          #  sys.exit(1)

        try:
            conn = mysql.connector.connect (
                user = 'root',
                password = 'Bel2022Fiy@',
                host = 'localhost',
                database = 'myHotel',
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
        
        # Tampilkan informasi 
        for data_tamu in cur:
            nomorKamarVal = data_tamu[0]
            namaPengunjungVal = data_tamu[1]
            NIKVal = data_tamu[2]
            tanggalCheckInVal = data_tamu[3]
            tanggalCheckOutVal = data_tamu[4]

        lf = tk.LabelFrame(screenBookValid, bg='white', padx=5, pady=10)
        lf.place(anchor="c", relx=.5, rely=.5)
        
        Label(lf, text= "Nomor Kamar", font = ("Helvetica", 13), bg= 'white').grid(row=0, column=0, padx=20, pady=5, sticky='W')
        Label(lf, text= "Nama Tamu", font = ("Helvetica", 13), bg= 'white').grid(row=1, column=0, padx=20, pady=5, sticky='W')
        Label(lf, text= "NIK Tamu", font = ("Helvetica", 13), bg= 'white').grid(row=2, column=0, padx=20, pady=5, sticky='W')
        Label(lf, text= "Tanggal Check In", font = ("Helvetica", 13), bg= 'white').grid(row=3, column=0, padx=20, pady=5, sticky='W')
        Label(lf, text= "Tanggal Check Out", font = ("Helvetica", 13), bg= 'white').grid(row=4, column=0, padx=20, pady=5, sticky='W')
        
        Label(lf, text=nomorKamarVal, font = ("Helvetica", 13), bg= 'white').grid(row=0, column=1, padx=20, pady=5, sticky='E')
        Label(lf, text=namaPengunjungVal, font = ("Helvetica", 13), bg= 'white').grid(row=1, column=1, padx=20, pady=5, sticky='E')
        Label(lf, text=NIKVal, font = ("Helvetica", 13), bg= 'white').grid(row=2, column=1, padx=20, pady=5, sticky='E')
        Label(lf, text=tanggalCheckInVal, font = ("Helvetica", 13), bg= 'white').grid(row=3, column=1, padx=20, pady=5, sticky='E')
        Label(lf, text=tanggalCheckOutVal, font = ("Helvetica", 13), bg= 'white').grid(row=4, column=1, padx=20, pady=5, sticky='E')
        
        conn.commit()

    def showCheckInBookingValid(self, screenBooking):
        global screenBookValid
        screenBooking.destroy()
        screenBookValid = Tk()
        screenBookValid.title("myHotel")
        screenBookValid.geometry("1270x690")
        screenBookValid.config(bg = "#F7F0F5")

        # Title
        self.showTitle(screenBookValid)
        # Section Title
        self.showSectionTitle(screenBookValid)
        def ulangiCheckInBooking():
            self.BookingCheckIn(screenBookValid)

        def bukakonfirmasiCheckIn1():
            self.konfirmasiCheckIn1(screenBookValid)

        # Section Title
        Label(screenBookValid, text = "Detail Pesanan Pengunjung", font = ("Helvetica", 10, "bold"), bg="#F7F0F5").place(x = 635, y = 180,anchor="center")

        # Menampilkan data check in pengunjung yang valid
        self.validateCheckInBooking()

        # Button next menuju konfirmasi check in
        Button(screenBookValid, text = "Berikutnya", font = ("Helvetica", 12, "bold"), bg="#DECBB7", width = 10, height = 1, command = bukakonfirmasiCheckIn1).place(x = 785, y = 500,anchor="ne")
        
        # Button back menuju halaman utama check in
        Button(screenBookValid, text = "Kembali", font = ("Helvetica", 12, "bold"), bg="#8F857D", width = 10, height = 1, command = ulangiCheckInBooking).place(x = 485, y = 500)

        screenBookValid.mainloop()

    def konfirmasiCheckIn1(self, screenBookValid):
        global screenKonfirmasi1
        screenBookValid.destroy()
        screenKonfirmasi1 = Tk()
        screenKonfirmasi1.title("myHotel")
        screenKonfirmasi1.geometry("1270x690")
        screenKonfirmasi1.config(bg = "#F7F0F5")

        self.showTitle(screenKonfirmasi1)
        self.showSectionTitle(screenKonfirmasi1)

        def backToShowBook():
            self.showCheckInBookingValid(screenKonfirmasi1)

        Label(screenKonfirmasi1, text = "Lanjutkan Check In?", font = ("Helvetica", 12, "bold"), bg= "#F7F0F5").place(x = 635, y = 220,anchor="center")

        # Button
        Button(screenKonfirmasi1, text = "Ya", font = ("Helvetica", 12, "bold"), bg= "#DECBB7", width=10, height=1, command=self.prosesCheckInBook).place(x = 785, y = 320,anchor="ne")
        Button(screenKonfirmasi1, text = "Tidak", font = ("Helvetica", 12, "bold"), bg= "#8F857D", width=10, height=1, command=backToShowBook).place(x = 485, y = 320)

        screenKonfirmasi1.resizable(False,False)
        screenKonfirmasi1.mainloop()

        
    def prosesCheckInBook(self):
        # Koneksi ke database

                #try:
        #    conn = mariadb.connect (
        #        user = 'root',
        #       password = '*****',
        #        host = 'localhost',
        #       database = 'myHotel'
        #    )
        #except mariadb.Error as e:
         #   print(f"Error connecting to Mysql Platform: {e}")
          #  sys.exit(1)
       
        try:
            conn = mysql.connector.connect (
                user = 'root',
                password = 'Bel2022Fiy@',
                host = 'localhost',
                database = 'myHotel',
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

        except mysql.connector.Error as e:
            print(f"Error updating or retrieving entry form database: {e}")

        conn.commit()
        self.checkInBookingBerhasil(screenKonfirmasi1)

    def checkInBookingBerhasil(self, screenBookValid):
        global screenBookBerhasil
        screenBookValid.destroy()
        screenBookBerhasil = Tk()
        screenBookBerhasil.title("myHotel")
        screenBookBerhasil.geometry("1270x690")
        screenBookBerhasil.config(bg = "#F7F0F5")
        
        self.showTitle(screenBookBerhasil)
        self.showSectionTitle(screenBookBerhasil)

        def ulangCheckInBook():
            self.BookingCheckIn(screenBookBerhasil)
        
        def backToHomescreen():
            from home import ClassHome
            ClassHome().homescreen(screenBookBerhasil)

        Label(screenBookBerhasil, text = "Check In Berhasil dilakukan!", font = ("Helvetica", 18, "bold"), bg= "#F7F0F5").place(x = 635, y = 220,anchor="center")

        # Button
        Button(screenBookBerhasil, text = "Selesai Check In", font = ("Helvetica", 12, "bold"), bg= "#DECBB7", width=15, height=1, command=backToHomescreen).place(x = 785, y = 320,anchor="ne")
        Button(screenBookBerhasil, text = "Kembali", font = ("Helvetica", 12, "bold"), bg= "#FF595E", width=10, height=1, command=ulangCheckInBook).place(x = 485, y = 320)

        screenBookBerhasil.resizable(False,False)
        screenBookBerhasil.mainloop()

    def showTitle(self, screen):
        Label(screen, text="myHotel",font=("helvetica",20,"bold"),bg="#F7F0F5",fg="black").place(x=635,y=100,anchor="center")

    def showSectionTitle(self, screen):
        Label(screen, text="Check-in",font=("helvetica",10,"bold"),bg="#F7F0F5",fg="black").place(x=635,y=140,anchor="center")