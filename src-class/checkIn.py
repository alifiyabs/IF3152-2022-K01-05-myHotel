# Check In
# Nama Penanggung Jawab : Alifiya Brizita Shary

# Progress : Sudah berfungsi
# Melakukan Check In pada Hotel, yaitu Booking Check In dan Check In Walk In
# Menggunakan warna-warna yang sudah dilabeli hex color

import sys
import datetime
import mariadb
import tkinter as tk
#from datetime import datetime
import os
#import mysql.connector
from PIL import ImageTk, Image
from tkcalendar import Calendar
from tkinter import *
from tkinter import ttk, messagebox
from datetime import date

pathToImg = os.path.abspath('.') + '/img'
#pathToImg = os.path.abspath('..') + '//img' --> UNTUK WINDOWS YA

class ClassCheckIn():
    def homeCheckIn(self, halaman):
        global window
        halaman.destroy()
        window = Tk()
        window.title("myHotel")
        window.geometry("1270x690")
        window.config(bg="#F7F0F5")

        framecheckin = Frame(window, width=1270, height=690, highlightthickness=0, bg="#F7F0F5")
        framecheckin.place(anchor="center", relx=0.5, rely=0.5)

        # Buka halaman Booking Check In
        def bukaBookingCheckIn():
            from bookingCheckIn import ClassBookingCheckIn
            ClassBookingCheckIn().BookingCheckIn(window)
        # Buka halaman Booking Walk In
        def bukaWalkIn():
            from checkInWalkIn import ClassCheckInWalkIn
            ClassCheckInWalkIn().checkInWalkIn(window)
        
        # Tampilan Judul myHotel dan Judul Check In
        self.showTitle(framecheckin)
        self.showSectionTitle(framecheckin)
        
         # Insert img CheckIn
        imgcheckin = PhotoImage(file=pathToImg+'/CheckIn.png')
        label = Label(framecheckin, image=imgcheckin)
        label.grid(row=2,column=1,columnspan=2, pady=(0,80))


        # Button bookingCheckIn menuju ke bookingCheckIn
        Button(framecheckin, text = "Booking Check In", font = ("Helvetica", 12, "bold"), bg="#DECBB7", width = 15, height = 2, command = bukaBookingCheckIn).grid(row=3,column=1, padx=(0,20), pady=(0,100))
        # Button checkInWalkIn menuju ke checkInWalkIn
        Button(framecheckin, text = "Check In Walk In", font = ("Helvetica", 12, "bold"), bg="#DECBB7", width = 15, height = 2, command = bukaWalkIn).grid(row=3,column=2, padx=(20,0), pady=(0,100))
        # Button kembali ke menu utama
        Button(window, text = "Kembali ke Menu Utama", font = ("Helvetica", 10, "bold"), bg="#FF595E", command = self.backToHomescreen).place(x = 75, y = 75, width=180, height=50)

    
        window.mainloop()

    # Back to home screen punya home screennya check in
    def backToHomescreen(self):
        from home import ClassHome
        ClassHome().homescreen(window)

    def showTitle(self, screen):
        Label(screen, text="myHotel",font=("helvetica",20,"bold"),bg="#F7F0F5",fg="black").grid(row=0,column=1,columnspan=2)

    def showSectionTitle(self, screen):
        Label(screen, text="Check-in",font=("helvetica",10,"bold"),bg="#F7F0F5",fg="black").grid(row=1,column=1,columnspan=2,pady=(0,100))
