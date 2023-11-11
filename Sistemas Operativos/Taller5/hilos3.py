from threading import Thread, get_ident
from time import sleep
import time

def sumatoria(inicial,final):
    global suma
    for i in range(inicial,final):
        suma=suma+i
suma=0
t1 = time.perf_counter()
hilo1=Thread(target=sumatoria,args=(1,1000000))
hilo2=Thread(target=sumatoria,args=(1000000,2000000))

hilo1.start()
hilo2.start()

hilo1.join()
hilo2.join()
t2 = time.perf_counter()
print("Tiempo:", round(t2 - t1, 2), "segundos")
t1 = time.perf_counter()
suma2=0
for i in range(0,2000000):
    suma2=suma2+i
t2 = time.perf_counter()
print("Tiempo:", round(t2 - t1, 2), "segundos")
print(suma)
print(suma2)