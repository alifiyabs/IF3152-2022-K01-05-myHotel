# Menu Makanan
# Penanggung jawab: Adwa Sofia 18220109

# Progress: Sudah berfungsi
# Prerequisite: Install tkinter (beserta seluruh library yang diperlukan)

# Import Library
import tkinter as tk
from tkinter import ttk

# Layar Utama Fitur Menampilkan Menu Makanan
class ClassMenuMakanan():
    def homeMenuMakanan(self, screen):
        screen.destroy()
        global root
        root= tk.Tk()
        root.title('Menu Makanan')
        root.geometry('1270x690')
        root.config(bg= '#F7F0F5')

        # Mencetak Title dan Sub-Title Halaman
        tk.Label(root, text= 'myHotel', font= ('Helvetica', 20, 'bold'), bg= '#F7F0F5', fg= 'black').place(x= 635, y= 100, anchor= 'center')
        tk.Label(root, text= 'Menu Makanan', font= ('Helvetica', 10, 'bold'), bg= '#F7F0F5', fg= 'black').place(x= 635, y= 140, anchor= 'center')

        # Menampilkan Tombol untuk Kembali ke Menu Utama
        tk.Button(root, text='Kembali ke Menu Utama', command= self.homeFromMenuMakanan, bg='#FF595E', font= ('Helvetica', 10, 'bold')).place(x= 75, y= 75, width= 180, height= 50)

        # Menampilkan Daftar Menu Makanan menggunakan Tabel
        # Mendefinisikan Kolom-Kolom Tabel
        columns= ('no', 'id_makanan', 'nama', 'harga')
        tree= ttk.Treeview(root, height= 7, columns= columns, show= 'headings')

        # Mendefinisikan Headings
        tree.heading('no', text= 'No')
        tree.heading('id_makanan', text= 'ID Makanan')
        tree.heading('nama', text= 'Nama')
        tree.heading('harga', text= 'Harga')
        
        # Mendefinisikan Lebar Kolom
        tree.column('no', width= 30)
        tree.column('id_makanan', width= 80)
        tree.column('nama', width= 150)
        tree.column('harga', width= 100)

        # Mendefinisikan Letak Tabel
        tree.place(x= 635, y= 220, anchor= 'n')

        # Mengatur Style Tabel
        style= ttk.Style()
        style.configure('Treeview', font= ('Helvetica', 10), background= '#DECBB7', foreground= 'black', fieldbackground= '#F7F0F5', rowheight= 25)
        style.map('Treeview', background= [('selected', '#8F857D')], foreground= [('selected','#F7F0F5')])

        # Men-generate Daftar Menu
        menus= [('1.', '001', 'Ayam Geprek', 20000),
                ('2.', '002', 'Ayam Penyet', 20000),
                ('3.', '003', 'Tempe', 2000),
                ('4.', '004', 'Nasi', 5000),
                ('5.', '005', 'Sayur', 10000),
                ('6.', '006', 'Teh', 3000),
                ('7.', '007', 'Kopi', 3000)]
        
        # Menambahkan Daftar Menu ke Treeview
        for menu in menus:
            tree.insert('', tk.END, values=menu)

        root.resizable(False, False)
        root.mainloop()

    # Fungsi untuk Kembali ke Menu Utama dari Fitur Menu Makanan
    def homeFromMenuMakanan(self):
        from home import ClassHome
        ClassHome().homescreen(root)