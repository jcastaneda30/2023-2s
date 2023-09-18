import heapq

heap = []
valor = 0
while True:
    elemento = input()
    
    if elemento == "end":
        break
    
    if elemento == "sig" and heap:
        valor = heapq.heappop(heap)
    elif elemento.isdigit():
        element = int(elemento)
        heapq.heappush(heap, element)

if(valor!=0): print(valor)
