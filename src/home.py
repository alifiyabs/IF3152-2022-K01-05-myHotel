import sys
import tkinter as tk
# from PIL import Image, ImageTk
import os
from tkinter import ttk
# import mysql.connector as mysql
import mariadb
from riwayat import Riwayat
from checkOut import homeCheckOut
from checkIn import homeCheckIn

def bukaRiwayat():
    Riwayat(screenhome)

def bukaCheckOut():
    homeCheckOut(screenhome)

def bukaCheckIn():
    homeCheckIn(screenhome)

def bukaMenuMakanan():
    MenuMakanan(screenhome)

def bukaPemesananMakanan():
    PemesananMakanan(screenhome) 

def homescreen(screen):
    global screenhome
    screen.destroy()
    screenhome = tk.Tk()
    screenhome.title("myHotel")
    screenhome.geometry("1270x690")
    screenhome.configure(bg="#F7F0F5")
    
    MyHotellabelTitle = tk.Label(screenhome,text="myHotel",font=("helvetica",20,"bold"),bg="#F7F0F5",fg="black").place(x=635,y=100,anchor="center")
    MenuUtamalabelTitle = tk.Label(screenhome,text="Menu Utama",font=("helvetica",12,"bold"),bg="#F7F0F5",fg="black").place(x=635,y=140,anchor="center")
    
    #button Informasi Kamar
    InfoKamarBut = tk.Button(screenhome,text="Informasi Kamar",font=("helvetica",10,"bold"),bg="#DECBB7").place(x=310,y=270,width=150,height=75)

    #button Check-In
    CheckInBut = tk.Button(screenhome,text="Check-in",font=("helvetica",10,"bold"),bg="#DECBB7",command=bukaCheckIn).place(x=560,y=270,width=150,height=75)

    #button Check Out
    CheckOutBut = tk.Button(screenhome,text="Check-out",font=("helvetica",10,"bold"),bg="#DECBB7",command=bukaCheckOut).place(x=810,y=270,width=150,height=75)

    #button Riwayat Kamar
    RiwayatBut = tk.Button(screenhome,text="Riwayat Kamar",font=("helvetica",10,"bold"),bg="#DECBB7",command=bukaRiwayat).place(x=510,y=420,width=150,height=75,anchor="center")
    
    #button Menu Makanan
    menuMakananBut = tk.Button(screenhome,text="menu makanan", command=bukaMenuMakanan).place(x=560,y=420,width=150,height=150)
    
    #button Pemesanan Makanan
    CheckOutBut = tk.Button(screenhome,text="Pemesanan Makanan",font=("helvetica",10,"bold"),bg="#DECBB7").place(x=760,y=420,width=150,height=75,anchor="center")
    
    screenhome.resizable(False,False)
    screenhome.mainloop()
