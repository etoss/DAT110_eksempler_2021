import tkinter
from klasser.punkt_properties import Punkt


class Linjetegner:
    def __init__(self):
        self.hovedvindu = tkinter.Tk()
        self.hovedvindu.title("Enkel egen grafikk")

        self.lerret = tkinter.Canvas(self.hovedvindu, width=600, height=500)
        self.lerret.pack()
        self.punktliste = list()

        self.lerret.bind("<Button>", self.tegne_lytter)

        tkinter.mainloop()

    def tegne_lytter(self, musehendelse):
        self.lerret.create_oval(musehendelse.x-2, musehendelse.y-2, musehendelse.x+2, musehendelse.y+2, fill="black")
        if len(self.punktliste) > 0:
            forrige_punkt = self.punktliste[-1]
            self.lerret.create_line(forrige_punkt.x_koordinat, forrige_punkt.y_koordinat, musehendelse.x,
                                    musehendelse.y)
        self.punktliste.append(Punkt(musehendelse.x, musehendelse.y))


if __name__ == "__main__":
    gui = Linjetegner()
