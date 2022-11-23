import sys
from tkinter import *
from tkinter import ttk, messagebox
from datetime import date
from home import Home
import tkinter as tk
import datetime
import os
import mariadb

class Login():
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

        Label(screen, text = "Username", font = ("Helvetica", 12, "bold"), bg="#F7F0F5").place(x = 485, y = 220)
        username_var = Entry(screen, textvariable = username, font=("Helvetica", 12), bg = "#DECBB7", fg = "black")
        username_var.place(x = 635, y = 250, width = 300, height = 30,anchor="n")

        Label(screen, text = "Password", font = ("Helvetica", 12, "bold"), bg="#F7F0F5").place(x = 485, y = 300)
        password_var = Entry(screen, textvariable = password, show ="*", font=("Helvetica", 12), bg = "#DECBB7", fg = "black")
        password_var.place(x = 635, y = 330, width = 300, height = 30,anchor="n")

        Button(screen, text = "Login", font = ("Helvetica", 12, "bold"), bg="#DECBB7", width = 10, height = 1, command = self.verifyLogin).place(x = 635, y = 390,anchor="n")
        screen.resizable(False,False)
        screen.mainloop()

    def verifyLogin(self):
        if (username.get() == "admin" and password.get() == "hotel123"):
            home_var = ClassHome()
            home_var.homescreen(screen)
        else:
            Label(screen, text = "Username atau password salah!", fg = "red", font = ("Helvetica, 12")).pack()
