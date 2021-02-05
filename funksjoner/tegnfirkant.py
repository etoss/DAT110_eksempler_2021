# Eksempel på funksjon som tar flere parametere. Denne tar
# tre parametere hvorav den siste har en default-verdi.
# Merk: Funksjoner som ikke har en return setning avslutter når tolkeren
#   når enden av blokken til funksjonen
def lag_firkant_av_tegn(bredde, hoyde, tegn="*"):
    for linje in range(hoyde):
        for tall in range(bredde):
            print(tegn, end="")
        print()


# Eksempel på funksjon som ikke tar noen parametere
def funksjon_uten_parametre():
    print("Test")


# Viser flere kall til funksjonen lag_firkant_av_tegn med ulike
# parametere.
if __name__ == "__main__":
    lag_firkant_av_tegn(6, 4)
    print()
    lag_firkant_av_tegn(5, 6, "#")
    print()
    lag_firkant_av_tegn(3, 5, "%")
    print()
    lag_firkant_av_tegn(8, 7, ".")
    print()
    lag_firkant_av_tegn(tegn="%", bredde=3, hoyde=2)
    print()
    lag_firkant_av_tegn(hoyde=5, bredde=3)

    # Kall til funksjoner uten parametere må fortsatt ha parenteser etter.
    # Dette skiller funksjoner fra variabler
    funksjon_uten_parametre()
