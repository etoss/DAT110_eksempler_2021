import tkinter
from tkinter import filedialog
from tkinter import font

TIMES = 1
ARIAL = 2
COURIER = 3

class EnkelTeksteditor:
    def __init__(self):
        self.hovedvindu = tkinter.Tk()
        self.tekstomraadet = tkinter.Text(self.hovedvindu, height=10, width=30)
        self.tekstomraadet.grid(column=0, row=0)
        self.scrollbar = tkinter.Scrollbar(self.hovedvindu, orient=tkinter.VERTICAL,
                                           command=self.tekstomraadet.yview)
        self.scrollbar.grid(column=1, row=0, sticky=(tkinter.N, tkinter.S))
        self.tekstomraadet.config(yscrollcommand=self.scrollbar.set)
        self.hovedvindu.title("Enkel teksteditor")

        self.hovedmeny = tkinter.Menu(self.hovedvindu)
        self.hovedvindu.config(menu=self.hovedmeny)
        self.hovedvindu.option_add("*tearOff", False)

        self.filmeny = tkinter.Menu(self.hovedvindu)
        self.hovedmeny.add_cascade(menu=self.filmeny, label="Fil")
        self.redigermeny = tkinter.Menu(self.hovedvindu)
        self.hovedmeny.add_cascade(menu=self.redigermeny, label="Rediger")

        self.filmeny.add_command(label="Åpne", command=self.aapne_valg)
        self.filmeny.add_command(label="Lagre", command=self.lagre_valg)
        self.filmeny.add_command(label="Lukk")

        self.redigermeny.add_command(label="Klipp ut")
        self.redigermeny.add_command(label="Kopier")
        self.redigermeny.add_command(label="Lim inn")

        self.knappramme = tkinter.Frame(self.hovedvindu)
        self.knappramme.grid(column=2, row=0)

        self.bold_var = tkinter.BooleanVar()
        self.bold_checkbutton = tkinter.Checkbutton(self.knappramme, text="Bold",
                                                    variable=self.bold_var, command=self.endre_font)
        self.bold_checkbutton.pack()

        self.italic_var = tkinter.BooleanVar()
        self.italic_checkbutton = tkinter.Checkbutton(self.knappramme, text="Italic",
                                                    variable=self.italic_var, command=self.endre_font)
        self.italic_checkbutton.pack()

        self.font_var = tkinter.IntVar(value=TIMES)
        self.times = tkinter.Radiobutton(self.knappramme, text="Times new roman",
                                         variable=self.font_var, value=TIMES, command=self.endre_font)
        self.times.pack()
        self.arial = tkinter.Radiobutton(self.knappramme, text="Arial",
                                         variable=self.font_var, value=ARIAL, command=self.endre_font)
        self.arial.pack()
        self.courier = tkinter.Radiobutton(self.knappramme, text="Courier New",
                                         variable=self.font_var, value=COURIER, command=self.endre_font)
        self.courier.pack()

        self.fontlistbox = tkinter.Listbox(self.hovedvindu, selectmode=tkinter.SINGLE)
        self.fontene = font.families()
        for fonten in self.fontene:
            self.fontlistbox.insert(tkinter.END, fonten)
        self.fontlistbox.grid(column=3, row=0, sticky=(tkinter.N, tkinter.S))

        self.fontscroller = tkinter.Scrollbar(self.hovedvindu, orient=tkinter.VERTICAL,
                                              command=self.fontlistbox.yview)
        self.fontlistbox.config(yscrollcommand=self.fontscroller.set)
        self.fontscroller.grid(column=4, row=0, sticky=(tkinter.N, tkinter.S))

        self.fontlistbox.bind("<Double-Button-1>", self.endre_font_listbox)
        self.fontlistbox.bind("<Key-Return>", self.endre_font_listbox)

        tkinter.mainloop()

    def endre_font(self):
        if self.bold_var.get():
            bold_tekst = "bold"
        else:
            bold_tekst = "normal"
        if self.italic_var.get():
            italic_tekst = "italic"
        else:
            italic_tekst = "roman"
        if self.font_var.get() == TIMES:
            font_tekst = "Times New Roman"
        if self.font_var.get() == ARIAL:
            font_tekst = "Arial"
        if self.font_var.get() == COURIER:
            font_tekst = "Courier New"
        ny_font = font.Font(size=10, weight=bold_tekst, slant=italic_tekst, family=font_tekst)
        self.tekstomraadet.config(font=ny_font)

    def endre_font_listbox(self, hendelse):
        if self.bold_var.get():
            bold_tekst = "bold"
        else:
            bold_tekst = "normal"
        if self.italic_var.get():
            italic_tekst = "italic"
        else:
            italic_tekst = "roman"
        valgte_indekser = self.fontlistbox.curselection()
        font_tekst = self.fontene[valgte_indekser[0]]
        ny_font = font.Font(size=10, weight=bold_tekst, slant=italic_tekst, family=font_tekst)
        self.tekstomraadet.config(font=ny_font)

    def aapne_valg(self):
        with filedialog.askopenfile() as fila:
            self.tekstomraadet.delete(0.0, tkinter.END)
            self.tekstomraadet.insert(tkinter.END, fila.read())

    def lagre_valg(self):
        with filedialog.asksaveasfile() as fila:
            teksten = self.tekstomraadet.get(0.0, tkinter.END)
            fila.write(teksten)


if __name__ == "__main__":
    gui = EnkelTeksteditor()
