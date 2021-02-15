# Refaktorering: Endre navngiving og/eller strukturen på koden uten å endre
# hva koden gjør

# Unngå bruk av globale variabler. Det er lettere å ha oversikt når alle
# variablene er lokale i funksjonen

# Fakultet som funksjon. Tar inn et tall som parameter
def fakultet(heltall):
    resultat = 1
    for tall in range(1, heltall + 1):
        resultat *= tall
    return resultat     # Returnerer resultatet til koden som kaller funksjonen
                        # og avslutter funksjonen


# Sjekker om dette er hoved-scriptet eller blir importert, kjører kun hvis dette
# er hoved-scriptet
if __name__ == "__main__":
    fakultet_av = int(input("Fakultet av: "))
    resultat_av_fakultet = fakultet(fakultet_av)
    print(f"Fakultat av {fakultet_av} er {resultat_av_fakultet}")
