numeros = []
while True:
    numero = int(input())
    if numero == 0:
        break

    eliminate = False

    if numero in numeros:
        numeros.remove(numero)
        eliminate = True
    elif numero - 1 in numeros:
        numeros.remove(numero - 1)
        eliminate = True
    elif numero + 1 in numeros:
        numeros.remove(numero + 1)
        eliminate = True

    if not eliminate:
        numeros.append(numero)

if numeros:
    print(" ".join(map(str, numeros)))
else:
    print("0")
