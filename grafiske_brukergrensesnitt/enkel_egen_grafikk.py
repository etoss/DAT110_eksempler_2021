import tkinter


class EnkelEgenGrafikk:
    def __init__(self):
        self.hovedvindu = tkinter.Tk()
        self.hovedvindu.title("Enkel egen grafikk")

        self.lerret = tkinter.Canvas(self.hovedvindu, width=600, height=500)
        self.lerret.pack()

        self.lerret.create_line(10, 10, 200, 100)
        self.lerret.create_line(10, 30, 200, 120, width=4, dash=(20, 10, 10, 10), fill="red")

        self.lerret.create_line(10, 50, 200, 140, width=4, dash=(20, 10, 10, 10), fill="#7777FF")

        self.lerret.create_rectangle(50, 50, 200, 200, outline="red", width=3)

        self.lerret.create_rectangle(10, 250, 300, 490, fill="white", outline="blue", width=4)

        self.lerret.create_oval(300, 10, 400, 210)
        self.lerret.create_arc(400, 10, 500, 110, start=0, extent=90, style=tkinter.PIESLICE)

        self.lerret.create_polygon(350, 400, 400, 350, 450, 350, 500, 400, 450, 450, 400, 450, fill="green")

        self.lerret.create_text(60, 220, text="Tester tekst i lerret")

        tkinter.mainloop()


if __name__ == "__main__":
    gui = EnkelEgenGrafikk()
