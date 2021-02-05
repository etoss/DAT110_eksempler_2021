linje = input("Skriv inn første linje tekst: ")
resultat = ""
while linje != "":
    resultat += linje + "\n"
    linje = input("Skriv inn neste linje tekst: ")
print(resultat)
