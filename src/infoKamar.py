# Informasi Kamar
# Penanggung jawab: Joe Putera 18217035

# Prerequisite: Library tkinter, mariadb
# Prerequisite: Database mariadb dengan nama myhotel
# Notes: Replace ***** dengan password database mariadb (ada 4 field password)

import sys
import tkinter as tk
import os
from tkinter import ttk
import mariadb
from riwayat import Riwayat
from checkOut import homeCheckOut

def kamarSingle():
    pageSingle(screenhome)

def kamarDouble():
    pageDouble(screenhome)

def kamarDeluxe():
    pageDeluxe(screenhome)

def kembaliHome():
        from home import homescreen
        homescreen(screenhome)

def Infokamar(screen):
    global screenhome
    screen.destroy()
    screenhome = tk.Tk()
    screenhome.title("Informasi Kamar")
    screenhome.geometry("1270x690")
    screenhome.configure(bg="white")

    MyHotellabelTitle = tk.Label(screenhome,text="myHotel",font=("helvetica",20,"bold"),bg="white",fg="black",width=100,anchor='w').place(x=550,y=100)
    MenuUtamalabelTitle = tk.Label(screenhome,text="Menu Utama",font=("helvetica",10,"bold"),bg="white",fg="black",width=100,anchor='w').place(x=560,y=140)
    PageTitle = tk.Label(screenhome,text="Informasi Kamar",font=("helvetica",20,"bold"),bg="white",fg="black",width=100,anchor='w').place(x=500,y=180)

    #Single room button
    SingleButton = tk.Button(screenhome,text="Single", command=kamarSingle).place(x=190,y=350,width=150,height=150)

    #Double room button
    DoubleButton = tk.Button(screenhome,text="Double", command=kamarDouble).place(x=550,y=350,width=150,height=150)

    #Deluxe room button
    DeluxeButton = tk.Button(screenhome,text="Deluxe", command=kamarDeluxe).place(x=930,y=350,width=150,height=150)

    #Display back to home button
    KembaliBut = tk.Button(screenhome,text="Kembali ke Menu Utama",command=kembaliHome).place(x=99,y=550,width=180,height=49)

    screenhome.mainloop()

def pageSingle(screen):
    global screenhome
    screen.destroy()
    screenhome = tk.Tk()
    screenhome.title("kamar Single")
    screenhome.geometry("1270x690")
    screenhome.configure(bg="white")

    #Connect to database
    try:
        conn = mariadb.connect(
            user='root',
            password='admin',
            host='localhost',
            database='myhotel'
        )
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)
    
    cursor = conn.cursor()
    
    #Single page heading
    MyHotellabelTitle = tk.Label(screenhome,text="myHotel",font=("helvetica",20,"bold"),bg="white",fg="black",width=100,anchor='w').place(x=550,y=100)
    MenuUtamalabelTitle = tk.Label(screenhome,text="Menu Utama",font=("helvetica",10,"bold"),bg="white",fg="black",width=100,anchor='w').place(x=560,y=140)
    SingleHeading = tk.Label(screenhome,text="Tipe Single",font=("helvetica",20,"bold"),bg="white",fg="black",width=100,anchor='w').place(x=120,y=160)

    #SQL command to fetch luasKamar
    cursor.execute('SELECT * FROM informasikamar WHERE tipeKamar = "Single" LIMIT 1')
    retval = cursor.fetchone()[2]
    
    #Display luasKamar
    LuasKamar = tk.Label(screenhome,text="Luas Kamar",font=("helvetica",14,),bg="white",fg="black",width=100,anchor='w').place(x=125,y=200)
    ValueLuasKamar = tk.Label(screenhome,text=retval,font=("helvetica",12,),bg="white",fg="black",width=100,anchor='w').place(x=125,y=230)

    #SQL command to fetch fasilitas
    cursor.execute('SELECT * FROM informasikamar WHERE tipeKamar = "Single" LIMIT 1')
    retval = cursor.fetchone()[3]

    #Display fasilitas
    Fasilitas = tk.Label(screenhome,text="Fasilitas Kamar",font=("helvetica",14,),bg="white",fg="black",width=100,anchor='w').place(x=125,y=270)
    ValueFasilitas = tk.Label(screenhome,text=retval,font=("helvetica",12,),bg="white",fg="black",width=100,anchor='w').place(x=125,y=300)

    #SQL command to fetch harga
    cursor.execute('SELECT * FROM informasikamar WHERE tipeKamar = "Single" LIMIT 1')
    retval = cursor.fetchone()[4]

    #Display harga
    Harga = tk.Label(screenhome,text="Harga Per Malam",font=("helvetica",14,),bg="white",fg="black",width=100,anchor='w').place(x=125,y=340)
    ValueHarga = tk.Label(screenhome,text=("Rp",retval),font=("helvetica",12,),bg="white",fg="black",width=100,anchor='w').place(x=125,y=370)

    #SQL command to fetch nomorKamar
    cursor.execute('SELECT * FROM informasikamar WHERE tipeKamar = "Single" ')
    retval = cursor.fetchall()

    #Convert query result into list
    i = 0
    arrayNo =[]
    while(i <len(retval)):
        arrayNo.append(retval[i][0])
        i += 1

    #Display nomorKamar
    NomorKamar = tk.Label(screenhome,text="Nomor Kamar Tipe Ini",font=("helvetica",14,),bg="white",fg="black",width=100,anchor='w').place(x=125,y=410)
    ValueNomorKamar = tk.Label(screenhome,text=(list(arrayNo)),font=("helvetica",12,),bg="white",fg="black",width=100,anchor='w').place(x=125,y=440)

    #Close DB connection
    conn.close()

    #Display back to home button
    KembaliBut = tk.Button(screenhome,text="Kembali ke Menu Utama",command=kembaliHome).place(x=99,y=550,width=180,height=49)

    screenhome.mainloop()

