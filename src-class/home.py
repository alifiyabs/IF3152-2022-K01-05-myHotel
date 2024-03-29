import sys
import tkinter as tk
import os
from tkinter import ttk
import mariadb
from riwayat import ClassRiwayat
from checkOut import ClassCheckOut
from checkIn import ClassCheckIn
from infoKamar import ClassInfoKamar
from menuMakanan import ClassMenuMakanan
from pemesananMakanan import ClassPemesananMakanan

class ClassHome():
    def bukaRiwayat(self):
        riwayat_var = ClassRiwayat()
        riwayat_var.Riwayat(screenhome)

    def bukaCheckOut(self):
        checkout_var = ClassCheckOut()
        checkout_var.homeCheckOut(screenhome)

    def bukaCheckIn(self):
        checkin_var = ClassCheckIn()
        checkin_var.homeCheckIn(screenhome)

    def bukaInfoKamar(self):
        infokamar_var = ClassInfoKamar()
        infokamar_var.Infokamar(screenhome)

    def bukaMenuMakanan(self):
        menuMakanan_var = ClassMenuMakanan()
        menuMakanan_var.homeMenuMakanan(screenhome)

    def bukaPemesananMakanan(self):
        pemesanan_var = ClassPemesananMakanan()
        pemesanan_var.homePemesananMakanan(screenhome)

    def homescreen(self, screen):
        global screenhome
        screen.destroy()
        screenhome = tk.Tk()
        screenhome.title("myHotel")
        screenhome.geometry("1270x690")
        screenhome.configure(bg="#F7F0F5")
        
        MyHotellabelTitle = tk.Label(screenhome,text="myHotel",font=("helvetica",20,"bold"),bg="#F7F0F5",fg="black").place(x=635,y=100,anchor="center")
        MenuUtamalabelTitle = tk.Label(screenhome,text="Menu Utama",font=("helvetica",12,"bold"),bg="#F7F0F5",fg="black").place(x=635,y=140,anchor="center")
        
        #button Informasi Kamar
        InfoKamarBut = tk.Button(screenhome,text="Informasi Kamar",font=("helvetica",10,"bold"),bg="#DECBB7",command=self.bukaInfoKamar).place(x=310,y=270,width=150,height=75)

        #button Check-In
        CheckInBut = tk.Button(screenhome,text="Check-in",font=("helvetica",10,"bold"),bg="#DECBB7",command=self.bukaCheckIn).place(x=560,y=270,width=150,height=75)

        #button Check Out
        CheckOutBut = tk.Button(screenhome,text="Check-out",font=("helvetica",10,"bold"),bg="#DECBB7",command=self.bukaCheckOut).place(x=810,y=270,width=150,height=75)

        #button Riwayat Kamar
        RiwayatBut = tk.Button(screenhome,text="Riwayat Kamar",font=("helvetica",10,"bold"),bg="#DECBB7",command=self.bukaRiwayat).place(x=310,y=400,width=150,height=75)
        
        #button Menu Makanan
        menuMakananBut = tk.Button(screenhome, text="Menu Makanan", font=("helvetica",10,"bold"), bg="#DECBB7", command=self.bukaMenuMakanan).place(x=560,y=400,width=150,height=75)

        #button Pemesanan Makanan
        pemesananMakananBut = tk.Button(screenhome, text="Pemesanan Makanan", font=("helvetica",10,"bold"), bg="#DECBB7", command=self.bukaPemesananMakanan).place(x=810,y=400,width=150,height=75)

        screenhome.resizable(False,False)
        screenhome.mainloop()
