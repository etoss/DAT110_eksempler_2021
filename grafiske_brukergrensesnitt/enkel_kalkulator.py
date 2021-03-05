import tkinter


class Kalkulator:
    def __init__(self):
        self.hovedvindu = tkinter.Tk()
        self.tallknappliste, self.tallknappramme = self.lag_tallknapper(self.hovedvindu)
        self.tallknappramme.grid(column=1, row=1, padx=10, pady=10)
        self.funksjonsknappliste, self.funksjonsknappramme = self.lag_funksjonsknapper(self.hovedvindu)
        self.funksjonsknappramme.grid(column=0, row=1, padx=10, pady=10)
        self.operasjonsknappliste, self.operasjonsknappramme = self.lag_operasjonsknapper(self.hovedvindu)
        self.operasjonsknappramme.grid(column=2, row=1, padx=10, pady=10)
        self.tallviser = tkinter.Label(self.hovedvindu, text="1234", anchor=tkinter.E)
        self.tallviser.grid(column=0, row=0, columnspan=3, padx=10, pady=5, sticky=(tkinter.E, tkinter.W))
        self.hovedvindu.title("Kalkulator")
        tkinter.mainloop()

    def lag_funksjonsknapper(self, forelder):
        knapper = list()
        ramme = tkinter.Frame(forelder)
        knapper.append(tkinter.Button(ramme, text="M2"))
        knapper[0].pack()
        knapper.append(tkinter.Button(ramme, text="M1"))
        knapper[1].pack()
        knapper.append(tkinter.Button(ramme, text="C"))
        knapper[2].pack()
        knapper.append(tkinter.Button(ramme, text="="))
        knapper[3].pack()
        return knapper, ramme

    def lag_operasjonsknapper(self, forelder):
        knapper = list()
        ramme = tkinter.Frame(forelder)
        knapper.append(tkinter.Button(ramme, text="+"))
        knapper[0].pack()
        knapper.append(tkinter.Button(ramme, text="-"))
        knapper[1].pack()
        knapper.append(tkinter.Button(ramme, text="*"))
        knapper[2].pack()
        knapper.append(tkinter.Button(ramme, text="/"))
        knapper[3].pack()
        return knapper, ramme

    def lag_tallknapper(self, forelder):
        knapper = list()
        ramme = tkinter.Frame(forelder)
        knapper.append(tkinter.Button(ramme, text="1"))
        knapper[0].grid(column=0, row=0, padx=5, pady=5)
        knapper.append(tkinter.Button(ramme, text="2"))
        knapper[1].grid(column=1, row=0)
        knapper.append(tkinter.Button(ramme, text="3"))
        knapper[2].grid(column=2, row=0)
        knapper.append(tkinter.Button(ramme, text="4"))
        knapper[3].grid(column=0, row=1)
        knapper.append(tkinter.Button(ramme, text="5"))
        knapper[4].grid(column=1, row=1)
        knapper.append(tkinter.Button(ramme, text="6"))
        knapper[5].grid(column=2, row=1)
        knapper.append(tkinter.Button(ramme, text="7"))
        knapper[6].grid(column=0, row=2)
        knapper.append(tkinter.Button(ramme, text="8"))
        knapper[7].grid(column=1, row=2)
        knapper.append(tkinter.Button(ramme, text="9"))
        knapper[8].grid(column=2, row=2)
        knapper.append(tkinter.Button(ramme, text="0"))
        knapper[9].grid(column=0, row=3, columnspan=2, sticky=(tkinter.W, tkinter.E)) # rowspan=1
        knapper.append(tkinter.Button(ramme, text=","))
        knapper[10].grid(column=2, row=3, sticky=(tkinter.W, tkinter.E))
        return knapper, ramme


if __name__ == "__main__":
    gui = Kalkulator()
