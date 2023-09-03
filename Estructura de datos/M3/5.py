datos = int(input())
dicttionary = {}
for i in range(datos):
    entrada = list(map(int,input().split()))
    suma=0
    for k in range(len(entrada)):
        for t in range(len(entrada)-1-k):
            if entrada[t]>entrada[t+1]:
                entrada[t],entrada[t+1]=entrada[t+1],entrada[t]
                suma+=1

    print(suma)