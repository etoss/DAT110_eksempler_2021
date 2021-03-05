def x_i_andre(x):
    return x**2


# "Funksjon" forventer en funksjon som tar en parameter, som er et flyttall, og returnerer
# et flyttall.
def numerisk_integrasjon(start, slutt, steg, funksjon):
    sum=0
    x = start+steg
    while x < slutt:
        sum += funksjon(x)*steg
        x += steg
    return sum


if __name__ == "__main__":
    integral1 = numerisk_integrasjon(0, 10, 0.0625, x_i_andre)
    print(integral1)
    integral1 = numerisk_integrasjon(0, 10, 0.0625, lambda x: x)
    print(integral1)
