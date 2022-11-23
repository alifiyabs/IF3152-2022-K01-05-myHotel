# Informasi Kamar
# Penanggung jawab: Joe Putera 18217035

# Prerequisite: Library tkinter, mariadb
# Prerequisite: Database mariadb dengan nama myhotel
# Notes: Replace ***** dengan password database mariadb (ada 3 field password)

import sys
import tkinter as tk
import os
from tkinter import ttk
import mariadb
from riwayat import ClassRiwayat
from checkOut import ClassCheckOut

class ClassInfoKamar():
    def kamarSingle(self):
        self.pageSingle(screenhome)

    def kamarDouble(self):
        self.pageDouble(screenhome)

    def kamarDeluxe(self):
        self.pageDeluxe(screenhome)

    def kembaliHome(self):
            from home import ClassHome
            ClassHome().homescreen(screenhome)

    def Infokamar(self, screen):
        global screenhome
        screen.destroy()
        screenhome = tk.Tk()
        screenhome.title("Informasi Kamar")
        screenhome.geometry("1270x690")
        screenhome.configure(bg="#F7F0F5")

        MyHotellabelTitle = tk.Label(screenhome,text="myHotel",font=("helvetica",20,"bold"),bg="#F7F0F5",fg="black").place(x=635,y=100,anchor="center")
        RiwayatlabelTitle = tk.Label(screenhome,text="Informasi Kamar",font=("helvetica",10,"bold"),bg="#F7F0F5",fg="black").place(x=635,y=140,anchor="center")

        #Single room button
        SingleButton = tk.Button(screenhome,text="Single", command=self.kamarSingle, bg="#DECBB7", font = ("Helvetica", 10, "bold")).place(x=385,y=350,width=150,height=75,anchor="n")

        #Double room button
        DoubleButton = tk.Button(screenhome,text="Double", command=self.kamarDouble, bg="#DECBB7", font = ("Helvetica", 10, "bold")).place(x=635,y=350,width=150,height=75,anchor="n")

        #Deluxe room button
        DeluxeButton = tk.Button(screenhome,text="Deluxe", command=self.kamarDeluxe, bg="#DECBB7", font = ("Helvetica", 10, "bold")).place(x=885,y=350,width=150,height=75,anchor="n")

        #Display back to home button
        KembaliBut = tk.Button(screenhome,text="Kembali ke Menu Utama",command=self.kembaliHome,bg="#FF595E", font = ("Helvetica", 10, "bold")).place(x = 75, y = 75, width=180, height=50)

        screenhome.mainloop()

    def pageSingle(self, screen):
        global screenhome
        screen.destroy()
        screenhome = tk.Tk()
        screenhome.title("kamar Single")
        screenhome.geometry("1270x690")
        screenhome.configure(bg="#F7F0F5")

        def kembali():
            self.Infokamar(screenhome)

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
        
        #Single page heading
        MyHotellabelTitle = tk.Label(screenhome,text="myHotel",font=("helvetica",20,"bold"),bg="#F7F0F5",fg="black").place(x=635,y=100,anchor="center")
        RiwayatlabelTitle = tk.Label(screenhome,text="Informasi Kamar",font=("helvetica",10,"bold"),bg="#F7F0F5",fg="black").place(x=635,y=140,anchor="center")
        TipelabelTitle = tk.Label(screenhome,text="Tipe Single",font=("helvetica",10,"bold"),bg="#F7F0F5",fg="black").place(x=635,y=160,anchor="center")

        #SQL command to fetch luasKamar
        cursor.execute('SELECT * FROM informasikamar WHERE tipeKamar = "Single" LIMIT 1')
        retval = cursor.fetchone()[2]
        
        #Display luasKamar
        LuasKamar = tk.Label(screenhome,text="Luas Kamar",font=("helvetica",14,),bg="#F7F0F5",fg="black",width=100,anchor='w').place(x=125,y=200)
        ValueLuasKamar = tk.Label(screenhome,text=retval,font=("helvetica",12,),bg="#F7F0F5",fg="black",width=100,anchor='w').place(x=125,y=230)

        #SQL command to fetch fasilitas
        cursor.execute('SELECT * FROM informasikamar WHERE tipeKamar = "Single" LIMIT 1')
        retval = cursor.fetchone()[3]

        #Display fasilitas
        Fasilitas = tk.Label(screenhome,text="Fasilitas Kamar",font=("helvetica",14,),bg="#F7F0F5",fg="black",width=100,anchor='w').place(x=125,y=270)
        ValueFasilitas = tk.Label(screenhome,text=retval,font=("helvetica",12,),bg="#F7F0F5",fg="black",width=100,anchor='w').place(x=125,y=300)

        #SQL command to fetch harga
        cursor.execute('SELECT * FROM informasikamar WHERE tipeKamar = "Single" LIMIT 1')
        retval = cursor.fetchone()[4]

        #Display harga
        Harga = tk.Label(screenhome,text="Harga Per Malam",font=("helvetica",14,),bg="#F7F0F5",fg="black",width=100,anchor='w').place(x=125,y=340)
        ValueHarga = tk.Label(screenhome,text=("Rp",retval),font=("helvetica",12,),bg="#F7F0F5",fg="black",width=100,anchor='w').place(x=125,y=370)

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
        NomorKamar = tk.Label(screenhome,text="Nomor Kamar Tipe Ini",font=("helvetica",14,),bg="#F7F0F5",fg="black",width=100,anchor='w').place(x=125,y=410)
        ValueNomorKamar = tk.Label(screenhome,text=(list(arrayNo)),font=("helvetica",12,),bg="#F7F0F5",fg="black",width=100,anchor='w').place(x=125,y=440)

        #Close DB connection
        conn.close()

        #Display back to home button
        KembaliBut = tk.Button(screenhome,text="Kembali",command=kembali,bg="#FF595E", font = ("Helvetica", 10, "bold")).place(x = 75, y = 75, width=180, height=50)

        screenhome.mainloop()

    def pageDouble(self, screen):
        global screenhome
        screen.destroy()
        screenhome = tk.Tk()
        screenhome.title("kamar Double")
        screenhome.geometry("1270x690")
        screenhome.configure(bg="#F7F0F5")
        
        def kembali():
            self.Infokamar(screenhome)

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
        MyHotellabelTitle = tk.Label(screenhome,text="myHotel",font=("helvetica",20,"bold"),bg="#F7F0F5",fg="black").place(x=635,y=100,anchor="center")
        RiwayatlabelTitle = tk.Label(screenhome,text="Informasi Kamar",font=("helvetica",10,"bold"),bg="#F7F0F5",fg="black").place(x=635,y=140,anchor="center")
        TipelabelTitle = tk.Label(screenhome,text="Tipe Double",font=("helvetica",10,"bold"),bg="#F7F0F5",fg="black").place(x=635,y=160,anchor="center")

        #SQL command to fetch luasKamar
        cursor.execute('SELECT * FROM informasikamar WHERE tipeKamar = "Double" LIMIT 1')
        retval = cursor.fetchone()[2]
        
        #Display luasKamar
        LuasKamar = tk.Label(screenhome,text="Luas Kamar",font=("helvetica",14,),bg="#F7F0F5",fg="black",width=100,anchor='w').place(x=125,y=200)
        ValueLuasKamar = tk.Label(screenhome,text=retval,font=("helvetica",12,),bg="#F7F0F5",fg="black",width=100,anchor='w').place(x=125,y=230)

        #SQL command to fetch fasilitas
        cursor.execute('SELECT * FROM informasikamar WHERE tipeKamar = "Double" LIMIT 1')
        retval = cursor.fetchone()[3]

        #Display fasilitas
        Fasilitas = tk.Label(screenhome,text="Fasilitas Kamar",font=("helvetica",14,),bg="#F7F0F5",fg="black",width=100,anchor='w').place(x=125,y=270)
        ValueFasilitas = tk.Label(screenhome,text=retval,font=("helvetica",12,),bg="#F7F0F5",fg="black",width=100,anchor='w').place(x=125,y=300)

        #SQL command to fetch harga
        cursor.execute('SELECT * FROM informasikamar WHERE tipeKamar = "Double" LIMIT 1')
        retval = cursor.fetchone()[4]

        #Display harga
        Harga = tk.Label(screenhome,text="Harga Per Malam",font=("helvetica",14,),bg="#F7F0F5",fg="black",width=100,anchor='w').place(x=125,y=340)
        ValueHarga = tk.Label(screenhome,text=("Rp",retval),font=("helvetica",12,),bg="#F7F0F5",fg="black",width=100,anchor='w').place(x=125,y=370)

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
        NomorKamar = tk.Label(screenhome,text="Nomor Kamar Tipe Ini",font=("helvetica",14,),bg="#F7F0F5",fg="black",width=100,anchor='w').place(x=125,y=410)
        ValueNomorKamar = tk.Label(screenhome,text=(list(arrayNo)),font=("helvetica",12,),bg="#F7F0F5",fg="black",width=100,anchor='w').place(x=125,y=440)

        #Close DB connection
        conn.close()

        #Display back to home button
        KembaliBut = tk.Button(screenhome,text="Kembali",command=kembali,bg="#FF595E", font = ("Helvetica", 10, "bold")).place(x = 75, y = 75, width=180, height=50)

        screenhome.mainloop()

    def pageDeluxe(self, screen):
        global screenhome
        screen.destroy()
        screenhome = tk.Tk()
        screenhome.title("kamar Deluxe")
        screenhome.geometry("1270x690")
        screenhome.configure(bg="#F7F0F5")

        def kembali():
            self.Infokamar(screenhome)

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
        
        #Deluxe page heading
        MyHotellabelTitle = tk.Label(screenhome,text="myHotel",font=("helvetica",20,"bold"),bg="#F7F0F5",fg="black").place(x=635,y=100,anchor="center")
        RiwayatlabelTitle = tk.Label(screenhome,text="Informasi Kamar",font=("helvetica",10,"bold"),bg="#F7F0F5",fg="black").place(x=635,y=140,anchor="center")
        TipelabelTitle = tk.Label(screenhome,text="Tipe Deluxe",font=("helvetica",10,"bold"),bg="#F7F0F5",fg="black").place(x=635,y=160,anchor="center")

        #SQL command to fetch luasKamar
        cursor.execute('SELECT * FROM informasikamar WHERE tipeKamar = "Deluxe" LIMIT 1')
        retval = cursor.fetchone()[2]
        
        #Display luasKamar
        LuasKamar = tk.Label(screenhome,text="Luas Kamar",font=("helvetica",14,),bg="#F7F0F5",fg="black",width=100,anchor='w').place(x=125,y=200)
        ValueLuasKamar = tk.Label(screenhome,text=retval,font=("helvetica",12,),bg="#F7F0F5",fg="black",width=100,anchor='w').place(x=125,y=230)

        #SQL command to fetch fasilitas
        cursor.execute('SELECT * FROM informasikamar WHERE tipeKamar = "Deluxe" LIMIT 1')
        retval = cursor.fetchone()[3]

        #Display fasilitas
        Fasilitas = tk.Label(screenhome,text="Fasilitas Kamar",font=("helvetica",14,),bg="#F7F0F5",fg="black",width=100,anchor='w').place(x=125,y=270)
        ValueFasilitas = tk.Label(screenhome,text=retval,font=("helvetica",12,),bg="#F7F0F5",fg="black",width=100,anchor='w').place(x=125,y=300)

        #SQL command to fetch harga
        cursor.execute('SELECT * FROM informasikamar WHERE tipeKamar = "Deluxe" LIMIT 1')
        retval = cursor.fetchone()[4]

        #Display harga
        Harga = tk.Label(screenhome,text="Harga Per Malam",font=("helvetica",14,),bg="#F7F0F5",fg="black",width=100,anchor='w').place(x=125,y=340)
        ValueHarga = tk.Label(screenhome,text=("Rp",retval),font=("helvetica",12,),bg="#F7F0F5",fg="black",width=100,anchor='w').place(x=125,y=370)

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
        NomorKamar = tk.Label(screenhome,text="Nomor Kamar Tipe Ini",font=("helvetica",14,),bg="#F7F0F5",fg="black",width=100,anchor='w').place(x=125,y=410)
        ValueNomorKamar = tk.Label(screenhome,text=(list(arrayNo)),font=("helvetica",12,),bg="#F7F0F5",fg="black",width=100,anchor='w').place(x=125,y=440)

        #Close DB connection
        conn.close()

        #Display back to home button
        KembaliBut = tk.Button(screenhome,text="Kembali",command=kembali,bg="#FF595E", font = ("Helvetica", 10, "bold")).place(x = 75, y = 75, width=180, height=50)

        screenhome.mainloop()
