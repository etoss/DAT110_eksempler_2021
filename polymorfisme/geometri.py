import math


def avstand(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)


def overlapper(sirkel_1, sirkel_2):
    if sirkel_1.radius+sirkel_2.radius > avstand(sirkel_1.senter_x_koordinat, sirkel_1.senter_y_koordinat,
                                                 sirkel_2.senter_x_koordinat, sirkel_2.senter_y_koordinat):
        return True
    else:
        return False


# Grensesnitt Flyttbar
class Flyttbar:
    # Flytt metoden skal flytte objektet det oppgitte antall plasser
    # i x- og y-retning
    def flytt(self, delta_x, delta_y):
        pass


class Sirkel:
    def __init__(self, senter_x_koordinat, senter_y_koordinat, radius):
        self.senter_x_koordinat = senter_x_koordinat
        self.senter_y_koordinat = senter_y_koordinat
        self.radius = radius

    def flytt(self, delta_x, delta_y):
        self.senter_x_koordinat += delta_x
        self.senter_y_koordinat += delta_y

    def areal(self):
        return math.pi*self.radius*self.radius

    def overlapper(self, annen_sirkel):
        if self.radius+annen_sirkel.radius > avstand(self.senter_x_koordinat, self.senter_y_koordinat,
                                    annen_sirkel.senter_x_koordinat, annen_sirkel.senter_y_koordinat):
            return True
        else:
            return False

    def avstand(self, annen_sirkel):
        if self.overlapper(annen_sirkel):
            return 0.0
        return avstand(self.senter_x_koordinat, self.senter_y_koordinat,
                    annen_sirkel.senter_x_koordinat, annen_sirkel.senter_y_koordinat) \
               - (self.radius + annen_sirkel.radius)

    def __str__(self):
        return f"Sirkel med senter ({self.senter_x_koordinat}, {self.senter_y_koordinat}) og radius {self.radius}"

    def er_inni(self, annen_sirkel):
        if self.radius > avstand(self.senter_x_koordinat, self.senter_y_koordinat,
                    annen_sirkel.senter_x_koordinat, annen_sirkel.senter_y_koordinat) + annen_sirkel.radius:
            return True
        else:
            return False

    def __eq__(self, annen_sirkel):
        if self.senter_x_koordinat != annen_sirkel.senter_x_koordinat:
            return False
        if self.senter_y_koordinat != annen_sirkel.senter_y_koordinat:
            return False
        if self.radius != annen_sirkel.radius:
            return False
        return True


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

    def __eq__(self, other):
        if not isinstance(other, Punkt):
            return False
        if self.x_koordinat == other.x_koordinat and self.y_koordinat == other.y_koordinat:
            return True
        return False


# startpunkt og sluttpunkt er ment å være Punkt objekter
class Linjesegment:
    def __init__(self, startpunkt, sluttpunkt):
        self.startpunkt = startpunkt
        self.sluttpunkt = sluttpunkt

    def flytt(self, delta_x, delta_y):
        self.startpunkt.flytt(delta_x, delta_y)
        self.sluttpunkt.flytt(delta_x, delta_y)

    def __str__(self):
        resultat = "Linjesegment: \n"
        resultat += str(self.startpunkt) + "\n"
        resultat += str(self.sluttpunkt) + "\n"
        return resultat

    def grunn_kopi(self):
        return Linjesegment(self.startpunkt, self.sluttpunkt)

    def dyp_kopi(self):
        startpunkt_kopi = Punkt(self.startpunkt.x_koordinat, self.startpunkt.y_koordinat)
        sluttpunkt_kopi = Punkt(self.sluttpunkt.x_koordinat, self.sluttpunkt.y_koordinat)
        return Linjesegment(startpunkt_kopi, sluttpunkt_kopi)


class Rektangel:
    def __init__(self, start_x, start_y, bredde, hoyde):
        self.start_x = start_x
        self.start_y = start_y
        self.hoyde = hoyde
        self.bredde = bredde

    def areal(self):
        return self.bredde*self.hoyde

    def flytt(self, delta_x, delta_y):
        self.start_x += delta_x
        self.start_y += delta_y

    # Endrer høyde og bredde på en slik måte at areal forblir det samme
    def strekk(self, multiplikator):
        self.bredde *= multiplikator
        self.hoyde /= multiplikator

    def __str__(self):
        return f"Rektangel fra ({self.start_x},  {self.start_y}), " \
            f"bredde {self.bredde}, høyde {self.hoyde}"


# Funksjon som tar inn ei liste med geometriske former og flytter alle samme delta_x
# og delta_y
#
# Hva krever funksjonen egentlig?
# Den krever at alle objektene i lista støtter/har flytt metoden
#
# Grensesnitt: Flyttbar. Klassen til objektet har metoden
#   flytt(delta_x, delta_y) som flytter objektet den oppgitte distansen i x- og y-
#   retning
def flytt_former(geometriske_former, delta_x, delta_y):
    for form in geometriske_former:
        form.flytt(delta_x, delta_y)


# Krever at hver form ar en metode areal som ikke tar noen parametre og
# returnererer et flyttall som representerer arelaet til formen.
def totalt_areal(liste_av_former):
    forelopig_total = 0.0
    for form in liste_av_former:
        forelopig_total += form.areal()
    return forelopig_total


if __name__ == "__main__":
    p1 = Punkt(2, 2)
    linje = Linjesegment(Punkt(3, 3), Punkt(2, 8))
    p2 = Punkt(0, 10)
    rektangel = Rektangel(5, 5, 6, 4)
    sirkel = Sirkel(20, 20, 4)
    liste = list()
    liste.append(p1)
    liste.append(linje)
    liste.append(p2)
    liste.append(rektangel)
    liste.append(sirkel)
#    liste.append("Test")
    for element in liste:
        print(element)
    flytt_former(liste, 5, 0)
    print()
    for element in liste:
        print(element)
    areal_liste = list()
    areal_liste.append(rektangel)
    areal_liste.append(sirkel)
    print(totalt_areal(areal_liste))

