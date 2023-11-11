varianza = 0

def valorEsperado(x,probabilidades):
    valor = 0
    for i in range(len(x)):
        valor+=x[i]*probabilidades[i]
    return valor

def varianza(x,probabilidades):
    ex_2=valorEsperado([i**2 for i in x],probabilidades)
    e2_x=(valorEsperado(x,probabilidades))**2
    return ex_2-e2_x

def expresion(x):
    return 25*x-8.5

def valorEsperadoConFuncion(expresion,x,probabilidades):
    valor = 0
    for i in range(len(x)):
        valor+=expresion(x[i])*probabilidades[i]
    return valor

def varianzaConFuncion(expresion,x,probabilidades):
    ex_2=valorEsperado([expresion(i)**2 for i in x],probabilidades)
    e2_x=(valorEsperadoConFuncion(expresion,x,probabilidades))**2
    return ex_2-e2_x

print(valorEsperado([6,7,8,9,10],[0.05,0.1,0.6,0.15,0.1]))
print(varianza([6,7,8,9,10],[0.05,0.1,0.6,0.15,0.1]))