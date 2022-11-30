# Check Out
# Penanggung jawab: Theodore Justin Lionar 18220011

# Prerequisite: Library tkcalendar, tkinter, mariadb
# Prerequisite: Database mariadb dengan nama myhotel
# Notes: Warna yang dipakai #F7F0F5, #DECBB7, #8F857D https://coolors.co/f7f0f5-decbb7-8f857d-5c5552-433633

import sys
from tkinter import *
from tkinter import ttk, messagebox
from tkcalendar import Calendar
from datetime import date
from tagihan import ClassTagihan
from connectdatabase import *
import tkinter as tk
import datetime
import os
import mariadb

class ClassCheckOut():
    # Layar utama menu check out
    def homeCheckOut(self, layar):
        global screen
        layar.destroy()
        screen = Tk()
        screen.title("myHotel")
        screen.geometry("1270x690")
        screen.config(bg = "#F7F0F5")
        
        global noKamar
        global nomorKamar_var
        noKamar = StringVar()

        # Judul halaman
        self.showTitle(screen)
        self.showSectionTitle(screen)

        def backToHome():
            from home import ClassHome
            ClassHome().homescreen(screen)

        # Entry box nomor kamar
        Label(screen, text = "Nomor Kamar", font = ("Helvetica", 12, "bold"), bg="#F7F0F5").place(x = 485, y = 220)
        nomorKamar_var = Entry(screen, textvariable = noKamar, font=("Helvetica", 12), bg = "#DECBB7", fg = "black")
        nomorKamar_var.place(x = 635, y = 250, width = 300, height = 30,anchor="n")

        # Button next menuju verifikasi kamar
        Button(screen, text = "Berikutnya", font = ("Helvetica", 12, "bold"), bg="#DECBB7", width = 10, height = 1, command = self.verifyKamar).place(x = 785, y = 320,anchor="ne")
        Button(screen, text = "Kembali ke Menu Utama", font = ("Helvetica", 10, "bold"), bg="#FF595E", width = 10, height = 1, command = backToHome).place(x = 75, y = 75, width=180, height=50)

        screen.resizable(False,False)
        screen.mainloop()

    def verifyKamar(self):
        # Buka koneksi dengan database
        conn
        
        # Execute query
        cur = conn.cursor()
        try:
            statement = "SELECT nomorKamar, statusKamar FROM informasiKamar WHERE nomorKamar = %s AND statusKamar = %s"
            data = (int(noKamar.get()), "Unavailable",)
            cur.execute(statement, data)
            row = cur.fetchone()
            if (row == None):
                self.kamarInvalid(screen)
            else:
                self.kamarValid(screen)
        except mariadb.Error as e:
            print(f"Error retrieving entry form database: {e}")
            self.databaseFail(screen)
        conn.commit()

    # Jika kamar valid, input data
    def kamarValid(self, screen):
        global screen1
        screen.destroy()
        screen1 = Tk()
        screen1.title("myHotel")
        screen1.geometry("1270x690")
        screen1.config(bg = "#F7F0F5")

        # Judul halaman
        self.showTitle(screen1)
        self.showSectionTitle(screen1)

        def ulangiCheckOut():
            self.ulangi(screen1)

        global NIKPelanggan
        global NIKPelanggan_var
        global cal
        NIKPelanggan = StringVar()

        # Entry box NIK
        Label(screen1, text = "NIK Pelanggan", font = ("Helvetica", 12, "bold"), bg="#F7F0F5").place(x = 485, y = 220)
        NIKPelanggan_var = Entry(screen1, textvariable = NIKPelanggan, font=("Helvetica", 12), bg = "#DECBB7", fg = "black")
        NIKPelanggan_var.place(x = 635, y = 250, width = 300, height = 30,anchor="n")

        # Entry box tanggal check out
        Label(screen1, text = "Tanggal Check Out", font = ("Helvetica", 12, "bold"), bg="#F7F0F5").place(x = 485, y = 320)
        cal = Calendar(screen1, selectmode = 'day', date_pattern = 'yyyy-mm-dd')
        cal.place(x = 485, y = 320, width = 300, height = 200)

        # Button next menuju ambil tanggal dan verifikasi data
        Button(screen1, text = "Berikutnya", font = ("Helvetica", 12, "bold"), bg="#DECBB7", width = 10, height = 1, command = self.getDate).place(x = 785, y = 550,anchor="ne")
        
        # Button back menuju halaman utama check out
        Button(screen1, text = "Kembali", font = ("Helvetica", 12, "bold"), bg="#8F857D", width = 10, height = 1, command = ulangiCheckOut).place(x = 485, y = 550)

        screen1.resizable(False,False)
        screen1.mainloop()

    # Fungsi untuk mengambil tanggal dari date picker calendar dan lanjut ke verifikasi data
    def getDate(self):
        global tanggalCheckOut

        tanggalCheckOut = cal.get_date()
        self.verifyData()

    # Jika kamar tidak valid (tidak ada ataupun tidak sedang digunakan)
    def kamarInvalid(self, screen):
        Label(screen, text = "Tidak dapat melakukan check out karena kamar tidak valid!", fg = "red", font = ("Helvetica, 13")).pack()

    # Verifikasi data tamu dan kamar
    def verifyData(self):
        global tanggalCheckOut_date

        # Koneksi dengan database
        conn
        
        # Execute query
        cur = conn.cursor()
        try:
            statement = "SELECT tanggalCheckIn, tanggalCheckOut, durasiMenginap FROM informasiTamuHotel WHERE NIK = %s AND nomorKamar = %s"
            data = (int(NIKPelanggan.get()), int(noKamar.get()),)
            cur.execute(statement, data)
            row = cur.fetchone()
            if (row == None):
                self.tamuInvalid(screen1)
            else: 
                # Ambil tanggal check out database
                statement = "SELECT tanggalCheckOut FROM informasiTamuHotel WHERE NIK = %s AND nomorKamar = %s AND statusPengunjung = %s"
                data = (int(NIKPelanggan.get()), int(noKamar.get()),"Check-in",)
                cur.execute(statement, data)
                row = cur.fetchone()
                for x in row:
                    tanggalCheckOutVerify = x

                # Ambil tanggal check in database
                statement = "SELECT tanggalCheckOut FROM informasiTamuHotel WHERE NIK = %s AND nomorKamar = %s AND statusPengunjung = %s"
                data = (int(NIKPelanggan.get()), int(noKamar.get()),"Check-in",)
                cur.execute(statement, data)
                row = cur.fetchone()
                for x in row:
                    tanggalCheckInVerify = x

                tanggalCheckOut_date = (datetime.datetime.strptime(tanggalCheckOut, '%Y-%m-%d')).date()

                # Cek apakah tanggal benar sesuai dengan database
                if (tanggalCheckOut_date == tanggalCheckOutVerify):
                    self.validateCheckOut(screen1)
                else:
                    if (tanggalCheckOut_date <= tanggalCheckInVerify):
                        self.waktuInvalid(screen1)
                    elif (tanggalCheckOut_date > tanggalCheckOutVerify):
                        self.waktuInvalid(screen1)
                    else:
                        self.waktuInvalid2(screen1)
        except mariadb.Error as e:
            print(f"Error retrieving entry form database: {e}")
            self.databaseFail(screen1)
        conn.commit()

    # Validasi perlakuan check out
    def validateCheckOut(self, screen1):
        global screen2
        screen1.destroy()
        screen2 = Tk()
        screen2.title("myHotel")
        screen2.geometry("1270x690")
        screen2.config(bg = "#F7F0F5")

        self.showTitle(screen2)
        self.showSectionTitle(screen2)
        
        def ulangiCheckOut():
            self.ulangi(screen2)
        
        def confirmationTagihan():
            self.confirmTagihan(screen2)

        # Cetak informasi kamar yang akan di-check out
        self.cetakValidateCheckOut()
        
        # Konfirmasi proses check out
        Label(screen2, text = "Lakukan check out?", font = ("Helvetica", 12, "bold"), bg="#F7F0F5").place(x = 635, y = 340,anchor="n")
        Button(screen2, text = "Ya", font = ("Helvetica", 12, "bold"), bg="#DECBB7", width = 10, height = 1, command = confirmationTagihan).place(x = 785, y = 400,anchor="ne")
        Button(screen2, text = "Tidak", font = ("Helvetica", 12, "bold"), bg="#8F857D", width = 10, height = 1, command = ulangiCheckOut).place(x = 485, y = 400)
        
        screen2.resizable(False,False)
        screen2.mainloop()

    # Cetak informasi kamar yang akan di-check out
    def cetakValidateCheckOut(self):
        # Koneksi ke database
        conn

        # Execute query
        cur = conn.cursor()
        try:
            # Mengambil informasi kamar tamu yang diperlukan
            statement = "SELECT nomorKamar, namaPengunjung, NIK FROM informasiTamuHotel WHERE NIK = %s AND nomorKamar = %s"
            data = (int(NIKPelanggan.get()), int(noKamar.get()),)
            cur.execute(statement, data)
        except mariadb.Error as e:
            print(f"Error retrieving entry form database: {e}")
            self.databaseFail(screen2)
            
        # Tampilkan informasi dalam bentuk tabel
        columns = (1,2,3)
        tree = ttk.Treeview(screen2, height = 1, columns = columns, show = 'headings')
        tree.place(x = 635, y = 220,anchor="n")
        tree.heading(1, text= "Nomor Kamar")
        tree.heading(2, text= "Nama Tamu")
        tree.heading(3, text= "NIK Tamu")

        style = ttk.Style()
        style.configure('Treeview',font=("helvetica",10),background='#DECBB7',foreground='black',fieldbackground='#F7F0F5',rowheight=25)
        style.map('Treeview',background=[("selected","#8F857D")],foreground=[("selected","#F7F0F5")])

        i = 1
        for (nomorKamar, namaPengunjung, NIK) in cur:
            tree.insert(parent='', index=i, text='', values = (nomorKamar, namaPengunjung, NIK))
            i += 1
        
        conn.commit()

    # Mengonfirmasi perlakuan check out
    def confirmTagihan(self, screen2):
        global screen3
        screen2.destroy()
        screen3 = Tk()
        screen3.title("myHotel")
        screen3.geometry("1270x690")
        screen3.config(bg = "#F7F0F5")
        
        # Judul halaman
        self.showTitle(screen3)

        tagihan_var = ClassTagihan()
        tagihan_var.showSectionTitle(screen3)
        tagihan_var.infotagihan(NIKPelanggan.get(),noKamar.get(),screen3)
        
        # Button bayar untuk melakukan proses check out
        Button(screen3, text = "Bayar", font = ("Helvetica", 12, "bold"), bg="#DECBB7", width = 10, height = 1, command = self.processCheckOut).place(x = 635, y = 520,anchor="n")
        
        screen3.resizable(False,False)
        screen3.mainloop()

    # Proses update database untuk melakukan check out
    def processCheckOut(self):
        # Koneksi ke database
        conn

        # Execute query
        cur = conn.cursor()
        try:
            # Update status pengunjung dari sedang check in menjadi sedang check out
            statement = "UPDATE informasiTamuHotel SET statusPengunjung = %s WHERE NIK = %s AND nomorKamar = %s"
            data = ("Check-out", int(NIKPelanggan.get()), int(noKamar.get()),)
            cur.execute(statement, data)

            # Update status kamar dari unavailable menjadi available
            cur = conn.cursor()
            statement = "UPDATE informasiKamar SET statusKamar = %s WHERE nomorKamar = %s"
            data = ("Available", int(noKamar.get()),)
            cur.execute(statement, data)

            # Ambil nilai tagihan tamu saat ini
            cur = conn.cursor()
            statement = "SELECT totalTagihan FROM informasiTamuHotel WHERE NIK = %s AND nomorKamar = %s"
            data = (int(NIKPelanggan.get()), int(noKamar.get()),)
            cur.execute(statement, data)
            row = cur.fetchone()
            for x in row:
                tagihan = x

            # Update riwayat kamar dari jumlah dipesan dan total pendapatan kamar berdasarkan tagihan tamu
            cur = conn.cursor()
            statement = "UPDATE riwayatKamar SET totalDipesan = (totalDipesan + %s), totalPendapatanKamar = (totalPendapatanKamar + %s) WHERE nomorKamar = %s"
            data = (1, tagihan, int(noKamar.get()),)
            cur.execute(statement, data)
        except mariadb.Error as e:
            print(f"Error updating or retrieving entry form database: {e}")
            self.databaseFail(screen3)

        conn.commit()
        self.successCheckOut(screen3)

    # Menampilkan status sukses melakukan check out
    def successCheckOut(self, screen3):
        global screen4
        screen3.destroy()
        screen4 = Tk()
        screen4.title("myHotel")
        screen4.geometry("1270x690")
        screen4.config(bg = "#F7F0F5")

        # Judul halaman
        self.showTitle(screen4)
        self.showSectionTitle(screen4)

        def checkOutAgain():
            self.homeCheckOut(screen4)
        
        def backToHome():
            from home import ClassHome
            ClassHome().homescreen(screen4)

        Label(screen4, text = "Check out berhasil dilakukan!", font = ("Helvetica", 12, "bold"), bg="#F7F0F5").place(x = 635, y = 220,anchor="n")
        
        # Button selesai untuk keluar (nanti kembali ke main menu)
        Button(screen4, text = "Selesai", font = ("Helvetica", 12, "bold"), bg="#DECBB7", width = 10, height = 1, command = backToHome).place(x = 785, y = 320,anchor="ne")
        
        # Button kembali untuk menuju ke halaman utama check out
        Button(screen4, text = "Kembali", font = ("Helvetica", 12, "bold"), bg="#8F857D", width = 10, height = 1, command = checkOutAgain).place(x = 485, y = 320)

        screen4.resizable(False,False)
        screen4.mainloop()

    # Text tamu invalid karena identitas yang salah
    def tamuInvalid(self, screen):
        Label(screen, text = "Tidak dapat melakukan check out karena identitas tamu tidak tepat!", fg = "red", font = ("Helvetica, 13")).pack()

    # Text input waktu invalid karena tidak melakukan check out di waktu yang seharusnya
    def waktuInvalid (self, screen):
        Label(screen, text = "Waktu check out invalid!", fg = "red", font = ("Helvetica, 12")).pack()

    # Text input waktu invalid karena melakukan check out terlebih dahulu dibanding pesanan
    def waktuInvalid2 (self, screen):
        Label(screen, text = "Belum waktunya check out!", fg = "red", font = ("Helvetica, 12")).pack()

    # Menampilkan ulang halaman utama check out 
    def ulangi (self, screen):
        self.homeCheckOut(screen)

    # Tampilan saat koneksi atau operasi ke database gagal
    def databaseFail(self, screen):
        global screen5
        screen.destroy()
        screen5 = Tk()
        screen5.title("myHotel")
        screen5.geometry("1270x690")
        screen5.config(bg = "#F7F0F5")   

        # Judul halaman
        self.showTitle(screen5)
        self.showSectionTitle(screen5)

        def ulangiCheckOut():
            self.ulangi(screen5)

        # Tombol kembali ke laman utama check out
        Label(screen5, text = "Kegagalan Sistem!", font = ("Helvetica", 12, "bold"), bg="#F7F0F5").place(x = 635, y = 220,anchor="center")
        Button(screen5, text = "Kembali", font = ("Helvetica", 12, "bold"), bg="#8F857D", width = 10, height = 1, command = ulangiCheckOut).place(x = 485, y = 580)

        screen5.resizable(False,False)
        screen5.mainloop()

    # Menampilkan judul aplikasi
    def showTitle(self, screen):
        Label(screen, text="myHotel",font=("helvetica",20,"bold"),bg="#F7F0F5",fg="black").place(x=635,y=100,anchor="center")

    # Menampilkan judul section check out
    def showSectionTitle(self, screen):
        Label(screen, text="Check-out",font=("helvetica",10,"bold"),bg="#F7F0F5",fg="black").place(x=635,y=140,anchor="center")
