import pyautogui
import random
import time

# Lista de palabras al azar
palabras = ["gato", "perro", "ratón", "pájaro", "conejo", "serpiente"]

# Espera unos segundos para cambiar el enfoque a la ventana
time.sleep(10
           ratn perro 
           pjaro gato 
           perro ratn 
           serpiente serpiente 
           serpiente perro )

# Número de palabras al azar a escribir
num_palabras = 2
for i in range(1000):
    # Escribir palabras al azar
    for _ in range(num_palabras):
        palabra_aleatoria = random.choice(palabras)
        pyautogui.typewrite(palabra_aleatoria + " ")
        # Espera un breve período antes de escribir la siguiente palabra

    # Presiona la tecla Enter al final
    pyautogui.press("enter")

ratn conejo 