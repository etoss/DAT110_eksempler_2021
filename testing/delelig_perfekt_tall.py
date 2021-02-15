# Oppgave f
def delelig(a, b):
    if a%b == 0:
        return True
    else:
        return False


# Oppgave g
def perfekt(tall):
    sum_av_faktorer = 1
    for dele_paa in range(2, (tall+2)//2):
        if delelig(tall, dele_paa):
            sum_av_faktorer += dele_paa
            print(f"Faktor: {dele_paa}")
    print(f"Sum av faktorer: {sum_av_faktorer}")
    if sum_av_faktorer == tall:
        return True
    else:
        return False


# Oppgave h
if __name__ == "__main__":
    tall = int(input("Hvilket tall skal jeg sjekke om er perfekt? "))
    if perfekt(tall):
        print(f"{tall} er perfekt")
    else:
        print(f"{tall} er ikke perfekt")
