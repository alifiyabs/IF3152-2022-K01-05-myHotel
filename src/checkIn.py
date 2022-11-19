# Check In
# Penanggung Jawab: 18220069 Alifiya Brizita Shary


import sys
import datetime
import tkinter as tk
from tkinter import *
import mysql.connector
import os

nikPelanggan = int

nikPelanggan = input("Masukkan nikPelanggan: ")
nomorKamar = input("Masukkan Nomor Kamar: ")

class CheckIn:

    def __init__(checkIn, inNIKPelanggan, inNomorKamar):
        checkIn.NIKPelanggan = inNIKPelanggan
        checkIn.nomorKamar = inNomorKamar

    # Getter

    def getIdCheckIn(self):

        return self.idCheckIn
        # Karena tipe data idCheckIn serial jadi dia nambah + 1 sendiri di databasenya begituh
        # Jadi pada fungsi ini berniat memanggil saja nomor id Check Innya pada database ceunah

    #  Setter

    def setTanggalCheckIn(self):

        print(str(self.datetime.date.today()))

    # bookingCheckIn
    # checkInWalkIn
    # addDataPelanggan -> khusus checkInWalkIn
    # updateStatusKamar -> otomatis

    # Instance Display

    def displayPesanan(checkIn):
        print("Nomor Kamar:" + str(checkIn.nomorKamar))
        print("NIK Pelanggan:" + str(checkIn.nomorKamar))
        print("Status Kamar:") # Ini harusnya ditambah status kamar yang diambil dari database


detailPesanan = []

def showPesanan(list):
    print("Detail Pesanan Pelanggan:")
    for pesananPelanggan in list:
        pesananPelanggan.displayPesanan()



pesanan = CheckIn(nikPelanggan, nomorKamar)
print(pesanan.__dict__)