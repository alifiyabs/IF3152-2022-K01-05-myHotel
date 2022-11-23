import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.title('Menu Makanan')
root.geometry('1270x690')
root.config(bg = "white")

#tk.Label(root, text = "Menu Makanan", font = ("Helvetica", 20, "bold"), bg="white").place(x = 500, y = 100)
tk.Label(root, text = "myHotel", font = ("Helvetica", 20, "bold"), bg="white").place(x=575,y=40)
tk.Label(root, text="Menu Makanan", font=("helvetica", 10, "bold"), bg="white", fg="black", width=100, anchor='w').place(x=580,y=80)

# define columns
columns = ('no', 'id_makanan', 'nama', 'harga')

tree = ttk.Treeview(root, height=13, columns=columns, show='headings')
tree.pack(side=tk.BOTTOM, pady=20)
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
style.configure("Treeview", font=('helvetica', 12), background="white",foreground="black",fieldbackground='dodgerblue3',rowheight=40)
style.map("Treeview",background=[('selected','azure4')])

# generate sample data
menus = [('1.', '001', 'Ayam Geprek', 'Rp20.000'),
        ('2.', '002', 'Ayam Penyet', 'Rp20.000'),
        ('3.', '003', 'Tempe', 'Rp2.000')]

# add data to the treeview
for menu in menus:
    tree.insert('', tk.END, values=menu)


#def item_selected(event):
    #for selected_item in tree.selection():
        #item = tree.item(selected_item)
        #record = item['values']
        # show a message
        #showinfo(title='Information', message=','.join(record))


#tree.bind('<<TreeviewSelect>>', item_selected)

#tree.grid(row=0, column=0, sticky='nsew')

# add a scrollbar
#scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)
#tree.configure(yscroll=scrollbar.set)
#scrollbar.grid(row=0, column=1, sticky='ns')

# run the app
root.mainloop()