casos=int(input())

for i in range(casos):
    entrada = list(map(int,input().split(", ")))
    entrada.sort()
    prefix=[entrada[0]]*len(entrada)
    for i in range(1,len(entrada)):
        prefix[i]=prefix[i-1]+entrada[i]
    r=len(entrada)
    dif=999999999
    acum=entrada[-1]
    for i in range(1,r-1):
        dif=min(dif,abs(acum-prefix[-i-1]))
        acum=entrada[-i-1]+acum
    print(dif)

