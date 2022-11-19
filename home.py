import sys
import tkinter as tk
# from PIL import Image, ImageTk
import os
from tkinter import ttk
# import mysql.connector as mysql
import mariadb
from riwayat import Riwayat
from checkOut import home

def bukaRiwayat():
    Riwayat(screenhome)

def bukaCheckOut():
    home(screenhome)

def homescreen(screen):
    global screenhome
    screen.destroy()
    screenhome = tk.Tk()
    screenhome.title("myHotel")
    screenhome.geometry("1270x690")
    screenhome.configure(bg="white")
    
    #button Informasi Kamar
    InfoKamarBut = tk.Button(screenhome,text="informasi kamar").place(x=190,y=270,width=150,height=150)

    #button Check-In
    CheckInBut = tk.Button(screenhome,text="check-in").place(x=560,y=270,width=150,height=150)

    #button Check Out
    CheckOutBut = tk.Button(screenhome,text="check-out",command=bukaCheckOut).place(x=930,y=270,width=150,height=150)

    #button Riwayat Kamar
    RiwayatBut = tk.Button(screenhome,text="riwayat kamar",command=bukaRiwayat).place(x=375,y=420,width=150,height=150)
    
    #button Pemesanan Makanan
    CheckOutBut = tk.Button(screenhome,text="pemesanan makanan").place(x=745,y=420,width=150,height=150)

    screenhome.mainloop()