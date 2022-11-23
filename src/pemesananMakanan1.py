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

# Layar Pertama Fitur Pencatatan Pesanan Makanan
def PemesananMakanan(screen):
    screen.destroy()

    global screenPemesananMakanan
    screenPemesananMakanan = tk.Tk()
    screenPemesananMakanan.title("Pesan Makanan")
    screenPemesananMakanan.geometry('1270x690')
    screenPemesananMakanan.config(bg = "white")

    # Mencetak Title dan Sub-Title Halaman
    tk.Label(screenPemesananMakanan, text ="myHotel", font = ("Helvetica", 20, "bold"), bg="white").place(x=575,y=40)
    tk.Label(screenPemesananMakanan, text="Pesan Makanan", font=("Helvetica", 10, "bold"), bg="white", fg="black", width=100, anchor="w").place(x=580,y=80)

    # Entry box Nomor Kamar yang akan Dicatat Pesanan Makanannya
    global inputNoKamar
    global nomerKamar
    nomerKamar = StringVar()
    tk.Label(screenPemesananMakanan, text="Masukkan Nomor Kamar", font=("Helvetica", 15), bg="white", fg="black", width=100, anchor="w").place(x=525,y=200)
    inputNoKamar = tk.Entry(screenPemesananMakanan, textvariable = nomerKamar, font=("Helvetica", 12), bg="light grey", fg="black")
    inputNoKamar.place(x=545,y=240)
    tk.Label(screenPemesananMakanan, text=str(inputNoKamar.get()), font=("Helvetica", 10, "bold"), bg="white", fg="black", width=100, anchor="w").place(x=800,y=600)

    # Button untuk Melanjutkan ke Verifikasi Nomor Kamar
    btn = tk.Button(screenPemesananMakanan, text = "Pesan Makanan", bd='2', command=isKamarTerisi)
    btn.place(x=588,y=280)

    screenPemesananMakanan.mainloop()

    
def isKamarTerisi():
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
            Pesan(screenPemesananMakanan)
    except mariadb.Error as e:
        print(f"Error retrieving entry form database: {e}")
    conn.commit()

# Layar Kedua Fitur Pencatatan Pesanan Makanan   
def Pesan(screen):
    screen.destroy()
    global screenPesan

    screenPesan = tk.Tk()
    screenPesan.title("Pemesanan Makanan")
    screenPesan.geometry("1270x690")
    screenPesan.config(bg="white")

    # Mencetak Title dan Sub-Title Halaman
    tk.Label(screenPesan, text = "myHotel", font = ("Helvetica", 20, "bold"), bg="white").place(x=575,y=40)
    tk.Label(screenPesan, text="Pesan Makanan", font=("Helvetica", 10, "bold"), bg="white", fg="black", width=100, anchor="w").place(x=580,y=80)

    # Menampilkan Daftar Menu Makanan menggunakan Tabel
    # Mendefinisikan Kolom-Kolom Tabel
    columns = ('no', 'id_makanan', 'nama', 'harga')

    tree = ttk.Treeview(screenPesan, height=8, columns=columns, show='headings')
    tree.place(x=300,y=200)

    # Mendefinisikan Headings
    tree.heading('no', text='No')
    tree.heading('id_makanan', text='ID Makanan')
    tree.heading('nama', text='Nama')
    tree.heading('harga', text='Harga')

    tree.column('no', width=30, anchor=tk.CENTER)
    tree.column('id_makanan', width=80, anchor=tk.CENTER)
    tree.column('nama', width=150, anchor=tk.CENTER)
    tree.column('harga', width=100, anchor=tk.CENTER)

    # Mengatur Style Treeview
    style = ttk.Style()
    style.configure("Treeview", font=('Helvetica', 12), background="white",foreground="black",fieldbackground='dodgerblue3',rowheight=40)
    style.map("Treeview", background=[('selected','azure4')])

    # Men-generate Daftar Menu
    menus = [('1.', '001', 'Ayam Geprek', 'Rp20.000'),
            ('2.', '002', 'Ayam Penyet', 'Rp20.000'),
            ('3.', '003', 'Tempe', 'Rp2.000')]

    # Menambahkan Daftar Menu ke Treeview
    for menu in menus:
        tree.insert('', tk.END, values=menu)
    
    # Entry Box Total Harga Pesanan Tamu Hotel
    global inputHargaPesanan
    global hargaPesanan
    hargaPesanan = StringVar()
    tk.Label(screenPesan, text="Masukkan Harga Makanan", font=("Helvetica", 15), bg="white", fg="black", width=100, anchor="w").place(x=725,y=275)
    inputHargaPesanan = tk.Entry(screenPesan, textvariable=hargaPesanan, font=("Helvetica", 12), bg="light grey", fg="black")
    inputHargaPesanan.place(x=745,y=315)

    # Button Pesan untuk Mengonfirmasi Pesanan
    btn = tk.Button(screenPesan, text = "Pesan", bd='2', command=callKonfirmasiPesanan)
    btn.place(x=820,y=355)

    # Button Batal untuk Membatalkan Pesanan
    btn = tk.Button(screenPesan, text = "Batalkan Pesanan", bd='2', command=homeFromPesan)
    btn.place(x=800,y=385)

    screenPesan.mainloop()

