import tkinter
from tkinter import filedialog


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

        tkinter.mainloop()

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