def pageDouble(screen):
    global screenhome
    screen.destroy()
    screenhome = tk.Tk()
    screenhome.title("kamar Double")
    screenhome.geometry("1270x690")
    screenhome.configure(bg="white")

    #Connect to database
    try:
        conn = mariadb.connect(
            user='root',
            password='*****',
            host='localhost',
            database='myhotel'
        )
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)
    
    cursor = conn.cursor()
    
    #Double page heading
    MyHotellabelTitle = tk.Label(screenhome,text="myHotel",font=("helvetica",20,"bold"),bg="white",fg="black",width=100,anchor='w').place(x=550,y=100)
    MenuUtamalabelTitle = tk.Label(screenhome,text="Menu Utama",font=("helvetica",10,"bold"),bg="white",fg="black",width=100,anchor='w').place(x=560,y=140)
    DoubleHeading = tk.Label(screenhome,text="Tipe Double",font=("helvetica",20,"bold"),bg="white",fg="black",width=100,anchor='w').place(x=120,y=160)

    #SQL command to fetch luasKamar
    cursor.execute('SELECT * FROM informasikamar WHERE tipeKamar = "Double" LIMIT 1')
    retval = cursor.fetchone()[2]
    
    #Display luasKamar
    LuasKamar = tk.Label(screenhome,text="Luas Kamar",font=("helvetica",14,),bg="white",fg="black",width=100,anchor='w').place(x=125,y=200)
    ValueLuasKamar = tk.Label(screenhome,text=retval,font=("helvetica",12,),bg="white",fg="black",width=100,anchor='w').place(x=125,y=230)

    #SQL command to fetch fasilitas
    cursor.execute('SELECT * FROM informasikamar WHERE tipeKamar = "Double" LIMIT 1')
    retval = cursor.fetchone()[3]

    #Display fasilitas
    Fasilitas = tk.Label(screenhome,text="Fasilitas Kamar",font=("helvetica",14,),bg="white",fg="black",width=100,anchor='w').place(x=125,y=270)
    ValueFasilitas = tk.Label(screenhome,text=retval,font=("helvetica",12,),bg="white",fg="black",width=100,anchor='w').place(x=125,y=300)

    #SQL command to fetch harga
    cursor.execute('SELECT * FROM informasikamar WHERE tipeKamar = "Double" LIMIT 1')
    retval = cursor.fetchone()[4]

    #Display harga
    Harga = tk.Label(screenhome,text="Harga Per Malam",font=("helvetica",14,),bg="white",fg="black",width=100,anchor='w').place(x=125,y=340)
    ValueHarga = tk.Label(screenhome,text=("Rp",retval),font=("helvetica",12,),bg="white",fg="black",width=100,anchor='w').place(x=125,y=370)

    #SQL command to fetch nomorKamar
    cursor.execute('SELECT * FROM informasikamar WHERE tipeKamar = "Double" ')
    retval = cursor.fetchall()

    #Convert query result into list
    i = 0
    arrayNo =[]
    while(i <len(retval)):
        arrayNo.append(retval[i][0])
        i += 1

    #Display nomorKamar
    NomorKamar = tk.Label(screenhome,text="Nomor Kamar Tipe Ini",font=("helvetica",14,),bg="white",fg="black",width=100,anchor='w').place(x=125,y=410)
    ValueNomorKamar = tk.Label(screenhome,text=(list(arrayNo)),font=("helvetica",12,),bg="white",fg="black",width=100,anchor='w').place(x=125,y=440)

    #Close DB connection
    conn.close()

    #Display back to home button
    KembaliBut = tk.Button(screenhome,text="Kembali ke Menu Utama",command=kembaliHome).place(x=99,y=550,width=180,height=49)

    screenhome.mainloop()

