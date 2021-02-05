print("Skriv inn tekst. Avslutt med tom linje:")
linje = input("> ")
resultat = ""
while linje != "":
    resultat += linje + "\n"
    linje = input("> ")
print(resultat)
