import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.title("Pesan Makanan")
root.geometry('1270x690')
root.config(bg = "white")

tk.Label(root, text = "myHotel", font = ("Helvetica", 20, "bold"), bg="white").place(x=575,y=40)
tk.Label(root, text="Pesan Makanan", font=("Helvetica", 10, "bold"), bg="white", fg="black", width=100, anchor="w").place(x=580,y=80)

tk.Label(root, text="Masukkan Nomor Kamar", font=("Helvetica", 15), bg="white", fg="black", width=100, anchor="w").place(x=525,y=200)
e1 = tk.Entry(root, font=("Helvetica", 12), bg="light grey", fg="black")
e1.place(x=545,y=240)

# add empty label in row 0 and column 0
#l1 = tk.Label(root, text='     \n   ')
#l1.grid(column=0, row=2)

btn = tk.Button(root, text = "Pesan Makanan", bd='2', command=root.destroy)
btn.place(x=588,y=280)

root.mainloop()

