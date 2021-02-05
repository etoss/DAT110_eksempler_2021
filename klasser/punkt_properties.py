import math

class Punkt:
    #Konstruktør
    def __init__(self, start_x=0, start_y=0):
        self.x_koordinat = start_x
        self.y_koordinat = start_y

    def flytt(self, delta_x, delta_y):
        self.x_koordinat += delta_x
        self.y_koordinat += delta_y

    # Bruker en property for x-koordinat for å sørge for at koordinatet ikke kan være
    # negativt
    @property
    def x_koordinat(self):
        return self.__x_koordinat

    @x_koordinat.setter
    def x_koordinat(self, ny_x):
        if ny_x >= 0:
            self.__x_koordinat = ny_x
        else:
            raise ValueError("X-koorinatet i denne applikasjonen kan ikke være negativt!")

    # Properties uten en setter blir read-only, man kan lese dem men ikke sette dem
    # lik noe. R og Theta er også beregnete egenskaper siden de regnes ut
    # fra koordinatene.
    @property
    def r(self):
        return math.sqrt(self.x_koordinat**2 + self.y_koordinat**2)

    @property
    def theta(self):
        return math.acos(self.x_koordinat/self.r)

    def __str__(self):
        return f"Punkt: ({self.x_koordinat}, {self.y_koordinat})"


if __name__ == "__main__":
    p1 = Punkt()
