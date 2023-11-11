from collections import deque

class Node():
    def __init__(self):
        self.visited = False
        self.movimientos = 0

def BFS(nodes, edges, start,fin):
    nodes[start].visited = True
    q = deque()
    q.append(start)
    while q:
        current_node = q.popleft()
        for neighbor in edges[current_node]:
            if not nodes[neighbor].visited:
                nodes[neighbor].visited = True
                nodes[neighbor].movimientos = nodes[current_node].movimientos + 1
                q.append(neighbor)
        if current_node==fin:
                    break


nodos=dict()
aristas=dict()
letras = ("A","B","C","D","E","F","G","H")
for i in letras:
    for t in range(1,9):
        exec(f"aristas['{i}{t}']=[]")
        exec(f"nodos['{i}{t}']=Node()")
for i in range(8):
    for j in range(8):
        node = letras[i] + str(j+1)
        moves = []
        if i+2 < 8 and j+1 < 8:
            moves.append(letras[i+2] + str(j+2))
        if i+2 < 8 and j-1 >= 0:
            moves.append(letras[i+2] + str(j))
        if i+1 < 8 and j+2 < 8:
            moves.append(letras[i+1] + str(j+3))
        if i+1 < 8 and j-2 >= 0:
            moves.append(letras[i+1] + str(j-1))
        if i-1 >= 0 and j+2 < 8:
            moves.append(letras[i-1] + str(j+3))
        if i-1 >= 0 and j-2 >= 0:
            moves.append(letras[i-1] + str(j-1))
        if i-2 >= 0 and j+1 < 8:
            moves.append(letras[i-2] + str(j+2))
        if i-2 >= 0 and j-1 >= 0:
            moves.append(letras[i-2] + str(j))
        aristas[node] = moves
casos = int(input())

for k in range(casos):
    inicio, fin = input().split()
    for i in nodos.keys():
        nodos[i].visited = False
        nodos[i].movimientos = 0
    BFS(nodos,aristas,inicio,fin)
    if inicio==fin:
        print(0)
        continue
    print(nodos[fin].movimientos)