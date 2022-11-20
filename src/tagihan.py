import src.checkOut

import sys 
import mariadb

import tkinter as tk

def test():
    # Connect to MariaDB Platform
    # global noKamar
    # global nomorKamar_var
    # noKamar = StringVar()

    try:
        conn = mariadb.connect(
            user = "root",
            password = "",
            host = "localhost",
            port = 3306,
            database = "myhotel"
        )
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

    # Get Cursor
    cur = conn.cursor()
    try:
        noKamar = int(input("Masukkan nomor kamar = "))
        statement = f"SELECT hargaPerMalam FROM informasikamar WHERE nomorKamar = '{noKamar}'"
        # data = (int(noKamar.get()))
        # print(f"SELECT hargaPerMalam FROM informasikamar WHERE nomorKamar = '{noKamar}'")
        # data = (int(input("Masukkan nomor kamar = ")))
        data = (noKamar,)
        print("statementnya = ", statement)
        cur.execute(statement, data)
        print('o')
        row = cur.fetchone()
        if (row == None):
            print("Kamar invalid")
        else:
            print("masuk else")
            for x in row:
                biayaKamar = x
            print(biayaKamar)
    
    except mariadb.Error as e:
        print(f"Error retrieving entry form database: {e}")

    conn.close()

test()