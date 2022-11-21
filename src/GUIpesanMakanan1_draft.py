import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.title('Pesan Makanan')
root.geometry('380x200')

# add empty label in row 0 and column 0
l0 = tk.Label(root, text='\n')
l0.grid(column=0, row=0)

tk.Label(root, text='Masukkan Nomor Kamar').grid(row=0, column=1)
#tk.Label(root, text='Last Name').grid(row=1)
e1 = tk.Entry(root)
#e2 = tk.Entry(root)
e1.grid(row=1, column=1)
#e2.grid(row=1, column=1)

# add empty label in row 0 and column 0
l1 = tk.Label(root, text='     \n   ')
l1.grid(column=0, row=2)

btn = tk.Button(root, text = 'Pesan Makanan', bd='2', command=root.destroy)
btn.grid(row=3, column=1)

root.mainloop()

