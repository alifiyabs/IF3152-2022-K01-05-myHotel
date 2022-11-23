# Pencatatan Pesanan Makanan
# Penanggung jawab: Adwa Sofia 18220109

# Progress: Sudah berfungsi
# Prerequisite: Install tkinter dan mariadb (beserta seluruh library yang diperlukan)
# Prerequisite: Database mariadb dengan nama myhotel sudah ada
# Notes: Replace ***** dengan password database, serta ganti port database jika diperlukan

# Import Library
import sys
import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
from tkinter.messagebox import showinfo
import os
import mariadb
import home

class ClassPemesananMakanan():
    def __init__(roo):
        super().__init__()

    # Layar Pertama Fitur Pencatatan Pesanan Makanan
    def homePemesananMakanan(self, screen):
        screen.destroy()

        global screenPemesananMakanan
        screenPemesananMakanan = tk.Tk()
        screenPemesananMakanan.title("Pesan Makanan")
        screenPemesananMakanan.geometry('1270x690')
        screenPemesananMakanan.config(bg ="#F7F0F5")

        # Mencetak Title dan Sub-Title Halaman
        tk.Label(screenPemesananMakanan, text ="myHotel", font = ("Helvetica", 20, "bold"), bg="#F7F0F5", fg="black").place(x=575,y=40)
        tk.Label(screenPemesananMakanan, text="Pesan Makanan", font=("Helvetica", 10, "bold"), bg="#F7F0F5", fg="black", width=100, anchor="w").place(x=580,y=80)

        # Entry box Nomor Kamar yang akan Dicatat Pesanan Makanannya
        global inputNoKamar
        global nomerKamar
        nomerKamar = StringVar()
        tk.Label(screenPemesananMakanan, text="Masukkan Nomor Kamar", font = ("Helvetica", 12, "bold"), bg="#F7F0F5").place(x=525,y=200)
        inputNoKamar = tk.Entry(screenPemesananMakanan, textvariable = nomerKamar, font=("Helvetica", 12), bg="light grey", fg="black")
        inputNoKamar.place(x=545,y=240)
        tk.Label(screenPemesananMakanan, text=str(inputNoKamar.get()), font=("Helvetica", 10, "bold"), bg="white", fg="black", width=100, anchor="w").place(x=800,y=600)

        # Button untuk Melanjutkan ke Verifikasi Nomor Kamar
        btn = tk.Button(screenPemesananMakanan, text = "Pesan Makanan", font = ("Helvetica", 12, "bold"), bg="#DECBB7", width = 20, height = 1, command=self.isKamarTerisi)
        btn.place(x=588,y=280)

        screenPemesananMakanan.mainloop()

    
    def isKamarTerisi(self):
        # Membuka Koneksi dengan Database
        try:
            conn = mariadb.connect (
                user = 'root',
                password = 'sngshdcb29',
                host = 'localhost',
                port = 3307,
                database = 'myhotel'
            )
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")

        # Mengeksekusi Query Verifikasi Nomor Kamar
        cur = conn.cursor()
        try:
            statement = "SELECT nomorKamar, statusKamar FROM informasiKamar WHERE nomorKamar = %s AND statusKamar = %s"
            data = (int(nomerKamar.get()), "Unavailable",)
            cur.execute(statement, data)
            row = cur.fetchone()
            if (row == None):
                # Nomor Kamar tersebut tidak dapat Melakukan Pemesanan Makanan
                # (Kamar tidak tersedia, Kamar kosong, atau Tamu Hotel belum Check-in)
                tk.Label(screenPemesananMakanan, text = "Tidak dapat melakukan pemesanan makanan karena kamar tidak valid!", fg = "red", font = ("Helvetica, 13")).pack()
            else:
                # Nomor Kamar dapat Melakukan Pemesanan Makanan
                # Menampilkan Layar Kedua dari Fitur Pencatatan Pesanan Makanan
                self.Pesan(screenPemesananMakanan)
        except mariadb.Error as e:
            print(f"Error retrieving entry form database: {e}")
        conn.commit()

    # Layar Kedua Fitur Pencatatan Pesanan Makanan   
    def Pesan(self, screen):
        screen.destroy()
        global screenPesan

        screenPesan = tk.Tk()
        screenPesan.title("Pemesanan Makanan")
        screenPesan.geometry("1270x690")
        screenPesan.config(bg="white")

        # Mencetak Title dan Sub-Title Halaman
        tk.Label(screenPesan, text = "myHotel", font = ("Helvetica", 20, "bold"), bg="white").place(x=575,y=40)
        tk.Label(screenPesan, text="Pesan Makanan", font=("Helvetica", 10, "bold"), bg="white", fg="black", width=100, anchor="w").place(x=580,y=80)

        # Menampilkan Pilihan Menu Makanan
        pilihanMenuMakanan = Frame(screenPesan, bd=5, height=370, width=300, relief=RAISED)
        pilihanMenuMakanan.place(x=390, y=118)

        ayamgeprek = StringVar()
        ayampenyet = StringVar()
        tempe = StringVar()
        nasi = StringVar()
        sayur = StringVar()
        teh = StringVar()
        kopi = StringVar()
        total_biaya_makanan = StringVar()

        # Label Pilihan Menu Makanan
        ayamgeprek_label = Label(pilihanMenuMakanan, font=("Helvetica", 13), text="Ayam Geprek", width=12, fg="blue4")
        ayamgeprek_label.grid(row=1, column=0)
        ayampenyet_label = Label(pilihanMenuMakanan, font=("Helvetica", 13), text="Ayam Penyet", width=12, fg="blue4")
        ayampenyet_label.grid(row=2, column=0)
        tempe_label = Label(pilihanMenuMakanan, font=("Helvetica", 13), text="Tempe", width=12, fg="blue4")
        tempe_label.grid(row=3, column=0)
        nasi_label = Label(pilihanMenuMakanan, font=("Helvetica", 13), text="Nasi", width=12, fg="blue4")
        nasi_label.grid(row=4, column=0)
        sayur_label = Label(pilihanMenuMakanan, font=("Helvetica", 13), text="Sayur", width=12, fg="blue4")
        sayur_label.grid(row=5, column=0)
        teh_label = Label(pilihanMenuMakanan, font=("Helvetica", 13), text="Teh", width=12, fg="blue4")
        teh_label.grid(row=6, column=0)
        kopi_label = Label(pilihanMenuMakanan, font=("Helvetica", 13), text="Kopi", width=12, fg="blue4")
        kopi_label.grid(row=7, column=0)

        # Entry Pilihan Menu Makanan
        entry_ayamgeprek = Entry(pilihanMenuMakanan, font=('Helvetica', 13), textvariable=ayamgeprek, bd=6, width=8, bg="#8F857D")
        entry_ayamgeprek.grid(row=1, column=1)
        entry_ayampenyet = Entry(pilihanMenuMakanan, font=('Helvetica', 13), textvariable=ayampenyet, bd=6, width=8, bg='white')
        entry_ayampenyet.grid(row=2, column=1)
        entry_tempe = Entry(pilihanMenuMakanan, font=('Helvetica', 13), textvariable=tempe, bd=6, width=8, bg='white')
        entry_tempe.grid(row=3, column=1)
        entry_nasi = Entry(pilihanMenuMakanan, font=('Helvetica', 13), textvariable=nasi, bd=6, width=8, bg='white')
        entry_nasi.grid(row=4, column=1)
        entry_sayur = Entry(pilihanMenuMakanan, font=('Helvetica', 13), textvariable=sayur, bd=6, width=8, bg='white')
        entry_sayur.grid(row=5, column=1)
        entry_teh = Entry(pilihanMenuMakanan, font=('Helvetica', 13), textvariable=teh, bd=6, width=8, bg='white')
        entry_teh.grid(row=6, column=1)
        entry_kopi = Entry(pilihanMenuMakanan, font=('Helvetica', 13), textvariable=kopi, bd=6, width=8, bg='white')
        entry_kopi.grid(row=7, column=1)

        # Fungsi untuk me-reset input Kuantitas Pilihan Menu Makanan
        def Reset():
            entry_ayamgeprek.delete(0, END)
            entry_ayampenyet.delete(0, END)
            entry_tempe.delete(0, END)
            entry_nasi.delete(0, END)
            entry_sayur.delete(0, END)
            entry_teh.delete(0, END)
            entry_kopi.delete(0, END)
        
        def Total():
            try: a1 = int(ayamgeprek.get())
            except: a1=0

            try: a2 = int(ayampenyet.get())
            except: a2=0

            try: a3 = int(tempe.get())
            except: a3=0
        
            try: a4 = int(nasi.get())
            except: a4=0
        
            try: a5 = int(sayur.get())
            except: a5=0

            try: a6 = int(teh.get())
            except: a6=0
        
            try: a7 = int(kopi.get())
            except: a7=0

            # Harga makanan
            harga1 = 20000*a1
            harga2 = 20000*a2
            harga3 = 2000*a3
            harga4 = 5000*a4
            harga5 = 10000*a5
            harga6 = 3000*a6
            harga7 = 3000*a7
            
            label_total = Label(frameTotal, font=('Helvetica', 13, 'bold'), text='Total', width=16, fg='lightyellow', bg='black')
            label_total.place(x=0, y=50)

            entry_total = Entry(frameTotal, font=('Helvetica', 13, 'bold'), textvariable= total_biaya_makanan, bd=6, width=15, bg='lightgreen')
            entry_total.place(x=20, y=100)
            
            global total_harga
            total_harga = harga1+harga2+harga3+harga4+harga5+harga6+harga7
            string_harga = str(total_harga)
            total_biaya_makanan.set(string_harga)

        # Button Reset untuk me-reset input Kuantitas Pilihan Menu Makanan
        btn_reset = Button(pilihanMenuMakanan, bd=5, fg="black", bg="lightblue", font=("Helvetica", 16, "bold"), width=10, text="Reset", command=Reset)
        btn_reset.grid(row=8, column=0)

        # Button Total untuk Menampilkan Total Harga Pesanan
        btn_total = Button(pilihanMenuMakanan, bd=5, fg="black", bg="lightblue", font=("Helvetica", 16, "bold"), width=10, text="Total", command=Total)
        btn_total.grid(row=8, column=1)

        # BILL
        frameTotal = Frame(screenPesan, bg="lightyellow", width=300, height=370)
        frameTotal.place(x=690, y=118)

        # Button Pesan untuk Mengonfirmasi Pesanan
        btn = tk.Button(screenPesan, text = "Pesan", bd='2', command=self.callKonfirmasiPesanan)
        btn.place(x=820,y=355)

        # Button Batal untuk Membatalkan Pesanan
        btn = tk.Button(screenPesan, text = "Batalkan Pesanan", bd='2', command=self.homeFromPesan)
        btn.place(x=800,y=385)
        

        screenPesan.mainloop()
        
        
    # Fungsi untuk Memanggil Layar Konfirmasi Pesanan
    def callKonfirmasiPesanan(self):
        self.KonfirmasiPesanan(screenPesan)

    # Fungsi untuk Memanggil Layar Home
    def homeFromPesan(self):
        from home import ClassHome
        ClassHome().homescreen(screenPesan)
    def homeFromKonfirmasiPesanan(self):
        from home import ClassHome
        ClassHome().homescreen(screenKonfirmasiPesan)

    # Fungsi untuk Mengonfirmasi Pesanan
    def KonfirmasiPesanan(self, screen):
        global screenKonfirmasiPesan

        screen.destroy()
        screenKonfirmasiPesan = tk.Tk()
        screenKonfirmasiPesan.title("Konfirmasi Pesanan Makanan")
        screenKonfirmasiPesan.geometry("1270x690")
        screenKonfirmasiPesan.config(bg="white")

        # Mencetak Title dan Sub-Title Halaman
        tk.Label(screenKonfirmasiPesan, text = "myHotel", font = ("Helvetica", 20, "bold"), bg="white").place(x=575,y=40)
        tk.Label(screenKonfirmasiPesan, text="Detail Pesanan Makanan", font=("Helvetica", 10, "bold"), bg="white", fg="black", width=100, anchor="w").place(x=580,y=80)

        # Button Pesan untuk Mengonfirmasi Pesanan
        btn = tk.Button(screenKonfirmasiPesan, text = "Lanjutkan Pesan", bd='2', command=self.addTotalTagihan)
        btn.place(x=820,y=355)

        # Button Batal untuk Membatalkan Pesanan
        btn = tk.Button(screenKonfirmasiPesan, text = "Batalkan Pesanan", bd='2', command=self.homeFromKonfirmasiPesanan)
        btn.place(x=800,y=385)

        # Membuka Koneksi dengan Database
        try:
            conn = mariadb.connect (
                user = 'root',
                password = 'sngshdcb29',
                host = 'localhost',
                port = 3307,
                database = 'myhotel'
            )
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")

        # Mengeksekusi Query
        cur = conn.cursor()
        try:
            statement = "SELECT nomorKamar, namaPengunjung FROM informasiTamuHotel WHERE nomorKamar = %s AND statusPengunjung = %s"
            data = (int(nomerKamar.get()), "Check-in",)
            cur.execute(statement, data)
            
            row = cur.fetchone()
            if (row == None):
                tk.Label(screenKonfirmasiPesan, text = "Tidak dapat melakukan pemesanan makanan karena kamar tidak valid!", fg = "red", font = ("Helvetica, 13")).pack()
            else:
                noKamarDB = row[0]
                namaPengunjungDB = row[1]
                
                tk.Label(screenKonfirmasiPesan, text="Nomor Kamar:", font=("Helvetica", 15), bg="white", fg="black", width=100, anchor="w").place(x=325,y=200)
                tk.Label(screenKonfirmasiPesan, text=noKamarDB, font=("Helvetica", 15), bg="white", fg="black", width=100, anchor="w").place(x=500,y=200)
                tk.Label(screenKonfirmasiPesan, text="Nama Pengunjung:", font=("Helvetica", 15), bg="white", fg="black", width=100, anchor="w").place(x=325,y=300)
                tk.Label(screenKonfirmasiPesan, text=namaPengunjungDB, font=("Helvetica", 15), bg="white", fg="black", width=100, anchor="w").place(x=500,y=300)
                tk.Label(screenKonfirmasiPesan, text="Harga Pesanan:", font=("Helvetica", 15), bg="white", fg="black", width=100, anchor="w").place(x=325,y=600)
                tk.Label(screenKonfirmasiPesan, text=total_harga, font=("Helvetica", 15), bg="white", fg="black", width=100, anchor="w").place(x=500,y=600)
            
        except mariadb.Error as e:
            print(f"Error retrieving entry from database: {e}")
        
    # Fungsi untuk Menambahkan Harga Total Pesanan ke Tagihan Tamu Hotel tersebut di Database
    def addTotalTagihan(self):
        # Membuka Koneksi dengan Database
        try:
            conn = mariadb.connect (
                user = 'root',
                password = 'sngshdcb29',
                host = 'localhost',
                port = 3307,
                database = 'myhotel'
            )
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            #databaseFail(screen)
        
        # Mengeksekusi Query
        cur = conn.cursor()
        try:
            statement = "SELECT nomorKamar, namaPengunjung, totalTagihan FROM informasiTamuHotel WHERE nomorKamar = %s AND statusPengunjung = %s"
            data = (int(nomerKamar.get()), "Check-in",)
            cur.execute(statement, data)
            
            row = cur.fetchone()
            if (row == None):
                tk.Label(screenKonfirmasiPesan, text = "Tidak dapat melakukan pemesanan makanan karena kamar tidak valid!", fg = "red", font = ("Helvetica, 13")).pack()
            else:
                noKamarDB = row[0]
                namaPengunjungDB = row[1]
                tagihanDB = row[2]
        except mariadb.Error as e:
            print(f"Error retrieving entry from database: {e}")
        tagihanAkhir = tagihanDB + int(total_harga)
        cur = conn.cursor()
        try:
            statement = "UPDATE informasiTamuHotel SET totalTagihan = %s WHERE nomorKamar = %s AND statusPengunjung = %s"

            data = (int(tagihanAkhir), int(nomerKamar.get()), "Check-in",)
            cur.execute(statement, data)
            self.PesananTercatat(screenKonfirmasiPesan)
        except mariadb.Error as e:
            print(f"Error retrieving entry from database: {e}")  
                
        conn.commit()

    def PesananTercatat(self, screen):
        global screenPesananTercatat

        screen.destroy()
        screenPesananTercatat = tk.Tk()
        screenPesananTercatat.title("Konfirmasi Pesanan Makanan")
        screenPesananTercatat.geometry("1270x690")
        screenPesananTercatat.config(bg="white")

        tk.Label(screenPesananTercatat, text = "Pesanan telah ditambahkan ke tagihan tamu hotel.", font = ("Helvetica", 12, "bold"), bg="white").place(x=105,y=40)

        # Button Batal untuk Kembali ke Home
        btn = tk.Button(screenPesananTercatat, text = "Kembali ke Menu Utama", bd='2', command=self.homeFromPesananTercatat)
        btn.place(x=800,y=385)

    def homeFromPesananTercatat(self):
        from home import ClassHome
        ClassHome().homescreen(screenPesananTercatat)
