import turtle

# Setup er normalt sett ikke nødvendig, jeg trengte den for videoen.
# Parametere bredde og høyde samt x- og y- posisjon til vinduet når det blir opprettet
turtle.setup(600, 600, 120, 20)

# Tegner opp en firkant med sider på 100 piksler
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)

# Avslutter tegningen slik at turtle-vinduet forblir åpent når scriptet avslutter
turtle.done()
