import tkinter as tk
from tkinter import *

# Buat Window main
checkinWindow = tk.Tk()
checkinWindow.title("myHotel")
checkinWindow.geometry('800x450')

# Buat Entry Kolom (Buat input NIK Pelanggan)

# nik pelanggan
# nomor kamar


# Create Label and Button
title = tk.Label(checkinWindow, text = "Check In")
button1 = tk.Button(checkinWindow, text = "Booking Check In", padx=50, pady=10)
button2 = tk.Button(checkinWindow, text = "Check In Walk In",padx=50, pady=10)

title.pack()
button1.pack()
button2.pack()



# Shoving it onto the screen

checkinWindow.mainloop()