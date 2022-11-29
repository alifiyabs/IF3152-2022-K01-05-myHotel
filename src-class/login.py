import sys
from tkinter import *
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
from datetime import date
from home import ClassHome
import tkinter as tk
import datetime
import os
import mariadb

pathToImg = os.path.abspath('.') + '/img'

class ClassLogin():
    def homeLogin(self, layar):
        global screen
        layar.destroy()
        screen = Tk()
        screen.title("myHotel")
        screen.geometry("1270x690")
        screen.config(bg = "#F7F0F5")

        MyHotellabelTitle = tk.Label(screen,text="myHotel",font=("helvetica",20,"bold"),bg="#F7F0F5",fg="black").place(x=635,y=100,anchor="center")
        RiwayatlabelTitle = tk.Label(screen,text="Login",font=("helvetica",10,"bold"),bg="#F7F0F5",fg="black").place(x=635,y=140,anchor="center")
        
        global username
        global username_var
        global password
        global password_var
        username = StringVar()
        password = StringVar()

         # Insert img login
        framelogin = Frame(screen, width=600, height=690)
        framelogin.grid(row = 0, column = 0)
        imglogin = PhotoImage(file=pathToImg+'/Login.png')
        label = Label(framelogin, image=imglogin)
        label.grid(row = 0, column = 0)

        # Create frame untuk input login (username, password)
        frameinput = Frame(screen, bg="#F7F0F5", width=670, height=690)
        frameinput.grid(row = 0, column= 2, padx=(235,0))

        # Judul myHotel dan Login
        MyHotellabelTitle = tk.Label(frameinput,text="myHotel",font=("Inter",20,"bold"),bg="#F7F0F5",fg="black").grid(row = 0, column = 2,pady=(0,10))
        RiwayatlabelTitle = tk.Label(frameinput,text="Login",font=("Inter",15,"bold"),bg="#F7F0F5",fg="black").grid(row = 1, column = 2,pady=(0,30))

        # Username
        Label(frameinput, text = "Username", font = ("Inter", 12, "bold"), bg="#F7F0F5").grid(row = 2, column = 2, pady=(0,5))
        username_var = Entry(frameinput, textvariable = username, font=("Inter", 12), bg = "#DECBB7", fg = "black")
        username_var.grid(row = 3, column= 2, pady=(0,20))
        
        # Password
        Label(frameinput, text = "Password", font = ("Inter", 12, "bold"), bg="#F7F0F5").grid(row = 4, column=2,pady=(0,5))
        password_var = Entry(frameinput, textvariable = password, show ="*", font=("Inter", 12), bg = "#DECBB7", fg = "black")
        password_var.grid(row = 5, column = 2,pady=(0,30))

        # Button login
        Button(frameinput, text = "Login", font = ("Inter", 12, "bold"), bg="#DECBB7", width = 10, height = 1, command = self.verifyLogin).grid(row= 6, column=2)
        screen.resizable(False,False)
        screen.mainloop()

    def verifyLogin(self):
        if (username.get() == "admin" and password.get() == "hotel123"):
            home_var = ClassHome()
            home_var.homescreen(screen)
        else:
            Label(screen, text = "Username atau password salah!", fg = "red", font = ("Helvetica, 12")).pack()