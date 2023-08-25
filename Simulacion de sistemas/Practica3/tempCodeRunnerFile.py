for i in range(1, len(lista) - 1):
    if lista[i] <  lista[i-1] :
        contadorW += 1
    elif lista[i] >  lista[i-1]:
        contadorL += 1