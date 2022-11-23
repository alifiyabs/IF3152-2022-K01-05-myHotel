import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.title('Menu Makanan')
root.geometry('1270x690')
root.config(bg = "white")

#tk.Label(root, text = "Menu Makanan", font = ("Helvetica", 20, "bold"), bg="white").place(x = 500, y = 100)
tk.Label(root, text = "myHotel", font = ("Helvetica", 20, "bold"), bg="white").place(x=575,y=40)
tk.Label(root, text="Menu Makanan", font=("Helvetica", 10, "bold"), bg="white", fg="black", width=100, anchor='w').place(x=580,y=80)

# define columns
columns = ('no', 'id_makanan', 'nama', 'harga')

tree = ttk.Treeview(root, height=8, columns=columns, show='headings')
#tree.pack(side=tk.LEFT, pady=20)
tree.place(x=300,y=200)
#tree.pack(fill=tk.X)

# define headings
tree.heading('no', text='No')
tree.heading('id_makanan', text='ID Makanan')
tree.heading('nama', text='Nama')
tree.heading('harga', text='Harga')

tree.column('no', width=30, anchor=tk.CENTER)
tree.column('id_makanan', width=80, anchor=tk.CENTER)
tree.column('nama', width=150, anchor=tk.CENTER)
tree.column('harga', width=100, anchor=tk.CENTER)

# Style Treeview
style = ttk.Style()
style.configure("Treeview", font=('Helvetica', 12), background="white",foreground="black",fieldbackground='dodgerblue3',rowheight=40)
style.map("Treeview",background=[('selected','azure4')])

# generate sample data
menus = [('1.', '001', 'Ayam Geprek', 'Rp20.000'),
        ('2.', '002', 'Ayam Penyet', 'Rp20.000'),
        ('3.', '003', 'Tempe', 'Rp2.000')]

# add data to the treeview
for menu in menus:
    tree.insert('', tk.END, values=menu)

tk.Label(root, text="Masukkan Harga Makanan", font=("Helvetica", 15), bg="white", fg="black", width=100, anchor="w").place(x=725,y=275)
e1 = tk.Entry(root, font=("Helvetica", 12), bg="light grey", fg="black")
e1.place(x=745,y=315)

btn = tk.Button(root, text = "Pesan", bd='2', command=root.destroy)
btn.place(x=820,y=355)

btn = tk.Button(root, text = "Selesai Pesan", bd='2', command=root.destroy)
btn.place(x=800,y=385)

root.mainloop()