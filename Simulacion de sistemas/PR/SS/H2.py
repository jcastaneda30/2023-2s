import math
import matplotlib.pyplot as plt

with open('demcom1.txt', 'r') as archivo:
    datos = [float(linea.strip()) for linea in archivo.readlines()]

n = len(datos)
k = math.ceil(math.log(n,2) + 1)

min_valor = min(datos)
max_valor = max(datos)
intervalos = [min_valor + i * (max_valor - min_valor) / k for i in range(k)]+[max_valor]
frecuencias = [0] * (k)

for dato in datos:
    for i in range(k):
            if dato >= intervalos[i] and dato < intervalos[i + 1]:
                frecuencias[i] += 1
print(sum(frecuencias))
frecuencias_relativas = [frecuencia / n for frecuencia in frecuencias]

fig = plt.figure()
ax = fig.add_subplot(111)
x = range(1, k + 1)
ax.bar(x, frecuencias_relativas)

# Etiquetas para el eje X
rangos_etiquetas = [f"{intervalos[i]:.1f}-{intervalos[i + 1]:.1f}" for i in range(k)]
ax.set_xticks(x)
ax.set_xticklabels(rangos_etiquetas, rotation=45)

plt.ylabel("Frecuencias Relativas")
plt.xlabel("Intervalos")
plt.title("Histograma")
plt.show()
