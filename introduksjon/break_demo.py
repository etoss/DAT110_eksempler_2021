#break: Avbryter ei løkke midt i

resultat = ""
while True:
    linje = input("Skriv inn neste linje tekst: ")
    if linje == "":
        break
    resultat += linje + "\n"
print(resultat)
