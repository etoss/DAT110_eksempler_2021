# Versjon av filleser eksemplet som bruker with-blokk i stedet
# for å eksplisitt lukke fila.

max = 0.0
min = 1000.0
sum = 0.0
antall = 0
with open("vindmaalinger.txt", "r") as filreferanse:
    try:
        for linje in filreferanse:
            try:
                tall = float(linje)
                if tall > max:
                    max = tall
                if tall < min:
                    min = tall
                sum += tall
                antall += 1
            except ValueError:
                print("Advarsel: Linje som ikke var et lovlig flyttall!")
        gjennomsnitt = sum/antall
        print(f"Minimum vindtyrke: {min}")
        print(f"Maksimum vindtyrke: {max}")
        print(f"Gjennomsnitt vindtyrke: {gjennomsnitt}")
    except IOError as e:
        print("Feil under lesing av fila " + str(e))
