# Check In
# Nama PenangBel2022Fiy@gung Jawab : Alifiya Brizita Shary
# Melakukan Check In pada Hotel, yaitu Booking Check In dan Check In Walk In

import sys
import datetime
import mariadb
import tkinter as tk
import datetime
import os
from tkcalendar import Calendar
from tkinter import *
from tkinter import ttk, messagebox
from datetime import date

class CheckIn():
    def homeCheckIn(self, halaman):
        global window
        halaman.destroy()
        window = Tk()
        window.title("myHotel")
        window.geometry("1270x690")
        window.config(bg="white")
        
        # Tampilan Judul myHotel dan Judul Check In
        self.showTitle(window)
        self.showSectionTitle(window)

        # Buka halaman Booking Check In
        def bukaBookingCheckIn():
            self.BookingCheckIn(window)
        # Buka halaman Booking Walk In
        def bukaWalkIn():
            self.checkInWalkIn(window)

        # Button bookingCheckIn menuju ke bookingCheckIn
        Button(window, text = "Booking Check In", font = ("Helvetica", 15, "bold"), bg="#71BC68", width = 20, height = 2, command = bukaBookingCheckIn).place(x = 350, y = 500)
        # Button checkInWalkIn menuju ke checkInWalkIn
        Button(window, text = "Check In Walk In", font = ("Helvetica", 15, "bold"), bg="#71BC68", width = 20, height = 2, command = bukaWalkIn).place(x = 730, y = 500)
        # Button kembali ke menu utama
        Button(window, text = "Kembali ke menu utama", font = ("Helvetica", 10, "bold"), bg="red", width = 10, height = 1, command = self.backToHomescreen).place(x = 99, y = 113, width=180, height=49)
    
        window.mainloop()

    def BookingCheckIn(self, window):
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

        def backToHomeCheckIn():
            self.homeCheckIn(screenBooking)

        # Title
        self.showTitle(screenBooking)
        # Sectione Title
        Label(screenBooking, text = "Booking Check-In", font = ("Helvetica", 20, "bold"), bg="white").place(x = 635, y = 140,anchor="center")

        # Entry box NIK Pelanggan
        Label(screenBooking, text = "NIK Pelanggan", font = ("Helvetica", 15, "bold"), bg="white").place(x = 500, y = 220)
        nikPelangganBook_var = Entry(screenBooking, textvariable= nikPelangganBook,font=("Helvetica", 15), bg = "#ADD8E6", fg = "black")
        nikPelangganBook_var.place(x = 635, y = 250, width = 300, height = 30,anchor="n")

        # Entry box Nomor Kamar 
        Label(screenBooking, text = "Nomor Kamar ", font = ("Helvetica", 15, "bold"), bg="white").place(x = 500, y = 320)
        noKamarBook_var= Entry(screenBooking, textvariable= noKamarBook,font=("Helvetica", 15), bg = "#ADD8E6", fg = "black")
        noKamarBook_var.place(x = 635, y = 350, width = 300, height = 30,anchor="n")

        # Button next menuju cek ketersediaan kamar 
        Button(screenBooking, text = "Cek Kamar" ,font = ("Helvetica", 15, "bold"), bg="#90EE90", width = 15, height = 2, command = self.verifikasiBookingCheckIn).place(x = 670, y = 430)
        # Button kembali ke menu utama Check In
        Button(screenBooking, text = "Kembali ke menu Check In", font = ("Helvetica", 10, "bold"), bg="#FFA07A", width = 10, height = 1, command = backToHomeCheckIn).place(x = 99, y = 113, width=180, height=49)
    
        
        screenBooking.mainloop()

    def checkInWalkIn(self, window):
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
            self.isiDataPengunjung(screenWalkIn)
        
        # Kembali ke halaman utama Check In
        def backToHomeCheckIn():
            self.homeCheckIn(screenWalkIn)

        # Entry nomor kamar
        self.showTitle(screenWalkIn)
        Label(screenWalkIn, text = "Check-In Walk In", font = ("Helvetica", 20, "bold"), bg="white").place(x = 635, y = 140,anchor="center")

        Label(screenWalkIn, text = "Nomor Kamar", font = ("Helvetica", 15, "bold"), bg="white").place(x = 500, y = 220)
        noKamarWalkIn_var = Entry(screenWalkIn, textvariable = noKamarWalkIn, font=("Helvetica", 15), bg = "#ADD8E6", fg = "black")
        noKamarWalkIn_var.place(x = 635, y = 250, width = 300, height = 30,anchor="n")

        # Button Cek ketersediaan kamar
        Button(screenWalkIn, text = "Cek Kamar" ,font = ("Helvetica", 15, "bold"), bg= "#90EE90", width = 15, height = 2, command = self.verifikasiCheckInWalkIn).place(x = 670, y = 300)
        # Button kembali ke menu utama Check In
        Button(screenWalkIn, text = "Kembali ke menu Check In", font = ("Helvetica", 10, "bold"), bg="#FFA07A", width = 10, height = 1, command = backToHomeCheckIn).place(x = 99, y = 113, width=180, height=49)

        screenWalkIn.mainloop()

    def verifikasiBookingCheckIn(self):
        # Buka koneksi dengan database mysql

        try:
            conn = mariadb.connect (
                user = 'root',
                password = '*****',
                host = 'localhost',
                database = 'myHotel'
            )
        except mariadb.Error as e:
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
        except mariadb.Error as e:
            print(f"Error retrieving entry form database: {e}")

    def verifikasiCheckInWalkIn(self):
        # Buka koneksi dengan database mysql
        try:
            conn = mariadb.connect (
                user = 'root',
                password = '*****',
                host = 'localhost',
                database = 'myHotel'
            )
        except mariadb.Error as e:
            print(f"Error connecting to Mysql Platform: {e}")
            sys.exit(1)
        
        # Execute Query
        cur = conn.cursor()
        try:
            statement = "SELECT nomorKamar FROM informasiKamar WHERE nomorKamar = %s AND statusKamar = %s"
            data = (int(noKamarWalkIn_var.get()), "Available",)
            cur.execute(statement, data)
            row = cur.fetchone()
            if (row == None):
                Label(screenWalkIn, text = "Tidak dapat melakukan check in karena kamar tidak valid!", fg = "red", font = ("Helvetica, 13")).pack()
            else:
                self.isiDataPengunjung(screenWalkIn)
        except mariadb.Error as e:
            print(f"Error retrieving entry form database: {e}")

    def isiDataPengunjung(self, screenWalkIn):
        global screenFillData
        screenWalkIn.destroy()
        screenFillData = Tk()
        screenFillData.title("myHotel")
        screenFillData.geometry("1270x690")
        screenFillData.config(bg = "white")

        Label(screenFillData, text = "myHotel", font = ("Helvetica", 20, "bold"), bg="white").place(x=635, y=50, anchor="center")
        Label(screenFillData, text = "Pengisian data pengunjung", font = ("Helvetica", 20, "bold"), bg="white").place(x = 635, y = 90, anchor="center")

        global nikPengunjungFill
        global NIKPengunjungFill_var
        global namaPengunjungFill
        global namaPengunjungFill_var
        global calendarIn
        global calendarOut
        nikPengunjungFill = StringVar()
        namaPengunjungFill = StringVar()

        def backToHomeCheckIn():
            self.homeCheckIn(screenFillData)
        def bukaShowWalkIn():
            self.showCheckInWalkInValid(screenFillData)

        # Entry box NIK
        Label(screenFillData, text = "NIK Pelanggan", font = ("Helvetica", 15, "bold"), bg="white").place(x = 330, y = 300)
        nikPengunjungFill_var = Entry(screenFillData, textvariable = nikPengunjungFill, font=("Helvetica", 15), bg = "light grey", fg = "black")
        nikPengunjungFill_var.place(x = 400, y = 330, width = 300, height = 30, anchor = "n")

        # Entry box Nama Pelanggan
        Label(screenFillData, text = "Nama Pelanggan", font = ("Helvetica", 15, "bold"), bg="white").place(x = 330, y = 370)
        namaPengunjungFill_var = Entry(screenFillData, textvariable = namaPengunjungFill, font=("Helvetica", 15), bg = "light grey", fg = "black")
        namaPengunjungFill_var.place(x = 400, y = 400, width = 300, height = 30, anchor = "n")

        # Entry box tanggal check in
        Label(screenFillData, text = "Tanggal Check In", font = ("Helvetica", 15, "bold"), bg="white").place(x = 730, y = 120)
        calendarIn = Calendar(screenFillData, selectmode = 'day', date_pattern = 'yyyy-mm-dd')
        calendarIn.place(x = 800, y = 150, width = 300, height = 200, anchor = "n")

        # Entry box tanggal check out
        Label(screenFillData, text = "Tanggal Check Out", font = ("Helvetica", 15, "bold"), bg="white").place(x = 730, y = 420)
        calendarOut = Calendar(screenFillData, selectmode = 'day', date_pattern = 'yyyy-mm-dd')
        calendarOut.place(x = 800, y = 450, width = 300, height = 200, anchor = "n")

        # Button next menuju verifikasi data yang sudah terinsert pada database
        Button(screenFillData, text = "Berikutnya", font = ("Helvetica", 15, "bold"), bg="#71BC68", width = 10, height = 1, command = self.prosesCheckInWalk).place(x = 200, y = 200)
        
        # Button back menuju halaman utama check out
        Button(screenFillData, text = "Batal", font = ("Helvetica", 15, "bold"), bg="#F4AB6A", width = 10, height = 1, command = backToHomeCheckIn).place(x = 200, y = 220)

        screenFillData.mainloop()


    # def getCheckInDate():
        # global tglCheckIn

        # tglCheckIn = calendarIn.get_date()

    # def getCheckOutDate():
        # global tglCheckOut

        # tglCheckOut = calendarOut.get_date()

    def validateCheckInBooking(self):

        # Connect to database
        try:
            conn = mariadb.connect (
                user = 'root',
                password = '*****',
                host = 'localhost',
                database = 'myHotel'
            )
        except mariadb.Error as e:
            print(f"Error connecting to Mysql Platform: {e}")
            sys.exit(1)

        cur = conn.cursor()
        try:
            statement = "SELECT nomorKamar, namaPengunjung, NIK, tanggalCheckIn, tanggalCheckOut FROM informasiTamuHotel WHERE NIK = %s AND nomorKamar = %s AND statusPengunjung = %s"
            data = (int(nikPelangganBook.get()), int(noKamarBook.get()), "Book")
            cur.execute(statement, data)
        except mariadb.Error as e:
            print(f"Error retrieving entry from Database: {e}")
        
        # Tampilkan informasi dalam bentuk Tabel
        columns = (1,2,3,4,5)
        tree = ttk.Treeview(screenBookValid, height = 1, columns = columns, show = 'headings')
        tree.place(x = 60, y = 220)
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

    def validateCheckInWalkIn(self):

        # Connect to database
        try:
            conn = mariadb.connect (
                user = 'root',
                password = '*****',
                host = 'localhost',
                database = 'myHotel'
            )
        except mariadb.Error as e:
            print(f"Error connecting to Mysql Platform: {e}")
            sys.exit(1)

        cur = conn.cursor()
        try:
            statement = "SELECT nomorKamar, namaPengunjung, NIK, tanggalCheckIn, tanggalCheckOut FROM informasiTamuHotel WHERE noKamar = %s AND statusKamar = %s"
            data = (int(noKamarWalkIn.get()), "Available")
            cur.execute(statement, data)
        except mariadb.Error as e:
            print(f"Error retrieving entry from Database: {e}")
        
        # Tampilkan informasi dalam bentuk Tabel
        columns = (1,2,3,4,5)
        tree = ttk.Treeview(screenWalkInValid, height = 1, columns = columns, show = 'headings')
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

    def showCheckInBookingValid(self, screenBooking):
        global screenBookValid
        screenBooking.destroy()
        screenBookValid = Tk()
        screenBookValid.title("myHotel")
        screenBookValid.geometry("1270x690")
        screenBookValid.config(bg = "white")

        # Title
        self.showTitle(screenBookValid)
        # Section Title
        self.showSectionTitle(screenBookValid)
        def ulangiCheckIn():
            self.homeCheckIn(screenBookValid)

        # Section Title
        Label(screenBookValid, text = "Detail Pesanan Pengunjung", font = ("Helvetica", 10, "bold"), bg="white").place(x = 635, y = 180,anchor="center")

        # Menampilkan data check in pengunjung yang valid
        self.validateCheckInBooking()

        # Button next menuju konfirmasi check in
        Button(screenBookValid, text = "Berikutnya", font = ("Helvetica", 12, "bold"), bg="#DECBB7", width = 10, height = 1, command = self.konfirmasiCheckIn1).place(x = 785, y = 400,anchor="ne")
        
        # Button back menuju halaman utama check in
        Button(screenBookValid, text = "Kembali", font = ("Helvetica", 12, "bold"), bg="#8F857D", width = 10, height = 1, command = ulangiCheckIn).place(x = 485, y = 400)

        screenBookValid.mainloop()

    def showCheckInWalkInValid(self, screenFillData):
        global screenWalkInValid
        screenFillData.destroy()
        screenWalkInValid = Tk()
        screenWalkInValid.title("myHotel")
        screenWalkInValid.geometry("1270x690")
        screenWalkInValid.config(bg = "#FAF0E6")

        # Title
        self.showTitle(screenWalkInValid)
        # Section Title
        self.showSectionTitle(screenWalkInValid)

        def ulangiCheckIn():
            self.homeCheckIn(screenWalkInValid)
        # Section Title
        Label(screenWalkInValid, text = "Detail Pesanan Pengunjung", font = ("Helvetica", 10, "bold"), bg="white").place(x = 635, y = 180,anchor="center")

        # Menampilkan data check in pengunjung yang valid
        self.validateCheckInWalkIn()

        # Button next menuju konfirmasi check in
        Button(screenWalkInValid, text = "Berikutnya", font = ("Helvetica", 12, "bold"), bg="#DECBB7", width = 10, height = 1, command = self.konfirmasiCheckIn1).place(x = 785, y = 400,anchor="ne")
        
        # Button back menuju halaman utama check in
        Button(screenWalkInValid, text = "Kembali", font = ("Helvetica", 12, "bold"), bg="#8F857D", width = 10, height = 1, command = ulangiCheckIn).place(x = 485, y = 400)

        screenWalkInValid.mainloop()

    def konfirmasiCheckIn1(self, screenBookValid):
        global screenKonfirmasi1
        screenBookValid.destroy
        screenKonfirmasi1 = Tk()
        screenKonfirmasi1.title("myHotel")
        screenKonfirmasi1.geometry("1270x690")
        screenKonfirmasi1.config(bg = "#FAF0E6")

        self.showTitle(screenKonfirmasi1)
        self.showSectionTitle(screenKonfirmasi1)

        def backToShowBook():
            self.showCheckInBookingValid(screenKonfirmasi1)

        Label(screenKonfirmasi1, text = "Lanjutkan Check In?", font = ("Helvetica", 12, "bold"), bg= "#FAF0E6").place(x = 635, y = 220,anchor="center")

        # Button
        Button(screenKonfirmasi1, text = "Ya", font = ("Helvetica", 12, "bold"), bg= "#90EE90", width=10, height=1, command=self.prosesCheckInBook).place(x = 785, y = 320, anchor="se")
        Button(screenKonfirmasi1, text = "Tidak", font = ("Helvetica", 12, "bold"), bg= "#FFA07A", width=10, height=1, command=backToShowBook).place(x = 785, y = 320, anchor="sw")

        screenKonfirmasi1.resizable(False,False)
        screenKonfirmasi1.mainloop()

    def konfirmasiCheckIn2(self, screenWalkInValid):
        global screenKonfirmasi2
        screenWalkInValid.destroy
        screenKonfirmasi2 = Tk()
        screenKonfirmasi2.title("myHotel")
        screenKonfirmasi2.geometry("1270x690")
        screenKonfirmasi2.config(bg = "#FAF0E6")

        self.showTitle(screenKonfirmasi2)
        self.showSectionTitle(screenKonfirmasi2)

        def backToShowBook():
            self.showCheckInWalkInValid(screenKonfirmasi2)

        Label(screenKonfirmasi2, text = "Lanjutkan Check In?", font = ("Helvetica", 12, "bold"), bg= "#FAF0E6").place(x = 635, y = 220,anchor="center")

        # Button
        Button(screenKonfirmasi2, text = "Ya", font = ("Helvetica", 12, "bold"), bg= "#90EE90", width=10, height=1, command=self.prosesCheckInBook).place(x = 785, y = 320, anchor="se")
        Button(screenKonfirmasi2, text = "Tidak", font = ("Helvetica", 12, "bold"), bg= "#FFA07A", width=10, height=1, command=backToShowBook).place(x = 785, y = 320, anchor="sw")

        screenKonfirmasi2.resizable(False,False)
        screenKonfirmasi2.mainloop()
        
    def prosesCheckInBook(self):
        # Koneksi ke database
        try:
            conn = mariadb.connect (
                user = 'root',
                password = '*****',
                host = 'localhost',
                database = 'myHotel'
            )
        except mariadb.Error as e:
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

        except mariadb.Error as e:
            print(f"Error updating or retrieving entry form database: {e}")

        conn.commit()
        self.checkInBookingBerhasil(screenBookBerhasil)

    def prosesCheckInWalk(self):
        # Koneksi ke database
        try:
            conn = mariadb.connect (
                user = 'root',
                password = '*****',
                host = 'localhost',
                database = 'myHotel'
            )
        except mariadb.Error as e:
            print(f"Error connecting to Mysql Platform: {e}")
            sys.exit(1)
        
        cur = conn.cursor()
        try:

            # Update status kamar dari available menjadi unavailable pada Check In Walk In pada tabel informasi kamar
            cur = conn.cursor()
            statement = "UPDATE informasiKamar SET statusKamar = %s WHERE nomorKamar = %s"
            data = ("Unavailable", int(noKamarWalkIn.get()),)
            cur.execute(statement, data)

            # Insert data pengunjung baru pada tabel informasi tamu hotel
            cur = conn.cursor()
            statement = "INSERT INTO informasiTamuHotel (NIK, nomorKamar, tanggalCheckIn, tanggalCheckOut, namaPengunjung, statusPengunjung) VALUES (%s, %s, %s, %s, %s, %s)"
            value = (int(nikPengunjungFill.get()), int(noKamarWalkIn.get()), calendarIn, calendarOut, namaPengunjungFill.get(), "Check-In",)
            cur.execute(statement,value)
        except mariadb.Error as e:
            print(f"Error updating or retrieving entry form database: {e}")

        conn.commit()
        self.showCheckInWalkInValid(screenFillData)

    def checkInBookingBerhasil(self, screenBookValid):
        global screenBookBerhasil
        screenBookValid.destroy
        screenBookBerhasil = Tk()
        screenBookBerhasil.title("myHotel")
        screenBookBerhasil.geometry("1270x690")
        screenBookBerhasil.config(bg = "#FAF0E6")
        
        self.showTitle(screenBookBerhasil)
        self.showSectionTitle(screenBookBerhasil)

        def ulangCheckInBook():
            self.BookingCheckIn(screenBookValid)
        
        def backToHomescreen():
            from home import Home
            Home().homescreen(screenBookValid)

        Label(screenBookBerhasil, text = "Check In Berhasil dilakukan!", font = ("Helvetica", 12, "bold"), bg= "#FAF0E6").place(x = 635, y = 220,anchor="center")

        # Button
        Button(screenBookBerhasil, text = "Selesai Check In", font = ("Helvetica", 12, "bold"), bg= "#90EE90", width=10, height=1, command=backToHomescreen).place(x = 785, y = 320, anchor="se")
        Button(screenBookBerhasil, text = "Kembali", font = ("Helvetica", 12, "bold"), bg= "#FFA07A", width=10, height=1, command=ulangCheckInBook).place(x = 785, y = 320, anchor="sw")

        screenBookBerhasil.resizable(False,False)
        screenBookBerhasil.mainloop()

    def checkInWalkInBerhasil(self, screenWalkInValid):
        global screenWalkInBerhasil
        screenWalkInValid.destroy
        screenWalkInBerhasil = Tk()
        screenWalkInBerhasil.title("myHotel")
        screenWalkInBerhasil.geometry("1270x690")
        screenWalkInBerhasil.config(bg = "#FAF0E6")
        
        self.showTitle(screenWalkInBerhasil)
        self.showSectionTitle(screenWalkInBerhasil)

        def ulangCheckInWalk():
            self.BookingCheckIn(screenWalkInBerhasil)
        
        def backToHomescreen():
            from home import Home
            Home().homescreen(screenWalkInBerhasil)

        Label(screenWalkInBerhasil, text = "Check In Berhasil dilakukan!", font = ("Helvetica", 12, "bold"), bg= "#FAF0E6").place(x = 635, y = 220,anchor="center")

        # Button
        Button(screenWalkInBerhasil, text = "Selesai Check In", font = ("Helvetica", 12, "bold"), bg= "#90EE90", width=10, height=1, command=backToHomescreen).place(x = 785, y = 320, anchor="se")
        Button(screenWalkInBerhasil, text = "Kembali", font = ("Helvetica", 12, "bold"), bg= "#FFA07A", width=10, height=1, command=ulangCheckInWalk).place(x = 785, y = 320, anchor="sw")

        screenBookBerhasil.resizable(False,False)
        screenBookBerhasil.mainloop()

    def backToHomescreen(self):
        from home import homescreen
        homescreen(window)

    # Kembali ke halaman utama Check In

    def showTitle(self, screen):
        Label(screen, text = "myHotel", font = ("Helvetica", 20, "bold"), bg="white").place(x = 635, y = 100, anchor="center")

    def showSectionTitle(self, screen):
        Label(screen, text = "Check-In", font = ("Helvetica", 25, "bold"), bg="white").place(x = 635, y = 140,anchor="center")
