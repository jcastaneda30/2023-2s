from collections import deque

class Node():
    def __init__(self):
        self.visited = False
        self.distancia = "INF"

def DFS(nodes, edges):
    familias = 0
    integrantesMax=0
    for i in nodes.keys():
        integrantes =0
        if nodes[i].visited==False:
            familias+=1
            q = deque()
            q.append(i)
            while q:
                u=q.pop()
                if nodes[u].visited==False:
                    nodes[u].visited=True
                    integrantes+=1
                    for adyacente in edges[u]:
                        if nodes[adyacente].visited ==False:
                            q.append(adyacente)
        integrantesMax=max(integrantes,integrantesMax)
    return familias,integrantesMax

casos = int(input())

for i in range(casos):
    registros = int(input())
    nodos=dict()
    aristas=dict()
    for i in range(registros):
        inicio, fin = map(int,input().split())
        nodos[inicio]=Node()
        nodos[fin]=Node()
        if inicio not in aristas:
            aristas[inicio]=[fin]
        else:
            aristas[inicio].append(fin)

        if fin not in aristas:
            aristas[fin]=[inicio]
        else:
            aristas[fin].append(inicio)
    valores =  DFS(nodos,aristas)
    print(valores[0], valores[1])

