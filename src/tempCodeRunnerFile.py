def home(layar):
    global screen
    layar.destroy()
    screen = Tk()
    screen.title("myHotel")
    screen.geometry("1270x690")
    screen.config(bg = "white")
    
    global noKamar
    global nomorKamar_var
    noKamar = StringVar()

    # Judul halaman
    showTitle(screen)
    showSectionTitle(screen)

    # Entry box nomor kamar
    Label(screen, text = "Nomor Kamar", font = ("Helvetica", 15, "bold"), bg="white").place(x = 500, y = 220)
    nomorKamar_var = Entry(screen, textvariable = noKamar, font=("Helvetica", 15), bg = "light grey", fg = "black")
    nomorKamar_var.place(x = 500, y = 250, width = 300, height = 30)

    # Button next menuju verifikasi kamar
    Button(screen, text = "Berikutnya", font = ("Helvetica", 15, "bold"), bg="#71BC68", width = 10, height = 1, command = verifyKamar).place(x = 670, y = 320)

    screen.mainloop()