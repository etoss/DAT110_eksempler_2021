import tkinter


class BasisGUI:
    def __init__(self):
        self.hovedvindu = tkinter.Tk()
        self.etikett = tkinter.Label(self.hovedvindu, text="Ekko eksempel")
        self.etikett.pack(side=tkinter.LEFT)
        self.tekstfelt = tkinter.Entry(self.hovedvindu, width=10)
        self.tekstfelt.pack(side=tkinter.LEFT)
        self.ekko_strengvariabel = tkinter.StringVar()
        self.ekko_strengvariabel.set("Her kommer ekkoet etter hvert")
        self.knappen = tkinter.Button(self.hovedvindu, text="Lag Ekko", command=self.haandter_ekkoknapp)
        self.knappen.pack(side=tkinter.LEFT)
        self.ekkofelt = tkinter.Label(self.hovedvindu, textvariable=self.ekko_strengvariabel)
        self.ekkofelt.pack(side=tkinter.LEFT)
        self.hovedvindu.title("Enkelt GUI eksempel: Ekko")
        tkinter.mainloop()

    def haandter_ekkoknapp(self):
        teksten = self.tekstfelt.get()
        self.ekko_strengvariabel.set(teksten)
        print("Ekko")


if __name__ == "__main__":
    gui = BasisGUI()
    print("Programmet avslutter")