def pageDeluxe(screen):
    global screenhome
    screen.destroy()
    screenhome = tk.Tk()
    screenhome.title("kamar Deluxe")
    screenhome.geometry("1270x690")
    screenhome.configure(bg="white")

    #Connect to database
    try:
        conn = mariadb.connect(
            user='root',
            password='admin',
            host='localhost',
            database='myhotel'
        )
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)
    
    cursor = conn.cursor()
    
    #Deluxe page heading
    MyHotellabelTitle = tk.Label(screenhome,text="myHotel",font=("helvetica",20,"bold"),bg="white",fg="black",width=100,anchor='w').place(x=550,y=100)
    MenuUtamalabelTitle = tk.Label(screenhome,text="Menu Utama",font=("helvetica",10,"bold"),bg="white",fg="black",width=100,anchor='w').place(x=560,y=140)
    DeluxeHeading = tk.Label(screenhome,text="Tipe Deluxe",font=("helvetica",20,"bold"),bg="white",fg="black",width=100,anchor='w').place(x=120,y=160)

    #SQL command to fetch luasKamar
    cursor.execute('SELECT * FROM informasikamar WHERE tipeKamar = "Deluxe" LIMIT 1')
    retval = cursor.fetchone()[2]
    
    #Display luasKamar
    LuasKamar = tk.Label(screenhome,text="Luas Kamar",font=("helvetica",14,),bg="white",fg="black",width=100,anchor='w').place(x=125,y=200)
    ValueLuasKamar = tk.Label(screenhome,text=retval,font=("helvetica",12,),bg="white",fg="black",width=100,anchor='w').place(x=125,y=230)

    #SQL command to fetch fasilitas
    cursor.execute('SELECT * FROM informasikamar WHERE tipeKamar = "Deluxe" LIMIT 1')
    retval = cursor.fetchone()[3]

    #Display fasilitas
    Fasilitas = tk.Label(screenhome,text="Fasilitas Kamar",font=("helvetica",14,),bg="white",fg="black",width=100,anchor='w').place(x=125,y=270)
    ValueFasilitas = tk.Label(screenhome,text=retval,font=("helvetica",12,),bg="white",fg="black",width=100,anchor='w').place(x=125,y=300)

    #SQL command to fetch harga
    cursor.execute('SELECT * FROM informasikamar WHERE tipeKamar = "Deluxe" LIMIT 1')
    retval = cursor.fetchone()[4]

    #Display harga
    Harga = tk.Label(screenhome,text="Harga Per Malam",font=("helvetica",14,),bg="white",fg="black",width=100,anchor='w').place(x=125,y=340)
    ValueHarga = tk.Label(screenhome,text=("Rp",retval),font=("helvetica",12,),bg="white",fg="black",width=100,anchor='w').place(x=125,y=370)

    #SQL command to fetch nomorKamar
    cursor.execute('SELECT * FROM informasikamar WHERE tipeKamar = "Deluxe" ')
    retval = cursor.fetchall()

    #Convert query result into list
    i = 0
    arrayNo =[]
    while(i <len(retval)):
        arrayNo.append(retval[i][0])
        i += 1

    #Display nomorKamar
    NomorKamar = tk.Label(screenhome,text="Nomor Kamar Tipe Ini",font=("helvetica",14,),bg="white",fg="black",width=100,anchor='w').place(x=125,y=410)
    ValueNomorKamar = tk.Label(screenhome,text=(list(arrayNo)),font=("helvetica",12,),bg="white",fg="black",width=100,anchor='w').place(x=125,y=440)

    #Close DB connection
    conn.close()

    #Display back to home button
    KembaliBut = tk.Button(screenhome,text="Kembali ke Menu Utama",command=kembaliHome).place(x=99,y=550,width=180,height=49)

    screenhome.mainloop()
