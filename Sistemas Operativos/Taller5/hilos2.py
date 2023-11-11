import threading
import time

# Definición de la función
def mifuncion():
    print("Estoy en mi función")
    # Retardo de un segundo
    time.sleep(1)
    print("Terminé función")

# Se inicia temporizador
t1 = time.perf_counter()

# Se crean dos hilos para ejecutar la función mifuncion
hilo1 = threading.Thread(target=mifuncion)
hilo2 = threading.Thread(target=mifuncion)

# Se inician los hilos
hilo1.start()
hilo2.start()

# Se espera a que ambos hilos terminen
hilo1.join()
hilo2.join()

# Se termina temporizador
t2 = time.perf_counter()

# Se muestra el tiempo total de ejecución
print("Tiempo:", round(t2 - t1, 2), "segundos")
