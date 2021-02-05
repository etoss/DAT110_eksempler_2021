#Oppgaven: Ønsker å regne ut arealet til rom hvor brukeren oppgir lengde og bredde

#Pseudokode
# Be brukeren om lengde
# Be brukeren om bredde
# Regn ut arealet
# Skriv ut arealet

lengde_streng = input("Lengden til rommet i meter: ")
lengde_flyttall = float(lengde_streng)
bredde_streng = input("Bredden til rommet i meter: ")
bredde_flyttall = float(bredde_streng)
areal = lengde_flyttall * bredde_flyttall
areal_avrundet = round(areal, 3)
print("Arealet ble: " + str(areal_avrundet))
