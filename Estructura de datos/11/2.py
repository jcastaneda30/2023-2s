from collections import deque

class Node():
    def __init__(self):
        self.visited = False
        self.dia = 0

def BFS(nodes, edges, start):
    nodes[start].visited = True
    q = deque()
    q.append(start)
    while q:
        current_node = q.popleft()
        for neighbor in edges[current_node]:
            if not nodes[neighbor].visited:
                nodes[neighbor].visited = True
                nodes[neighbor].dia = nodes[current_node].dia + 1
                q.append(neighbor)

amigos = int(input())
aristas = {}


for i in range(amigos):
    valores = list(map(int, input().split()))
    if valores[0] != -1:
        aristas[i] = valores
    else:
        aristas[i] = -1
centros = list(map(int, input().split(", ")))

for i in centros:

    if aristas[i] == -1:
        print(0)
        continue

    nodos = dict()
    for p in range(amigos):
        nodos[p]=Node()
    dias = [0] * amigos

    BFS(nodos, aristas, i)

    for k in range(amigos):
        if aristas[k]==-1:
            continue
        dias[nodos[k].dia] += 1

    max_can = 0
    dia_aa = 0
    for t in range(amigos):
        if dias[t]>max_can and t!=0:
            max_can=dias[t]
            dia_aa=t
    print(f"{dia_aa} {max_can}")
