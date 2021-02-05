# Skriv inn et antall tall, så skal den gjøre 1 + 2 + 3 + ... + antall

antall = int(input("Antall tall: "))
tall = 1
resultat = 0
while tall <= antall:
    resultat += tall
    tall += 1
    print(f"Foreløpig resultat: {resultat}")
print(f"Resultatet ble: {resultat}")
