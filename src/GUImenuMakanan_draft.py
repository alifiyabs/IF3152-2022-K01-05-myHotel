import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.title('Menu Makanan')
root.geometry('380x200')

# define columns
columns = ('no', 'id_makanan', 'nama', 'harga')

tree = ttk.Treeview(root, columns=columns, show='headings')

# define headings
tree.heading('no', text='No')
tree.heading('id_makanan', text='ID Makanan')
tree.heading('nama', text='Nama')
tree.heading('harga', text='Harga')

tree.column('no', width=30, anchor=tk.CENTER)
tree.column('id_makanan', width=80, anchor=tk.CENTER)
tree.column('nama', width=150, anchor=tk.CENTER)
tree.column('harga', width=100, anchor=tk.CENTER)

# generate sample data
menus = [('1.', '001', 'Ayam Geprek', 'Rp20.000'),
        ('2.', '002', 'Ayam Penyet', 'Rp20.000'),
        ('3.', '003', 'Tempe', 'Rp2.000')]

# add data to the treeview
for menu in menus:
    tree.insert('', tk.END, values=menu)


def item_selected(event):
    for selected_item in tree.selection():
        item = tree.item(selected_item)
        record = item['values']
        # show a message
        showinfo(title='Information', message=','.join(record))


tree.bind('<<TreeviewSelect>>', item_selected)

tree.grid(row=0, column=0, sticky='nsew')

# add a scrollbar
scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.grid(row=0, column=1, sticky='ns')

# run the app
root.mainloop()