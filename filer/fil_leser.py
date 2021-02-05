#Filer
#   Tekstfiler
#      CSV - comma-separated values
#   Binærfiler

#Modus
#   r - ønsker å lese fila (Read)
#   w - ønsker å skrive fila, ønsker å slette ei eventuell gammel fil (Write)
#   a - Ønsker å skrive fila, legger til på slutten hvis den finnes (Append)
#   x - Ønsker å skrive fila, feiler om fila allerede finnes

# Objekt
#  Inneholder tilstand og metoder.
#
#  Metode: Funksjon som du bruker på et objekt og
#  som gjør ting med objektet

# Eksempel: Leser inn ei fil med flyttall (vindmålinger) og finner gjennomsnitt,
# høyeste verdi og laveste verdi.
max = 0.0
min = 1000.0
sum = 0.0
antall = 0
try:
    filreferanse = None
    filreferanse = open("vindmaalinger.txt", "r")
    for linje in filreferanse:
        tall = float(linje)
        if tall > max:
            max = tall
        if tall < min:
            min = tall
        sum += tall
        antall += 1
    gjennomsnitt = sum/antall
    print(f"Minimum vindtyrke: {min}")
    print(f"Maksimum vindtyrke: {max}")
    print(f"Gjennomsnitt vindtyrke: {gjennomsnitt}")
except IOError:
    print("Feil under lesing av fil")
except ValueError:
    print("Feil format")
finally:
    if filreferanse:
        filreferanse.close()
