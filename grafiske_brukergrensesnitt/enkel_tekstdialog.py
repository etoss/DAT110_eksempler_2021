import tkinter
from tkinter import messagebox


class Tekstdialog:
    def __init__(self, forelder, sporsmaal):
        self.vindu = tkinter.Toplevel(forelder)

        self.sporsmaal = tkinter.Label(self.vindu, text=sporsmaal)
        self.sporsmaal.pack(side=tkinter.LEFT)
        self.tekstfelt = tkinter.Entry(self.vindu, width=20)
        self.tekstfelt.pack(side=tkinter.LEFT)
        self.ok = tkinter.Button(self.vindu, text="OK", command=self.ok_funksjon)
        self.ok.pack(side=tkinter.LEFT)
        self.cancel = tkinter.Button(self.vindu, text="Cancel", command=self.cancel_funksjon)
        self.cancel.pack(side=tkinter.LEFT)

        self.resultat = None

    def ok_funksjon(self):
        self.resultat = self.tekstfelt.get()
        self.vindu.destroy()

    def cancel_funksjon(self):
        self.vindu.destroy()


def vis_tekstdialog(sporsmaal, forelder=None):
    dialogen = Tekstdialog(forelder, sporsmaal)
    dialogen.vindu.wait_window()
    return dialogen.resultat


class DemoGUI:
    def __init__(self):
        self.hovedvindu = tkinter.Tk()
        self.dialogviser = tkinter.Button(self.hovedvindu, text="Vis dialog",
                                          command=self.dialogviser_funksjon)
        self.dialogviser.pack()
        tkinter.mainloop()

    def dialogviser_funksjon(self):
        resultatet = vis_tekstdialog("Spørsmålet", self.hovedvindu)
        if resultatet is not None:
            messagebox.showinfo("Resultat", resultatet)
        else:
            messagebox.showinfo("Resultat", "Avbrutt av brukeren")


if __name__ == "__main__":
    gui = DemoGUI()
