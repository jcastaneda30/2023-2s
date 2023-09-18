import heapq

entrada = int(input())

for i in range(entrada):
    valores = list(map(int,input().split()))
    valores.pop()
    heapq.heapify(valores)
    while(len(valores)>1):
        ultimo = heapq.heappop(valores)
        Penultimo = heapq.heappop(valores)
        heapq.heappush(valores,ultimo+Penultimo)
    print(ultimo, Penultimo)
        