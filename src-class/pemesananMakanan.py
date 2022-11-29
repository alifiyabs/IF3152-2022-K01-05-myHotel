# Pencatatan Pesanan Makanan
# Penanggung jawab: Adwa Sofia 18220109

# Progress: Sudah berfungsi
# Prerequisite: Install tkinter dan mariadb (beserta seluruh library yang diperlukan)
# Prerequisite: Database mariadb dengan nama myhotel sudah ada
# Notes: Replace password di file connectdatabase.py dengan password database, serta ganti port database jika diperlukan

# Import Library
import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
from tkinter.messagebox import showinfo
import mariadb
from connectdatabase import conn

class ClassPemesananMakanan():
    def __init__(roo):
        super().__init__()

    # Layar Pertama Fitur Pencatatan Pesanan Makanan
    def homePemesananMakanan(self, screen):
        screen.destroy()

        global screenPemesananMakanan
        screenPemesananMakanan= tk.Tk()
        screenPemesananMakanan.title('Pemesanan Makanan')
        screenPemesananMakanan.geometry('1270x690')
        screenPemesananMakanan.config(bg= '#F7F0F5')

        # Mencetak Title dan Sub-Title Halaman
        tk.Label(screenPemesananMakanan, text= 'myHotel', font= ('Helvetica', 20, 'bold'), bg= '#F7F0F5', fg= 'black').place(x= 635, y= 100, anchor= 'center')
        tk.Label(screenPemesananMakanan, text= 'Pesan Makanan', font= ('Helvetica', 10, 'bold'), bg= '#F7F0F5', fg= 'black').place(x= 635, y= 140, anchor= 'center')
        
        # Menampilkan Tombol untuk Kembali ke Menu Utama
        backButton = Button(screenPemesananMakanan, text='Kembali ke Menu Utama', command= self.homeFromPemesananMakanan, bg='#FF595E', font= ('Helvetica', 10, 'bold'))
        backButton.place(x= 75, y= 75, width= 180, height= 50)

        # Entry box Nomor Kamar yang akan Dicatat Pesanan Makanannya
        global inputNoKamar
        global nomerKamar
        nomerKamar= StringVar()
        tk.Label(screenPemesananMakanan, text= 'Masukkan Nomor Kamar:', font= ('Helvetica', 12, 'bold'), bg= '#F7F0F5', fg= 'black').place(x= 635, y= 250, anchor= 'center')
        inputNoKamar= tk.Entry(screenPemesananMakanan, textvariable= nomerKamar, font= ('Helvetica', 12), bg= '#DECBB7', fg= 'black')
        inputNoKamar.place(x= 635, y= 300, width= 300, height= 30, anchor= 'center')

        # Button untuk Melanjutkan ke Verifikasi Nomor Kamar
        btn= tk.Button(screenPemesananMakanan, text= 'Pesan Makanan', font= ('Helvetica', 12, 'bold'), bg= '#DECBB7', width= 20, height= 1, command= self.isKamarTerisi)
        btn.place(x= 635, y= 380, anchor= 'center')

        screenPemesananMakanan.mainloop()

    
    def isKamarTerisi(self):
        # Membuka Koneksi dengan Database
        conn

        # Mengeksekusi Query Verifikasi Nomor Kamar
        cur= conn.cursor()
        try:
            statement= 'SELECT nomorKamar, statusKamar FROM informasiKamar WHERE nomorKamar= %s AND statusKamar= %s'
            data= (int(nomerKamar.get()), 'Unavailable',)
            cur.execute(statement, data)
            row= cur.fetchone()
            if (row == None):
                # Nomor Kamar tersebut tidak dapat Melakukan Pemesanan Makanan
                # (Kamar tidak tersedia, Kamar kosong, atau Tamu Hotel belum Check-in)
                tk.Label(screenPemesananMakanan, text= 'Tidak dapat melakukan pemesanan makanan karena kamar tidak valid!', fg= 'red', font= ('Helvetica, 13')).pack()
            else:
                # Nomor Kamar dapat Melakukan Pemesanan Makanan
                # Menampilkan Layar Kedua dari Fitur Pencatatan Pesanan Makanan
                self.Pesan(screenPemesananMakanan)
        except mariadb.Error as e:
            print(f'Error retrieving entry form database: {e}')
        conn.commit()

    # Layar Kedua Fitur Pencatatan Pesanan Makanan   
    def Pesan(self, screen):
        screen.destroy()
        global screenPesan
        global total_biaya_makanan

        screenPesan= tk.Tk()
        screenPesan.title('Pemesanan Makanan')
        screenPesan.geometry('1270x690')
        screenPesan.config(bg= '#F7F0F5')

        # Mencetak Title dan Sub-Title Halaman
        tk.Label(screenPesan, text= 'myHotel', font= ('Helvetica', 20, 'bold'), bg= '#F7F0F5').place(x= 575, y= 40)
        tk.Label(screenPesan, text= 'Pesan Makanan', font= ('Helvetica', 10, 'bold'), bg= '#F7F0F5', fg= 'black', width= 100, anchor= 'w').place(x= 580, y= 80)

        # Menampilkan Tombol untuk Kembali ke Menu Utama
        backButton = Button(screenPesan, text='Kembali ke Menu Utama', command= self.homeFromPesan, bg='#FF595E', font= ('Helvetica', 10, 'bold'))
        backButton.place(x= 75, y= 75, width= 180, height= 50)

        # Menampilkan Pilihan Menu Makanan
        pilihanMenuMakanan= Frame(screenPesan, height= 370, width= 300, bg= '#F7F0F5', highlightbackground= "black", highlightthickness= 2)
        pilihanMenuMakanan.place(x= 635, y= 300, anchor= 'center')

        ayamgeprek= StringVar()
        ayampenyet= StringVar()
        tempe= StringVar()
        nasi= StringVar()
        sayur= StringVar()
        teh= StringVar()
        kopi= StringVar()
        total_biaya_makanan= StringVar()

        # Label Pilihan Menu Makanan
        namaMenu_label = Label(pilihanMenuMakanan, font= ('Helvetica', 13, 'bold'), text= 'Nama Menu', width= 12, bg= '#E8E8E8', fg= 'black')
        namaMenu_label.grid(row= 1, column= 0, padx= 5, pady= 5)
        kuantitas_label = Label(pilihanMenuMakanan, font= ('Helvetica', 13, 'bold'), text= 'Kuantitas', width= 12, bg= '#E8E8E8', fg= 'black')
        kuantitas_label.grid(row= 1, column= 1, padx= 5, pady= 5)
        ayamgeprek_label= Label(pilihanMenuMakanan, font= ('Helvetica', 13), text= 'Ayam Geprek', width= 12, bg= '#F7F0F5', fg= 'black')
        ayamgeprek_label.grid(row= 2, column= 0, pady= 5)
        ayampenyet_label= Label(pilihanMenuMakanan, font= ('Helvetica', 13), text= 'Ayam Penyet', width= 12, bg= '#F7F0F5', fg= 'black')
        ayampenyet_label.grid(row= 3, column= 0, pady= 5)
        tempe_label= Label(pilihanMenuMakanan, font= ('Helvetica', 13), text= 'Tempe', width= 12, bg= '#F7F0F5', fg= 'black')
        tempe_label.grid(row= 4, column= 0, pady= 5)
        nasi_label= Label(pilihanMenuMakanan, font= ('Helvetica', 13), text= 'Nasi', width= 12, bg= '#F7F0F5', fg= 'black')
        nasi_label.grid(row= 5, column= 0, pady= 5)
        sayur_label= Label(pilihanMenuMakanan, font= ('Helvetica', 13), text= 'Sayur', width= 12, bg= '#F7F0F5', fg= 'black')
        sayur_label.grid(row= 6, column= 0, pady= 5)
        teh_label= Label(pilihanMenuMakanan, font= ('Helvetica', 13), text= 'Teh', width= 12, bg= '#F7F0F5', fg= 'black')
        teh_label.grid(row= 7, column= 0, pady= 5)
        kopi_label= Label(pilihanMenuMakanan, font= ('Helvetica', 13), text= 'Kopi', width= 12, bg= '#F7F0F5', fg= 'black')
        kopi_label.grid(row= 8, column= 0, pady= 5)

        # Entry Pilihan Menu Makanan
        entry_ayamgeprek= Entry(pilihanMenuMakanan, font= ('Helvetica', 13), textvariable= ayamgeprek, width= 8, bg= '#F6F6F6')
        entry_ayamgeprek.grid(row= 2, column= 1, pady= 5)
        entry_ayampenyet= Entry(pilihanMenuMakanan, font= ('Helvetica', 13), textvariable= ayampenyet, width= 8, bg= '#F6F6F6')
        entry_ayampenyet.grid(row= 3, column= 1, pady= 5)
        entry_tempe= Entry(pilihanMenuMakanan, font= ('Helvetica', 13), textvariable= tempe, width= 8, bg= '#F6F6F6')
        entry_tempe.grid(row=4, column=1, pady= 5)
        entry_nasi= Entry(pilihanMenuMakanan, font=('Helvetica', 13), textvariable=nasi, width=8, bg='#F6F6F6')
        entry_nasi.grid(row=5, column=1, pady= 5)
        entry_sayur= Entry(pilihanMenuMakanan, font=('Helvetica', 13), textvariable=sayur, width=8, bg='#F6F6F6')
        entry_sayur.grid(row=6, column=1, pady= 5)
        entry_teh= Entry(pilihanMenuMakanan, font=('Helvetica', 13), textvariable=teh, width=8, bg='#F6F6F6')
        entry_teh.grid(row=7, column=1, pady= 5)
        entry_kopi= Entry(pilihanMenuMakanan, font=('Helvetica', 13), textvariable=kopi, width=8, bg='#F6F6F6')
        entry_kopi.grid(row=8, column=1, pady= 5)

        total_label= Label(pilihanMenuMakanan, font= ('Helvetica', 13, 'bold'), text='Total Harga', width=12, bg='#E8E8E8', fg='black')
        total_label.grid(row=1, column=2, padx= 5, pady= 5)

        total_biaya_makanan.set('0')
        entry_total= Label(pilihanMenuMakanan, font= ('Helvetica', 12, 'bold'), textvariable= total_biaya_makanan, width=12, bg='#F7F0F5')
        entry_total.grid(row=2, column=2, padx= 5, pady= 5)

        # Fungsi untuk me-reset input Kuantitas Pilihan Menu Makanan
        def Reset():
            entry_ayamgeprek.delete(0, END)
            entry_ayampenyet.delete(0, END)
            entry_tempe.delete(0, END)
            entry_nasi.delete(0, END)
            entry_sayur.delete(0, END)
            entry_teh.delete(0, END)
            entry_kopi.delete(0, END)
            total_biaya_makanan.set('0')
            entry_total= Label(pilihanMenuMakanan, font= ('Helvetica', 12, 'bold'), textvariable= total_biaya_makanan, width=12, bg='#F7F0F5')
            entry_total.grid(row=2, column=2, padx= 5, pady= 5)
        
        def Total():
            global total_harga

            try: a1= int(ayamgeprek.get())
            except: a1=0

            try: a2= int(ayampenyet.get())
            except: a2=0

            try: a3= int(tempe.get())
            except: a3=0
        
            try: a4= int(nasi.get())
            except: a4=0
        
            try: a5= int(sayur.get())
            except: a5=0

            try: a6= int(teh.get())
            except: a6=0
        
            try: a7= int(kopi.get())
            except: a7=0

            # Harga makanan
            harga1= 20000*a1
            harga2= 20000*a2
            harga3= 2000*a3
            harga4= 5000*a4
            harga5= 10000*a5
            harga6= 3000*a6
            harga7= 3000*a7

            total_harga= harga1+harga2+harga3+harga4+harga5+harga6+harga7
            string_harga= str(total_harga)
            total_biaya_makanan.set(string_harga)

            entry_total= Label(pilihanMenuMakanan, font= ('Helvetica', 13, 'bold'), textvariable= total_biaya_makanan, width=12, bg='#F7F0F5')
            entry_total.grid(row=2, column=2)

        # Button Reset untuk me-reset input Kuantitas Pilihan Menu Makanan
        resetBtn= Button(screenPesan, text= 'Reset Kuantitas', font= ('Helvetica', 12), bg= '#DECBB7', width=15, height= 1, command=Reset)
        resetBtn.place(x= 475, y= 450)

        # Button Total untuk Menampilkan Total Harga Pesanan
        totalBtn= Button(screenPesan, text= 'Lihat Total Harga', font= ('Helvetica', 12), bg= '#DECBB7', width=15, height= 1, command=Total)
        totalBtn.place(x= 640, y= 450)

        # Button Pesan untuk Mengonfirmasi Pesanan
        catatPesananBtn= tk.Button(screenPesan, text= 'Catat Pesanan', font= ('Helvetica', 12, 'bold'), bg= '#DECBB7', width= 20, height= 2, command=self.callKonfirmasiPesanan)
        catatPesananBtn.place(x= 635, y= 550, anchor= 'center')
        
        screenPesan.mainloop()
        
        
    # Fungsi untuk Memanggil Layar Konfirmasi Pesanan
    def callKonfirmasiPesanan(self):
        self.KonfirmasiPesanan(screenPesan)

    # Fungsi untuk Memanggil Layar Home
    def homeFromPemesananMakanan(self):
        from home import ClassHome
        ClassHome().homescreen(screenPemesananMakanan)
    def homeFromPesan(self):
        from home import ClassHome
        ClassHome().homescreen(screenPesan)
    def homeFromKonfirmasiPesanan(self):
        from home import ClassHome
        ClassHome().homescreen(screenKonfirmasiPesan)
    def homeFromPesananTercatat(self):
        from home import ClassHome
        ClassHome().homescreen(screenPesananTercatat)

    # Fungsi untuk Mengonfirmasi Pesanan
    def KonfirmasiPesanan(self, screen):
        global screenKonfirmasiPesan

        screen.destroy()
        screenKonfirmasiPesan= tk.Tk()
        screenKonfirmasiPesan.title('Pemesanan Makanan')
        screenKonfirmasiPesan.geometry('1270x690')
        screenKonfirmasiPesan.config(bg='#F7F0F5')

        # Mencetak Title dan Sub-Title Halaman
        tk.Label(screenKonfirmasiPesan, text= 'myHotel', font= ('Helvetica', 20, 'bold'), bg= '#F7F0F5', fg= 'black').place(x= 635, y= 100, anchor= 'center')
        tk.Label(screenKonfirmasiPesan, text= 'Konfirmasi Pesanan Makanan', font= ('Helvetica', 10, 'bold'), bg= '#F7F0F5', fg= 'black').place(x= 635, y= 140, anchor= 'center')

        # Button Batal untuk Membatalkan Pesanan
        batalPesanBtn= Button(screenKonfirmasiPesan, text= 'Batalkan Pesanan', font= ('Helvetica', 12, 'bold'), bg= '#DECBB7', width= 15, height= 2, command=self.homeFromKonfirmasiPesanan)
        batalPesanBtn.place(x= 445, y= 425)

        # Button Pesan untuk Mengonfirmasi Pesanan
        lanjutPesanBtn= Button(screenKonfirmasiPesan, text= 'Lanjutkan Catat Pesanan', font= ('Helvetica', 12, 'bold'), bg= '#DECBB7', width= 20, height= 2, command=self.addTotalTagihan)
        lanjutPesanBtn.place(x= 620, y= 425)

        # Membuka Koneksi dengan Database
        conn

        # Mengeksekusi Query
        cur= conn.cursor()
        try:
            statement= 'SELECT nomorKamar, namaPengunjung FROM informasiTamuHotel WHERE nomorKamar= %s AND statusPengunjung= %s'
            data= (int(nomerKamar.get()), 'Check-in',)
            cur.execute(statement, data)
            
            row= cur.fetchone()
            if (row == None):
                tk.Label(screenKonfirmasiPesan, text= 'Tidak dapat melakukan pemesanan makanan karena kamar tidak valid!', fg= 'red', font= ('Helvetica, 13')).pack()
            else:
                noKamarDB= row[0]
                namaPengunjungDB= row[1]
                
                # Menampilkan Konfirmasi Pesanan Makanan
                konfirmasiPesanan= Frame(screenKonfirmasiPesan, height= 370, width= 300, bg= '#F7F0F5', highlightbackground= "black", highlightthickness= 2)
                konfirmasiPesanan.place(x= 635, y= 300, anchor= 'center')

                # Label Pilihan Menu Makanan
                nomorKamar_label = Label(konfirmasiPesanan, font= ('Helvetica', 13, 'bold'), text= 'Nomor Kamar', width= 20, bg= '#E8E8E8', fg= 'black')
                nomorKamar_label.grid(row= 0, column= 0, padx= 5, pady= 5)
                namaPengunjung_label = Label(konfirmasiPesanan, font= ('Helvetica', 13, 'bold'), text= 'Nama Pengunjung', width= 20, bg= '#E8E8E8', fg= 'black')
                namaPengunjung_label.grid(row= 1, column= 0, padx= 5, pady= 5)
                hargaPesanan_label = Label(konfirmasiPesanan, font= ('Helvetica', 13, 'bold'), text= 'Total Harga Pesanan', width= 20, bg= '#E8E8E8', fg= 'black')
                hargaPesanan_label.grid(row= 2, column= 0, padx= 5, pady= 5)
                dataNomorKamar_label = Label(konfirmasiPesanan, font= ('Helvetica', 13), text= noKamarDB, width= 20, bg= '#E8E8E8', fg= 'black')
                dataNomorKamar_label.grid(row= 0, column= 1, padx= 5, pady= 5)
                dataNamaPengunjung_label = Label(konfirmasiPesanan, font= ('Helvetica', 13), text= namaPengunjungDB, width= 20, bg= '#E8E8E8', fg= 'black')
                dataNamaPengunjung_label.grid(row= 1, column= 1, padx= 5, pady= 5)
                dataHargaPesanan_label = Label(konfirmasiPesanan, font= ('Helvetica', 13), text= total_biaya_makanan.get(), width= 20, bg= '#E8E8E8', fg= 'black')
                dataHargaPesanan_label.grid(row= 2, column= 1, padx= 5, pady= 5)
            
        except mariadb.Error as e:
            print(f'Error retrieving entry from database: {e}')
        
    # Fungsi untuk Menambahkan Harga Total Pesanan ke Tagihan Tamu Hotel tersebut di Database
    def addTotalTagihan(self):
        # Membuka Koneksi dengan Database
        conn
        
        # Mengeksekusi Query
        cur= conn.cursor()
        try:
            statement= 'SELECT nomorKamar, namaPengunjung, totalTagihan FROM informasiTamuHotel WHERE nomorKamar= %s AND statusPengunjung= %s'
            data= (int(nomerKamar.get()), 'Check-in',)
            cur.execute(statement, data)
            
            row= cur.fetchone()
            if (row == None):
                tk.Label(screenKonfirmasiPesan, text= 'Tidak dapat melakukan pemesanan makanan karena kamar tidak valid!', fg= 'red', font= ('Helvetica, 13')).pack()
            else:
                noKamarDB= row[0]
                namaPengunjungDB= row[1]
                tagihanDB= row[2]
        except mariadb.Error as e:
            print(f'Error retrieving entry from database: {e}')
        tagihanAkhir= tagihanDB + int(total_harga)
        cur= conn.cursor()
        try:
            statement= 'UPDATE informasiTamuHotel SET totalTagihan= %s WHERE nomorKamar= %s AND statusPengunjung= %s'

            data= (int(tagihanAkhir), int(nomerKamar.get()), 'Check-in',)
            cur.execute(statement, data)
            self.PesananTercatat(screenKonfirmasiPesan)
        except mariadb.Error as e:
            print(f'Error retrieving entry from database: {e}')  
                
        conn.commit()

    def PesananTercatat(self, screen):
        global screenPesananTercatat

        screen.destroy()
        screenPesananTercatat= tk.Tk()
        screenPesananTercatat.title('Pemesanan Makanan')
        screenPesananTercatat.geometry('1270x690')
        screenPesananTercatat.config(bg='#F7F0F5')

        tk.Label(screenPesananTercatat, text= 'Pesanan telah ditambahkan ke tagihan tamu hotel.', font= ('Helvetica', 12, 'bold'), bg= '#F7F0F5', fg= 'black').place(x= 635, y= 250, anchor= 'center')

        # Menampilkan Tombol untuk Kembali ke Menu Utama
        backButton = Button(screenPesananTercatat, text='Kembali ke Menu Utama', command= self.homeFromPesananTercatat, bg='#FF595E', font= ('Helvetica', 10, 'bold'))
        backButton.place(x= 635, y= 550, anchor= 'center', width= 180, height= 50)
