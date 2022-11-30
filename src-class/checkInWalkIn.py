# Check In Walk In
# Nama Penanggung Jawab : Alifiya Brizita Shary

# Progress : Sudah berfungsi
# Melakukan Check In pada Hotel, yaitu Check In Walk In yang dilakukan secara langsung ditempat
# Menggunakan warna-warna yang sudah dilabeli hex color

import sys
import datetime
import mariadb
import tkinter as tk
from datetime import datetime
import os
# import mysql.connector
from connectdatabase import conn
from tkcalendar import Calendar
from tkinter import *
#from tkinter import ttk, messagebox
from datetime import date

class ClassCheckInWalkIn():

    def checkInWalkIn(self, window):
        global screenWalkIn
        window.destroy()
        screenWalkIn = Tk()
        screenWalkIn.title("myHotel")
        screenWalkIn.geometry("1270x690")
        screenWalkIn.config(bg="#F7F0F5")

        global noKamarWalkIn
        global noKamarWalkIn_var
        noKamarWalkIn = StringVar()
        
        # Kembali ke halaman utama Check In
        def backToHomeCheckIn():
            from checkIn import ClassCheckIn
            ClassCheckIn().homeCheckIn(screenWalkIn)

        # Entry nomor kamar
        self.showTitle(screenWalkIn)
        Label(screenWalkIn, text = "Check-In Walk In", font = ("Helvetica", 20, "bold"), bg="#F7F0F5").place(x = 635, y = 140,anchor="center")

        Label(screenWalkIn, text = "Nomor Kamar", font = ("Helvetica", 12, "bold"), bg="#F7F0F5").place(x = 500, y = 220)
        noKamarWalkIn_var = Entry(screenWalkIn, textvariable = noKamarWalkIn, font=("Helvetica", 15), bg = "#DECBB7", fg = "black")
        noKamarWalkIn_var.place(x = 635, y = 250, width = 300, height = 30,anchor="n")

        # Button Cek ketersediaan kamar
        Button(screenWalkIn, text = "Cek Kamar" ,font = ("Helvetica", 12, "bold"), bg= "#DECBB7", width = 15, height = 1, command = self.verifikasiCheckInWalkIn).place(x = 670, y = 300)
        # Button kembali ke menu utama Check In
        Button(screenWalkIn, text = "Kembali ke menu Check In", font = ("Helvetica", 10, "bold"), bg="#FF595E", width = 10, height = 1, command = backToHomeCheckIn).place(x = 99, y = 113, width=180, height=49)

        screenWalkIn.mainloop()

    def verifikasiCheckInWalkIn(self):
        
        # Buka koneksi ke Database
        conn
        
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
        screenFillData.config(bg = "#F7F0F5")

        Label(screenFillData, text = "Check-in Walk In", font = ("Helvetica", 20, "bold"), bg="#F7F0F5").place(x=635, y=50, anchor="center")
        Label(screenFillData, text = "Pengisian data pengunjung", font = ("Helvetica", 12, "bold"), bg="#F7F0F5").place(x = 635, y = 90, anchor="center")

        global nikPengunjungFill
        global NIKPengunjungFill_var
        global namaPengunjungFill
        global namaPengunjungFill_var
        global calendarIn
        global calendarOut
        nikPengunjungFill = StringVar()
        namaPengunjungFill = StringVar()

        def backToHomeCheckIn():
            from checkIn import ClassCheckIn
            ClassCheckIn().homeCheckIn(screenFillData)

        def bukaCheckInValid():
            self.showCheckInWalkInValid(screenFillData)

        # Entry box NIK
        Label(screenFillData, text = "NIK Pelanggan", font = ("Helvetica", 12, "bold"), bg="#F7F0F5").place(x = 485, y = 160)
        nikPengunjungFill_var = Entry(screenFillData, textvariable = nikPengunjungFill, font=("Helvetica", 15), bg = "#DECBB7", fg = "black")
        nikPengunjungFill_var.place(x = 635, y = 190, width = 300, height = 30, anchor = "n")

        # Entry box Nama Pelanggan
        Label(screenFillData, text = "Nama Pelanggan", font = ("Helvetica", 12, "bold"), bg="#F7F0F5").place(x = 485, y = 230)
        namaPengunjungFill_var = Entry(screenFillData, textvariable = namaPengunjungFill, font=("Helvetica", 15), bg = "#DECBB7", fg = "black")
        namaPengunjungFill_var.place(x = 635, y = 260, width = 300, height = 30, anchor = "n")

        # Entry box tanggal check in
        Label(screenFillData, text = "Tanggal Check In", font = ("Helvetica", 12, "bold"), bg="#F7F0F5").place(x = 420, y = 330)
        calendarIn = Calendar(screenFillData, selectmode = 'day', date_pattern = 'yyyy-mm-dd', background= "#d5a6bd")
        calendarIn.place(x = 485, y = 360, width = 200, height = 200, anchor = "n")

        # Entry box tanggal check out
        Label(screenFillData, text = "Tanggal Check Out", font = ("Helvetica", 12, "bold"), bg="#F7F0F5").place(x = 710, y = 330)
        calendarOut = Calendar(screenFillData, selectmode = 'day', date_pattern = 'yyyy-mm-dd', background="#d5a6bd")
        calendarOut.place(x = 785, y = 360, width = 200, height = 200, anchor = "n")

        # Button next menuju verifikasi data yang sudah terinsert pada database
        Button(screenFillData, text = "Berikutnya", font = ("Helvetica", 12, "bold"), bg="#71BC68", width = 10, height = 1, command = bukaCheckInValid).place(x = 670, y = 600)
        
        # Button back menuju halaman utama check out
        Button(screenFillData, text = "Batal", font = ("Helvetica", 12, "bold"), bg="#F4AB6A", width = 10, height = 1, command = backToHomeCheckIn).place(x = 485, y = 600)

        screenFillData.mainloop()
    
    def prosesCheckInWalk(self):
       
        # Buka Koneksi Ke Database
        conn
        
        cur = conn.cursor()
        try:

            # Update status kamar dari available menjadi unavailable pada Check In Walk In pada tabel informasi kamar
            cur = conn.cursor()
            statement = "UPDATE informasiKamar SET statusKamar = %s WHERE nomorKamar = %s"
            data = ("Unavailable", int(noKamarWalkIn.get()),)
            cur.execute(statement, data)
            conn.commit()

            # Insert data pengunjung baru pada tabel informasi tamu hotel
            cur = conn.cursor()
            statement = "INSERT INTO informasiTamuHotel (NIK, nomorKamar, tanggalCheckIn, tanggalCheckOut, tipeKamar, namaPengunjung, durasiMenginap, statusPengunjung, totalTagihan) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            # Kondisi jika 
            if (int(noKamarWalkIn.get()) < 200 and int(noKamarWalkIn.get()) >= 100):
                value = (int(nikPengunjungFill.get()), int(noKamarWalkIn.get()), calendarIn.get_date(), calendarOut.get_date(), "Single", namaPengunjungFill.get(), 1, "Check-In", 300000)
            elif (int(noKamarWalkIn.get()) < 300 and int(noKamarWalkIn.get()) >= 200):
                value = (int(nikPengunjungFill.get()), int(noKamarWalkIn.get()), calendarIn.get_date(), calendarOut.get_date(), "Double", namaPengunjungFill.get(), 2, "Check-In", 1200000)
            else:
                value = (int(nikPengunjungFill.get()), int(noKamarWalkIn.get()), calendarIn.get_date(), calendarOut.get_date(), "Deluxe", namaPengunjungFill.get(), 3 , "Check-In", 1000000)
            cur.execute(statement,value)
            conn.commit()
        except mariadb.Error as e:
            print(f"Error updating or retrieving entry form database: {e}")

        # conn.commit()
        self.checkInWalkInBerhasil(screenWalkInValid)

    def getCheckInDate():
        global tglCheckIn

        tglCheckIn = calendarIn.get_date()

    def getCheckOutDate():
        global tglCheckOut

        tglCheckOut = calendarOut.get_date()

    def validateCheckInWalkIn(self):
        
        frame = tk.LabelFrame(screenWalkInValid, bg='white', padx=5, pady=10)
        # lf.grid(row=0, column=0, padx=0, pady=35, sticky=CENTER)
        frame.place(anchor="c", relx=.5, rely=.5)
            
        Label(frame, text= "Nomor Kamar", font = ("Helvetica", 13), bg= 'white').grid(row=0, column=0, padx=20, pady=5, sticky='W')
        Label(frame, text= "Nama Tamu", font = ("Helvetica", 13), bg= 'white').grid(row=1, column=0, padx=20, pady=5, sticky='W')
        Label(frame, text= "NIK Tamu", font = ("Helvetica", 13), bg= 'white').grid(row=2, column=0, padx=20, pady=5, sticky='W')
        Label(frame, text= "Tanggal Check In", font = ("Helvetica", 13), bg= 'white').grid(row=3, column=0, padx=20, pady=5, sticky='W')
        Label(frame, text= "Tanggal Check Out", font = ("Helvetica", 13), bg= 'white').grid(row=4, column=0, padx=20, pady=5, sticky='W')

        Label(frame, text=noKamarWalkIn.get(), font = ("Helvetica", 13), bg= 'white').grid(row=0, column=1, padx=20, pady=5, sticky='E')
        Label(frame, text=namaPengunjungFill.get(), font = ("Helvetica", 13), bg= 'white').grid(row=1, column=1, padx=20, pady=5, sticky='E')
        Label(frame, text=nikPengunjungFill.get(), font = ("Helvetica", 13), bg= 'white').grid(row=2, column=1, padx=20, pady=5, sticky='E')
        Label(frame, text=calendarIn.get_date(), font = ("Helvetica", 13), bg= 'white').grid(row=3, column=1, padx=20, pady=5, sticky='E')
        Label(frame, text=calendarOut.get_date(), font = ("Helvetica", 13), bg= 'white').grid(row=4, column=1, padx=20, pady=5, sticky='E')


    def showCheckInWalkInValid(self, screenKonfirmasi2):
        global screenWalkInValid
        global frame
        screenKonfirmasi2.destroy()
        screenWalkInValid = Tk()
        screenWalkInValid.title("myHotel")
        screenWalkInValid.geometry("1270x690")
        screenWalkInValid.config(bg = "#F7F0F5")

        # Title
        self.showTitle(screenWalkInValid)
        # Section Title
        self.showSectionTitle(screenWalkInValid)

        # Kembali ke homescreen
        def backToCheckIn():
            from checkIn import ClassCheckIn
            ClassCheckIn().homeCheckIn(screenWalkInValid)
        
        # Section Title
        Label(screenWalkInValid, text = "Detail Pesanan Pengunjung", font = ("Helvetica", 10, "bold"), bg="#F7F0F5").place(x = 635, y = 180,anchor="center")
        Label(screenWalkInValid, text = "Lanjutkan Check-in?", font = ("Helvetica", 15, "bold"), bg="#F7F0F5").place(x = 635, y = 220,anchor="center")
        
        #  Menampilkan data check in pengunjung yang valid
        self.validateCheckInWalkIn()

        # Button next menuju konfirmasi check in
        Button(screenWalkInValid, text = "Ya", font = ("Helvetica", 12, "bold"), bg="#DECBB7", width = 10, height = 1, command = self.prosesCheckInWalk).place(x = 785, y = 500,anchor="ne")
        
        # Button back menuju halaman utama check in
        Button(screenWalkInValid, text = "Tidak", font = ("Helvetica", 12, "bold"), bg="#8F857D", width = 10, height = 1, command = backToCheckIn).place(x = 485, y = 500)

        screenWalkInValid.resizable(FALSE,FALSE)
        screenWalkInValid.mainloop()
        
    def checkInWalkInBerhasil(self, screenWalkInValid):
        global screenWalkInBerhasil
        screenWalkInValid.destroy()
        screenWalkInBerhasil = Tk()
        screenWalkInBerhasil.title("myHotel")
        screenWalkInBerhasil.geometry("1270x690")
        screenWalkInBerhasil.config(bg = "#F7F0F5")
        
        self.showTitle(screenWalkInBerhasil)
        self.showSectionTitle(screenWalkInBerhasil)
        
        def backToHomescreen():
            from home import ClassHome
            ClassHome().homescreen(screenWalkInBerhasil)

        Label(screenWalkInBerhasil, text = "Check In Berhasil dilakukan!", font = ("Helvetica", 18, "bold"), bg= "#F7F0F5").place(x = 635, y = 220,anchor="center")

        # Button
        Button(screenWalkInBerhasil, text = "Selesai Check In", font = ("Helvetica", 12, "bold"), bg= "#DECBB7", width=15, height=1, command=backToHomescreen).place(x = 635, y = 320, anchor="center")

        screenWalkInBerhasil.resizable(False,False)
        screenWalkInBerhasil.mainloop()

    def showTitle(self, screen):
        Label(screen, text="myHotel",font=("helvetica",20,"bold"),bg="#F7F0F5",fg="black").place(x=635,y=100,anchor="center")

    def showSectionTitle(self, screen):
        Label(screen, text="Check-in Walk In",font=("helvetica",10,"bold"),bg="#F7F0F5",fg="black").place(x=635,y=140,anchor="center")