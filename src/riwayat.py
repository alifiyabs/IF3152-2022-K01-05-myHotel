import sys
import tkinter as tk
# from PIL import Image, ImageTk
import os
from tkinter import ttk
# import mysql.connector as mysql
import mariadb


def Riwayat(screen):
    global root
    screen.destroy()
    root = tk.Tk()
    root.title("Riwayat Kamar")
    root.geometry('1270x690')
    root.configure(bg='white')
    
    MyHotellabelTitle = tk.Label(root,text="myHotel",font=("helvetica",20,"bold"),bg="white",fg="black",width=100,anchor='w').place(x=550,y=100)
    RiwayatlabelTitle = tk.Label(root,text="Riwayat Kamar",font=("helvetica",10,"bold"),bg="white",fg="black",width=100,anchor='w').place(x=555,y=140)

    scrollbar = tk.Scrollbar(root)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    columns = (1,2,3)
    tree = ttk.Treeview(root, height=10, columns=columns, show='headings')
    tree.column(1,width=100)
    tree.column(2,width=100)
    tree.column(3,width=200)
    tree.pack(side=tk.BOTTOM,fill=tk.Y,pady=20)
    tree.heading(1, text='Nomor Kamar')
    tree.heading(2, text='Total Dipesan')
    tree.heading(3, text='Total Pendapatan Kamar')

    style = ttk.Style()
    style.configure('Treeview',font=('helvetica,11'),background='lightgrey',foreground='black',fieldbackground='dodgerblue3',rowheight=40)
    style.map('Treeview',background=[('selected','azure4')])

    try:
        conn = mariadb.connect(
            user='root',
            password='***',
            host='localhost',
            database='myhotel'
        )
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)
    
    cur = conn.cursor()
    cur.execute('SELECT * FROM riwayatkamar')

    i=1
    for (nomorKamar, totalDipesan, totalPendapatanKamar) in cur:
        tree.insert(parent='',index=i,text='',values=(nomorKamar, totalDipesan, totalPendapatanKamar))
        i = i + 1

    conn.close()

    scrollbar.config(command = tree.yview)
    # root.resizable(False, False)
    root.mainloop()
