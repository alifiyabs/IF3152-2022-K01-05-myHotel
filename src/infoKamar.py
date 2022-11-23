import sys
import tkinter as tk
# from PIL import Image, ImageTk
import os
from tkinter import ttk
# import mysql.connector as mysql
import mariadb

def InfoKamar(screen):
    global root
    screen.destroy()
    root = tk.Tk()
    root.title("Informasi Kamar")
    root.geometry('1270x690')
    root.configure(bg='#F7F0F5')
    
    MyHotellabelTitle = tk.Label(root,text="myHotel",font=("helvetica",20,"bold"),bg="#F7F0F5",fg="black").place(x=635,y=100,anchor="center")
    InformasilabelTitle = tk.Label(root,text="Informasi Kamar",font=("helvetica",10,"bold"),bg="#F7F0F5",fg="black").place(x=635,y=140,anchor="center")

    columns = (1,2,3,4,5,6)
    tree = ttk.Treeview(root, height=10, columns=columns, show='headings')
    tree.column(1,width=100)
    tree.column(2,width=100)
    tree.column(3,width=200)
    tree.place(x = 635, y = 220,anchor="n")
    tree.heading(1, text='Nomor Kamar')
    tree.heading(2, text='Tipe Kamar')
    tree.heading(3, text='Luas Kamar')
    tree.heading(4, text='Fasilitas')
    tree.heading(5, text='Harga per Malam')
    tree.heading(6, text='Status Kamar')

    style = ttk.Style()
    style.configure('Treeview',font=("helvetica",10),background='#DECBB7',foreground='black',fieldbackground='#F7F0F5',rowheight=25)
    style.map('Treeview',background=[("selected","#8F857D")],foreground=[("selected","#F7F0F5")])

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
    
    cur = conn.cursor()
    cur.execute('SELECT * FROM informasikamar')

    i=1
    for (nomorKamar, tipeKamar, luasKamar, fasilitas, hargaPerMalam, statusKamar) in cur:
        tree.insert(parent='',index=i,text='',values=(nomorKamar, tipeKamar, luasKamar, fasilitas, hargaPerMalam, statusKamar))
        i = i + 1

    conn.close()

    def kembaliHome():
        from home import homescreen
        homescreen(root)

    KembaliBut = tk.Button(root,text="Kembali ke Menu Utama",font = ("Helvetica", 10, "bold"),bg="#FF595E",command=kembaliHome).place(x = 75, y = 75, width=180, height=50)
    
    root.resizable(False, False)
    root.mainloop()
