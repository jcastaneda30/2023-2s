import random
import matplotlib.pyplot as plt

def leadTime():
    dias = [1, 2, 3]
    acumulada = [0.6, 0.9, 1]
    r = random.random()
    for i in range(len(acumulada)):
        if r <= acumulada[i]:
            return dias[i] + 1

def demanda():
    demanda = [0, 1, 2, 3, 4]
    acumulada = [0.1, 0.35, 0.7, 0.91, 1]
    r = random.random()
    for i in range(len(acumulada)):
        if r <= acumulada[i]:
            return demanda[i]

trueCostoFInal = []

def simulacion(N):
    M = 11
    pedidoActual = 8
    deficit = [0] * 366  # Ajusta la longitud a 366
    pedido = [0] * 366  # Ajusta la longitud a 366
    inventario = [0] * 366  # Ajusta la longitud a 366
    inventario[1] = 3
    costo = 0
    desfase = 3

    for i in range(2, 361):  # Ajusta el rango a 366
        demandaDia = demanda()
        if i % N == 0:
            pedido[i] = (M - inventario[i - 1] + deficit[i - 1])
            pedidoActual = pedido[i]
            desfase = i + leadTime()
            costoFinal += 2000
        if i == desfase:
            inventario[i] += pedidoActual + inventario[i - 1]
        inventario[i]+=inventario[i - 1]
        inventario[i]-=demandaDia
        inventario[i]-=deficit[i - 1]

        if inventario[i]< 0:
            deficit[i] = abs(inventario[i])
            inventario[i]=0

        costo+=inventario[i]*0.4
        costo+=deficit[i]*0.6

    return inventario,deficit,pedido,costoFinal
import matplotlib.pyplot as plt

#Probando el programa con la gráfica
tupla =  simulacion(5)

lInvertario = tupla[0]
lDemanda = tupla[1]
lDeficit = tupla[2]

print(f"Lista inventa: {lInvertario}")
print(f"Lista demanda: {lDemanda}")
print(f"Lista deficit: {lDeficit}\n")

#Luego de completar la simulación, graficamos el inventario y el déficit en una sola gráfica
plt.figure(figsize=(12, 6))

#Graficar inventario
plt.plot(range(361), lInvertario, label='Inventario', linewidth=2, color='blue')

#Graficar déficit
plt.plot(range(361), lDeficit, label='Déficit', linewidth=2, color='red')

plt.xlabel('Día')
plt.ylabel('Inventario / Déficit')
plt.title('Gráfico de Inventario y Déficit')
plt.grid()
plt.legend()

plt.show()