# Fungsi untuk Memanggil Layar Konfirmasi Pesanan
def callKonfirmasiPesanan():
    KonfirmasiPesanan(screenPesan)

# Fungsi untuk Memanggil Layar Home
def homeFromPesan():
    home.homescreen(screenPesan)
def homeFromKonfirmasiPesanan():
    home.homescreen(screenKonfirmasiPesan)

# Fungsi untuk Mengonfirmasi Pesanan
def KonfirmasiPesanan(screen):
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
    btn = tk.Button(screenKonfirmasiPesan, text = "Lanjutkan Pesan", bd='2', command=addTotalTagihan)
    btn.place(x=820,y=355)

    # Button Batal untuk Membatalkan Pesanan
    btn = tk.Button(screenKonfirmasiPesan, text = "Batalkan Pesanan", bd='2', command=homeFromKonfirmasiPesanan)
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
        #databaseFail(screen)

    # Mengeksekusi Query
    #namaPengunjungDB = StringVar()
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
            #tk.Label(screenKonfirmasiPesan, text="Nomor Kamar: %s" (hargaPesanan.get()), font=("Helvetica", 15), bg="white", fg="black", width=100, anchor="w").place(x=325,y=240)
            
    except mariadb.Error as e:
        print(f"Error retrieving entry from database: {e}")
    
# Fungsi untuk Menambahkan Harga Total Pesanan ke Tagihan Tamu Hotel tersebut di Database
def addTotalTagihan():
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
    tagihanAkhir = tagihanDB + int(hargaPesanan.get())
    cur = conn.cursor()
    try:
        statement = "UPDATE informasiTamuHotel SET totalTagihan = %s WHERE nomorKamar = %s AND statusPengunjung = %s"

        data = (int(tagihanAkhir), int(nomerKamar.get()), "Check-in",)
        cur.execute(statement, data)
        PesananTercatat(screenKonfirmasiPesan)
    except mariadb.Error as e:
        print(f"Error retrieving entry from database: {e}")  
            
    conn.commit()

def PesananTercatat(screen):
    global screenPesananTercatat

    screen.destroy()
    screenPesananTercatat = tk.Tk()
    screenPesananTercatat.title("Konfirmasi Pesanan Makanan")
    screenPesananTercatat.geometry("1270x690")
    screenPesananTercatat.config(bg="white")

    tk.Label(screenPesananTercatat, text = "Pesanan telah ditambahkan ke tagihan tamu hotel.", font = ("Helvetica", 12, "bold"), bg="white").place(x=105,y=40)

    # Button Batal untuk Kembali ke Home
    btn = tk.Button(screenPesananTercatat, text = "Kembali ke Menu Utama", bd='2', command=homeFromPesananTercatat)
    btn.place(x=800,y=385)

def homeFromPesananTercatat():
    home.homescreen(screenPesananTercatat)
