# Eksempel: Lar brukeren skrive inn mange linjer tekst og lagrer
# dette til fil

filnavn = input("Hva skal fila hete? ")
filnavn += ".txt"

with open(filnavn, "w", encoding="UTF-8") as filreferanse:
    linje = input("Skriv inn første linje tekst: ")
    while linje != "":
        filreferanse.write(linje + "\n")
        linje = input("Skriv inn neste linje tekst: ")
