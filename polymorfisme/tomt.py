class Tomt:
    def __init__(self, id, eier, utstrekning, verdi):
        self.id = id
        self.eier = eier
        self.utstrekning = utstrekning
        self.verdi = verdi

    def areal(self):
        return self.utstrekning.areal()

    def kvadratmeterpris(self):
        return self.verdi/self.areal()
