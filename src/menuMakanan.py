# Menu Makanan
# Penanggung jawab: Adwa Sofia 18220109

# Progress: Sudah berfungsi
# Prerequisite: Install tkinter dan mariadb (beserta seluruh library yang diperlukan)
# Prerequisite: Database mariadb dengan nama myhotel sudah ada
# Notes: Replace ***** dengan password database, serta ganti port database jika diperlukan

# Import Library
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# Layar Utama Fitur Menampilkan Menu Makanan
def MenuMakanan(screen):
    screen.destroy()
    root = tk.Tk()
    root.title('Menu Makanan')
    root.geometry('1270x690')
    root.config(bg = "white")

    # Mencetak Title dan Sub-Title Halaman
    tk.Label(root, text = "myHotel", font = ("Helvetica", 20, "bold"), bg="white").place(x=575,y=40)
    tk.Label(root, text="Menu Makanan", font=("Helvetica", 10, "bold"), bg="white", fg="black", width=100, anchor='w').place(x=580,y=80)

    # Menampilkan Daftar Menu Makanan menggunakan Tabel
    # Mendefinisikan Kolom-Kolom Tabel
    columns = ('no', 'id_makanan', 'nama', 'harga')

    tree = ttk.Treeview(root, height=13, columns=columns, show='headings')
    tree.pack(side=tk.BOTTOM, pady=20)

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
    style.configure("Treeview", font=('helvetica', 12), background="white",foreground="black",fieldbackground='dodgerblue3',rowheight=40)
    style.map("Treeview",background=[('selected','azure4')])

    # Men-generate Daftar Menu
    menus = [('1.', '001', 'Ayam Geprek', 'Rp20.000'),
            ('2.', '002', 'Ayam Penyet', 'Rp20.000'),
            ('3.', '003', 'Tempe', 'Rp2.000')]

    # Menambahkan Daftar Menu ke Treeview
    for menu in menus:
        tree.insert('', tk.END, values=menu)

    root.mainloop()