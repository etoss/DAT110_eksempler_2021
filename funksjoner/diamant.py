# Diamant-eksemplet med funksjoner. Viser hvordan man med refaktorering kan
# unngå å kopiere kode
#
#   *
#  * *
# *   *
#  * *
#   *


def tegn_forste_del_linje(lengde, hvilken_linje):
    for tall in range(lengde):
        if tall == lengde-1-hvilken_linje:
            print("*", end="")
        else:
            print(" ", end="")


def tegn_andre_del_linje(lengde, hvilken_linje):
    for tall in range(lengde-1):
        if tall == hvilken_linje-1:
            print("*", end="")
        else:
            print(" ", end="")


def tegn_diamant(storrelse):
    for linje in range(storrelse):
        tegn_forste_del_linje(storrelse, linje)
        tegn_andre_del_linje(storrelse, linje)
        print()
    for linje in range(storrelse - 2, -1, -1):
        tegn_forste_del_linje(storrelse, linje)
        tegn_andre_del_linje(storrelse, linje)
        print()


if __name__ == "__main__":
    storrelse = int(input("Størrelse: "))
    tegn_diamant(storrelse)
