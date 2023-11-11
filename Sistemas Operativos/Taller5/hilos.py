from threading import Thread, get_ident
from time import sleep
def funcion():
    print("Soy un hilo ident =", get_ident())
    print()

t1 = Thread(target=funcion)
t2 = Thread(target=funcion)

t1.start()
sleep(5)

t2.start()
sleep(5)

print("Hilo principal sigue su ejecución")
print("Hilo principal sigue su ejecución")
print("Hilo principal sigue su ejecución")

t1.join()
t2.join()

print("Termina principal")
