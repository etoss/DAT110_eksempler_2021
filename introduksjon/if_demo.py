# Eksempel 1: Ber brukeren om et tall og sjekker om det er
# negativt

# Ber brukeren on et tall
tall_streng = input("Skriv inn et tall: ")

# Konverterer fra streng til flyttall
tall = float(tall_streng)

# Hvis tallet er mindre enn 0, utfør blokken
if tall < 0.0:
    print("Tallet er lavere enn 0")
    print("Tester ei linje til")

# Hvis tallet ikke er mindre enn 0, sjekk om det er 0 og utfør blokken under hvis det er 0
elif tall == 0.0:
    print("Tallet er eksakt 0")

# Hvis ingen av de foregående slår til, kjør blokken under
else:
    print("Tallet er høyere enn 0")
    print("Tester.....")

# Kjøres uansett hva som skjer i if-setningen siden det ikke er med i samme blokk
print("Avslutter")


#Eksempel 2: Ta inn en alder og sjekk aom personen er tenåring: tallet er mellom 13 og 19

tall_streng = input("Skriv inn en alder: ")
tall = float(tall_streng)

# Bruker "and" for å ha to betingelser som begge må være sanne.
if tall >= 13 and tall <= 19:
    print("Personen er tenåring")
