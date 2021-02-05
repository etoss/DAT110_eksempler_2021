print("Test", end=" ")
print("En test til")
print("Tredje test")
print("Tester linjeskift. \nDette kommer på ei ny linje. \n\tEtter tabulator")
print("Spesialtegn: \" \\ ")

tall = 5/3
test = "to"
streng = format(tall, "8.4f")   #Formaterer flyttallet "tall" med 8 siffer hvorav 4 bak komma. Runder av normalt.
print(streng)

#f-streng. Kan inkludere variabler fra scriptet i klammeparenteser
# Kan formatere variabelen med kolon og så formateringskoder som for format funksjonen
print(f"Tallet er: {tall:8.4f} og strengen er {test}")

# Formateringskoder
#   5.2f: Flyttall med 5 siffer (inkludert kommaet), hvorav 2 er bak komma.
#   8d: Heltall på vanlig format hvor den setter av 8 siffer

