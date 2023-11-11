from collections import deque

class Node():
    def __init__(self):
        self.visited = False
        self.distancia = "INF"

def BFS(nodes, edges, start):
    nodes[start].visited = True
    nodes[start].distancia = 0
    q = deque()
    q.append(start)
    while q:
        current_node = q.popleft()
        for neighbor in edges[current_node]:
            if not nodes[neighbor].visited or ((nodes[current_node].distancia+1) < nodes[neighbor].distancia) :
                nodes[neighbor].visited = True
                if nodes[neighbor].distancia=="INF":
                    nodes[neighbor].distancia = nodes[current_node].distancia + 1
                else:
                    nodes[neighbor].ditancia=min(nodes[neighbor].distancia,nodes[current_node].distancia+1)
                q.append(neighbor)

casos = int(input())

for i in range(1, casos + 1):
    n, b = map(int, input().split(", "))
    aristas = {}
    for p in range(n):
        aristas[p]=[]
    for _ in range(b):
        inicio, fin = map(int, input().split())
        aristas[inicio].append(fin)
        aristas[fin].append(inicio)

    nodos = {}
    numm = list(range(n))
    numm.sort()
    for t in numm:
        nodos[t] = Node()

    if 0 not in aristas:
        for nodo in numm:
            print(nodos[nodo].distancia)
        continue

    BFS(nodos, aristas, 0)
    print(f"fiesta {i}:")
    for v in numm:
        if v == 0:
            continue
        print(f"{v} {nodos[v].distancia}")
    print()
