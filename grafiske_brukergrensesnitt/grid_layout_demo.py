import tkinter


class Kalkulator:
    def __init__(self):
        self.hovedvindu = tkinter.Tk()
        self.knapper = list()
        self.knapper.append(tkinter.Button(self.hovedvindu, text="1"))
        self.knapper[0].grid(column=0, row=0, padx=5, pady=5)
        self.knapper.append(tkinter.Button(self.hovedvindu, text="2"))
        self.knapper[1].grid(column=1, row=0)
        self.knapper.append(tkinter.Button(self.hovedvindu, text="3"))
        self.knapper[2].grid(column=2, row=0)
        self.knapper.append(tkinter.Button(self.hovedvindu, text="4"))
        self.knapper[3].grid(column=0, row=1)
        self.knapper.append(tkinter.Button(self.hovedvindu, text="5"))
        self.knapper[4].grid(column=1, row=1)
        self.knapper.append(tkinter.Button(self.hovedvindu, text="6"))
        self.knapper[5].grid(column=2, row=1)
        self.knapper.append(tkinter.Button(self.hovedvindu, text="7"))
        self.knapper[6].grid(column=0, row=2)
        self.knapper.append(tkinter.Button(self.hovedvindu, text="8"))
        self.knapper[7].grid(column=1, row=2)
        self.knapper.append(tkinter.Button(self.hovedvindu, text="9"))
        self.knapper[8].grid(column=2, row=2)
        self.knapper.append(tkinter.Button(self.hovedvindu, text="0"))
        self.knapper[9].grid(column=0, row=3, columnspan=2, sticky=(tkinter.W, tkinter.E)) # rowspan=1
        self.knapper.append(tkinter.Button(self.hovedvindu, text=","))
        self.knapper[10].grid(column=2, row=3, sticky=(tkinter.W, tkinter.E))
        self.hovedvindu.title("Talltastatur")
        tkinter.mainloop()


if __name__ == "__main__":
    gui = Kalkulator()
