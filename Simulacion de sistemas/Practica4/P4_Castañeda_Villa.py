import random 

def Uniforme():
    dias = [5,6,7,8,9,10,11]

    acumulado = [0.05,0.15,0.35,0.65,0.85,0.95,1]

    #Primera fuente de incertidumbre
    suma = 0
    dias=0
    while(suma<8000):
        r=random.random()

        for i in range(len(acumulado)):
            if(r<=acumulado[i]):
                dias +=  dias[i]
        
        if inspeccion():
            suma=triangular(600,1100,1000)

    return suma,dias
        
def triangular(min,max,moda):
    valorX=random.triangular(min,max,moda)
    return valorX

def inspeccion():
    r = random.Random()
    if r<=0.8:
        return True
    else:
        return False

N=int(input())

for i in range(N):
    a=Uniforme()

