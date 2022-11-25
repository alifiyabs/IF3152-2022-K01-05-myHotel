# Check In
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
        window.config(bg="#F7F0F5")
        
        # Tampilan Judul myHotel dan Judul Check In
        self.showTitle(window)
        self.showSectionTitle(window)

        # Buka halaman Booking Check In
        def bukaBookingCheckIn():
            from bookingCheckIn import BookingCheckIn
            BookingCheckIn().BookingCheckIn(window)
        # Buka halaman Booking Walk In
        def bukaWalkIn():
            from checkInWalkIn import CheckInWalkIn
            CheckInWalkIn().checkInWalkIn(window)

        # Button bookingCheckIn menuju ke bookingCheckIn
        Button(window, text = "Booking Check In", font = ("Helvetica", 12, "bold"), bg="#DECBB7", width = 15, height = 2, command = bukaBookingCheckIn).place(x = 805, y = 220,anchor="ne")
        # Button checkInWalkIn menuju ke checkInWalkIn
        Button(window, text = "Check In Walk In", font = ("Helvetica", 12, "bold"), bg="#DECBB7", width = 15, height = 2, command = bukaWalkIn).place(x = 465, y = 220)
        # Button kembali ke menu utama
        Button(window, text = "Kembali ke Menu Utama", font = ("Helvetica", 10, "bold"), bg="#FF595E", width = 10, height = 1, command = self.backToHomescreen).place(x = 75, y = 75, width=180, height=50)
    
        window.mainloop()

    # Back to home screen punya home screennya check in
    def backToHomescreen(self):
        from home import ClassHome
        ClassHome().homescreen(window)

    def showTitle(self, screen):
        Label(screen, text="myHotel",font=("helvetica",20,"bold"),bg="#F7F0F5",fg="black").place(x=635,y=100,anchor="center")

    def showSectionTitle(self, screen):
        Label(screen, text="Check-in",font=("helvetica",10,"bold"),bg="#F7F0F5",fg="black").place(x=635,y=140,anchor="center")