from collections import deque

class Node():
    def __init__(self):
        self.visited = False
        self.color = True

def BFS(nodes, edges, start):
    nodes[start].visited = True
    q = deque()
    q.append(start)
    while q:
        current_node = q.popleft()
        for neighbor in edges[current_node]:
            if not nodes[neighbor].visited:
                nodes[neighbor].visited = True
                nodes[neighbor].color = not nodes[current_node].color
                q.append(neighbor)
    return verificar(nodes,edges,start)
        
    

def verificar(nodes, edges, start):
    for k in edges.keys():
        nodes[k].visited = False
    nodes[start].visited = True
    q = deque()
    q.append(start)
    while q:
        current_node = q.popleft()
        for neighbor in edges[current_node]:
            if nodes[neighbor].color==nodes[current_node].color:
                    return False
            if not nodes[neighbor].visited:
                nodes[neighbor].visited = True
                q.append(neighbor)
    return True
casos = int(input())
for i in range(casos):
    puntos, cantidadAristas = map(int,input().split())
    nodos=dict()
    aristas=dict()
    for i in range(cantidadAristas):
        inicio, fin = map(int,input().split(", "))
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
    a=True
    for t in aristas.keys():
        nodo2=nodos.copy()
        if not BFS(nodo2,aristas,t):
            print("no bipartito")
            a=False
            break
    if a: 
        print("bipartito")

