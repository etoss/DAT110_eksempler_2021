import tkinter
from tkinter import messagebox


class HendelsesDemo:
    def __init__(self):
        self.hovedvindu = tkinter.Tk()
        self.lerret = tkinter.Canvas(self.hovedvindu, width=600, height=500)

        self.rektanglet = self.lerret.create_rectangle(0, 0, 600,500, fill="blue")

        self.lerret.bind("<Enter>", self.mus_gaar_inn)
        self.lerret.bind("<Leave>", self.mus_gaar_ut)
        self.lerret.bind("<Button>", self.museklikk)
#        self.hovedvindu.bind("<Shift-Key-Up>", self.shift_key_up)
        self.hovedvindu.bind("<Key>", self.tastetrykk)

        self.lerret.pack()
        tkinter.mainloop()

    def mus_gaar_inn(self, hendelse):
        self.lerret.itemconfig(self.rektanglet, fill="green")

    def mus_gaar_ut(self, hendelse):
        self.lerret.itemconfig(self.rektanglet, fill="blue")

    # Museknapp bind gir hendelser av typen MouseEvent
    def museklikk(self, mushendelse):
        hvilken_knapp = mushendelse.num
        x_koordinat = mushendelse.x
        y_koordinat = mushendelse.y
        messagebox.showinfo("Museklikk", f"Du trykket på knapp {hvilken_knapp} på koordinatene "
                            f"({x_koordinat}, {y_koordinat})")

    def tastetrykk(self, tastehendelse):
        tegn = tastehendelse.char
        tastesymbol = tastehendelse.keysym
        tastekode = tastehendelse.keycode
        messagebox.showinfo("Tastetrykk", f"Tegn {tegn}. Symbol {tastesymbol}. Kode {tastekode}")

    def shift_key_up(self, tastehendelse):
        messagebox.showinfo("Tastetrykk", "Skift pil opp")

if __name__ == "__main__":
    gui = HendelsesDemo()
