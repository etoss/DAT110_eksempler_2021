for tall in range(10, 0, -1):
    print(tall)

liste = [1, 3, 6, 9, 11]
print()
for element in liste:
    element = 2*element
for index in range(len(liste)):
    liste[index] = 2*liste[index]
for element in liste:
    print(element)
