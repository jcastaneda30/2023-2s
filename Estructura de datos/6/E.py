duracion = int(input())
tonos = []
tiempos = []
for i in range(int(input())):
    codigo, inicio, frecuency = map(int,input().split())
    tonos.append((inicio,frecuency))

for inicio,frecuency in tonos:
    timer = inicio
    while timer<=duracion:
        tiempos.append(timer)
        timer+=frecuency

tiempos.sort()

for i in tiempos:
    print(i)