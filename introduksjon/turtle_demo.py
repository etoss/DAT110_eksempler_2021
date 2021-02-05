import turtle

# Tegner opp en firkant med sider på 100 piksler
def tegn_firkant(sidelengde):
    turtle.forward(sidelengde)
    turtle.left(60)
    turtle.forward(sidelengde)
    turtle.left(60)
    turtle.forward(sidelengde)
    turtle.left(60)
    turtle.forward(sidelengde)
    turtle.left(60)
    turtle.forward(sidelengde)
    turtle.left(60)
    turtle.forward(sidelengde)
    turtle.left(60)

# Setup er normalt sett ikke nødvendig, jeg trengte den for videoen.
# Parametere bredde og høyde samt x- og y- posisjon til vinduet når det blir opprettet
turtle.setup(600, 600, 120, 20)
tegn_firkant(100)

# Avslutter tegningen slik at turtle-vinduet forblir åpent når scriptet avslutter
turtle.done()
