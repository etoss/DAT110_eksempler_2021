# Refaktorering
# Unngå bruk av globale variabler

# Funksjonen "fakultet" er fra eksemplet i temaet "funksjoner"
def fakultet(heltall):
    resultat = 1
    for tall in range(1, heltall + 1):
        resultat *= tall
    return resultat


# Funksjon som leser inn input fra brukeren og håndterer at brukeren skriver
# inn noe som ikke er et lovlig heltall. Kjernen i dette eksemplet.
def les_ikke_negativt_heltall_fra_bruker(beskjed):
    ferdig = False
    while not ferdig:
        try:
            fakultet_av = int(input(beskjed))
            if fakultet_av < 0:
                print("Du kan ikke ha et negativt tall! Prøv på nytt!")
            else:
                ferdig = True
                return fakultet_av
        # Håndterer at brukeren ikke skreiv inn et lovlig heltall
        except ValueError:
            print("Det du skreiv inn er ikke et lovlig heltall! Prøv på nytt!")


# Sjekker om dette er hoved-scriptet eller blir importert, kjører kun hvis dette
# er hoved-scriptet
if __name__ == "__main__":
    fakultet_av = les_ikke_negativt_heltall_fra_bruker("Fakultet av: ")
    resultat_av_fakultet = fakultet(fakultet_av)
    print(f"Fakultat av {fakultet_av} er {resultat_av_fakultet}")
