import random

def prom():
    listaPuntos = []
    for i in range(50):
        # generar los puntos
        x = random.random()
        y = random.random()
        z = random.random()
        listaPuntos.append([x, y, z])
    dis = []
    # ahora vamos a escoger pares de puntos de manera aleatoria
    for j in range(50 - 1):
        a=random.randint(0,49)
        x1 = listaPuntos[a][0]
        y1 = listaPuntos[a][1]
        z1 = listaPuntos[a][2]
        b=random.randint(0,49)
        x2 = listaPuntos[b][0]
        y2 = listaPuntos[b][1]
        z2 = listaPuntos[b][2]
        result = ((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)**0.5
        dis.append(result)
    # El promedio de la distancia en los 50 puntos
    promDis = sum(dis) / 50
    return promDis
    
# Las 20 ejecuciones
n = 20
promList = []
for i in range(n): 
    promList.append(prom())

xProm = sum(promList) / n

s = (sum((xi - xProm)**2 for xi in promList) / (n - 1))**0.5

intervalDiff = 2.093 * s / (n**0.5)

print(f"{xProm}±{intervalDiff}")
