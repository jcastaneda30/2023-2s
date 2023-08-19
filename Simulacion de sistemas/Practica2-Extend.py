import random
from scipy.integrate import quad


def expresion(x):
    funcion = (x + (x + (x)**(1/2))**(1/2))**(1/2)
    return funcion


def escalar(a, b):
    U = random.uniform(0, 1)
    X = a + U * (b - a)
    return X


entrada = int(input("Ingrese el número de puntos: "))
a = int(input("Ingrese el valor de 'a': "))
b = int(input("Ingrese el valor de 'b': "))
c = int(input("Ingrese el valor de 'c': "))
listaPuntos = []

for i in range(entrada):
    X = escalar(a, b)
    Y = escalar(0, c)
    listaPuntos.append([X, Y])

listaAciertos = []

for i in range(entrada):
    x = listaPuntos[i][0]  # Cambiado de "entrada" a "i"
    y = listaPuntos[i][1]  # Cambiado de "entrada" a "i"
    listaAciertos.append(expresion(x) >= y)


N_H = listaAciertos.count(True)
NElegido = len(listaAciertos)

theta1 = c * (b - a) * (N_H / NElegido)
pEstimado = N_H / NElegido

I, error = quad(expresion, a, b)

varianzaTheta = (I/NElegido)*(c*(b-a)-I)

p = I/((c*(b-a)))

N = ((1-p)*p*(c*(b-a))**2)/((1-0.05)*0.01**2)

Intervalo = 1.64*(((pEstimado*(1-pEstimado))**(1/2))*(b-a)*c)/(N**(1/2))

print(f"Valor real de la integral I = {round(I,3)}")
print(f"Valor varianza theta = {round(varianzaTheta,3)}")
print(f"Valor estimado de N con  α =0.05 y el ε=0.01 N >= {round(N,3)}")
print(f"Valor de p̂ = {round(pEstimado,3)}")
print(f"Valor encontrado de I con la integral de montecarlo metodo 1 I ≈ {round(theta1,3)}")
print(f"Intervalo de confianza para theta1 {round(theta1,3)} ± {round(Intervalo,3)}")


#Metodo 2

listaPuntosMetodo2 = []

for i in range(entrada):
    X = escalar(a, b)
    Y = escalar(0, c)
    listaPuntosMetodo2.append([X, Y])

calculoG = []
for i in range(entrada):
    x = listaPuntos[i][0]  # Cambiado de "entrada" a "i"
    listaAciertos.append(expresion(x))

theta2 = ((b-a)*(1/NElegido))*sum(calculoG)



