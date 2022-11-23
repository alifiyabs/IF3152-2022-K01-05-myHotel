# Riwayat Kamar
# Penanggung jawab: Kyla Aisha 18220093

# Prerequisite: Library tkinter, mariadb
# Prerequisite: Database mariadb dengan nama myhotel
# Notes: Replace ***** dengan password database mariadb (hanya 1 field password)

import sys
import tkinter as tk
import os
from tkinter import ttk
import mariadb

class ClassRiwayat():
    def Riwayat(self, screen):
        global root
        screen.destroy()
        root = tk.Tk()
        root.title("Riwayat Kamar")
        root.geometry('1270x690')
        root.configure(bg='#F7F0F5')
        
        MyHotellabelTitle = tk.Label(root,text="myHotel",font=("helvetica",20,"bold"),bg="#F7F0F5",fg="black").place(x=635,y=100,anchor="center")
        RiwayatlabelTitle = tk.Label(root,text="Riwayat Kamar",font=("helvetica",10,"bold"),bg="#F7F0F5",fg="black").place(x=635,y=140,anchor="center")

        columns = (1,2,3)
        tree = ttk.Treeview(root, height=10, columns=columns, show='headings')
        tree.column(1,width=100)
        tree.column(2,width=100)
        tree.column(3,width=200)
        tree.place(x = 635, y = 220,anchor="n")
        tree.heading(1, text='Nomor Kamar')
        tree.heading(2, text='Total Dipesan')
        tree.heading(3, text='Total Pendapatan Kamar')

        style = ttk.Style()
        style.configure('Treeview',font=("helvetica",10),background='#DECBB7',foreground='black',fieldbackground='#F7F0F5',rowheight=25)
        style.map('Treeview',background=[("selected","#8F857D")],foreground=[("selected","#F7F0F5")])

        try:
            conn = mariadb.connect(
                user='root',
                password='sngshdcb29',
                host='localhost',
                database='myhotel',
                port=3307
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
        
        def kembaliHome():
            from home import ClassHome
            ClassHome().homescreen(root)

        KembaliBut = tk.Button(root,text="Kembali ke Menu Utama",font = ("Helvetica", 10, "bold"),bg="#FF595E",command=kembaliHome).place(x = 75, y = 75, width=180, height=50)

        root.resizable(False, False)
        root.mainloop()
