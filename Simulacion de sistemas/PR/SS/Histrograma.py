# Abre el archivo en modo lectura
with open('demcom1.txt', 'r') as archivo:
    # Lee todas las líneas del archivo y las coloca en una lista
    lista_de_datos = archivo.readlines()

# Ahora tienes los datos en una lista, pero como cadenas de texto.
# Si deseas convertirlos a números enteros, puedes hacerlo así:
lista_de_datos_enteros = [float(linea.strip()) for linea in lista_de_datos]

# Imprime la lista de datos enteros
import matplotlib.pyplot as plt
plt.hist(lista_de_datos_enteros)
plt.ylabel("Frecuencias")
plt.xlabel("Tiempos")
plt.show()