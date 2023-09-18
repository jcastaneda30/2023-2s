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

    for i in range(2, 361): 
        demandaDia = demanda()
        if i % N == 0:
            pedido[i] = (M - inventario[i - 1] + deficit[i - 1])
            pedidoActual = pedido[i]
            desfase = i + leadTime()
            costo += 2000
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

    return inventario,pedido,deficit,costo
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
plt.plot(range(366), lInvertario, label='Inventario', linewidth=2, color='blue')

#Graficar déficit
plt.plot(range(366), lDeficit, label='Déficit', linewidth=2, color='red')

plt.xlabel('Día')
plt.ylabel('Inventario / Déficit')
plt.title('Gráfico de Inventario y Déficit')
plt.grid()
plt.legend()

plt.show()

#Costo medio anual de la política actual de reposición

def costoMedioAnual(N):
  suma = 0
  for i in range(1000):
    suma += simulacion(N)[3]
  return suma/1000

print(f"El costo medio anual de la política actual de reposición es ${costoMedioAnual(5)}")

#¿Cómo se comportan los costos medios anuales si se aumenta el número de días que se espera para hacer un pedido?

print(f"Con 10 días: {costoMedioAnual(10)}")
print(f"Con 15 días: {costoMedioAnual(15)}")
print(f"Con 20 días: {costoMedioAnual(20)}")
print(f"Con 25 días: {costoMedioAnual(25)}")
print(f"Con 40 días: {costoMedioAnual(40)}")
print(f"Con 45 días: {costoMedioAnual(45)}")
print(f"Con 50 días: {costoMedioAnual(50)}")
print(f"Con 51 días: {costoMedioAnual(51)}")
print(f"Con 52 días: {costoMedioAnual(52)}")
print(f"Con 53 días: {costoMedioAnual(53)}")
print(f"Con 54 días: {costoMedioAnual(54)}")
print(f"Con 55 días: {costoMedioAnual(55)}")
print(f"Con 56 días: {costoMedioAnual(56)}")
print(f"Con 57 días: {costoMedioAnual(57)}")
print(f"Con 60 días: {costoMedioAnual(60)}")
print(f"Con 70 días: {costoMedioAnual(70)}")
print(f"Con 75 días: {costoMedioAnual(75)}")
print(f"Con 80 días: {costoMedioAnual(80)}")
print(f"Con 100 días: {costoMedioAnual(100)}")
print(f"Con 150 días: {costoMedioAnual(150)}")
print(f"Con 200 días: {costoMedioAnual(200)}")

texto = """\nLos costos comienzan a bajar hasta cierto punto, para comenzar a subir de nuevo, y así sucesivamente,
por lo que no se encuentra un patrón evidente, con los datos podriamos afirmar que para reducir los costos
estaría bien hacer pedidos cada N=52 días, pues es el N que genera menos costos medios anuales"""

print(texto)