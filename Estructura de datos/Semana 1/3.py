entrada = int(input())
positivos=0
negativos=0
for i in range(entrada):
    numero=int(input())
    if(numero<0):
        negativos+=numero
    else:
        positivos+=numero
print(f"positivos {positivos}, negativos {negativos}")