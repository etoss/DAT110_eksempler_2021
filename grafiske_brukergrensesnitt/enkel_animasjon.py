import tkinter


class EnkelAnimasjon:
    def __init__(self):
        self.hovedvindu = tkinter.Tk()
        self.hovedvindu.title("Enkel egen grafikk")

        self.lerret = tkinter.Canvas(self.hovedvindu, width=600, height=300)

        self.x_posisjon = 10
        self.kula = self.lerret.create_oval(self.x_posisjon, 50, self.x_posisjon+40, 90, fill="green")

        self.hovedvindu.after(20, self.flytt_kula)

        self.lerret.pack()
        tkinter.mainloop()

    def flytt_kula(self):
        self.x_posisjon += 10
        if self.x_posisjon >= 560:
            self.x_posisjon = 10
        self.lerret.coords(self.kula, self.x_posisjon, 50, self.x_posisjon+40, 90)
        self.hovedvindu.after(20, self.flytt_kula)


if __name__ == "__main__":
    gui = EnkelAnimasjon()
