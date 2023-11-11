def revision(Visitados,j,t,elementos):
    a,b,c,d=0,0,0,0
    if j>0 and j<len(elementos) and t>=0 and t<len(elementos[0]) and elementos[j-1][t]=='X' and not Visitados[j-1][t]:
        Visitados[j-1][t]=True
        a = revision(Visitados,j-1,t,elementos)+1
    if j>=0 and j<len(elementos)-1 and t>=0 and t<len(elementos[0]) and elementos[j+1][t]=='X' and not Visitados[j+1][t]:
        Visitados[j+1][t]=True
        b = revision(Visitados,j+1,t,elementos)+1
    if j>=0 and j<len(elementos) and t>0 and t<len(elementos[0]) and elementos[j][t-1]=='X' and not Visitados[j][t-1]:
        Visitados[j][t-1]=True
        c = revision(Visitados,j,t-1,elementos)+1
    if j>=0 and j<len(elementos) and t>=0 and t<len(elementos[0])-1 and elementos[j][t+1]=='X' and not Visitados[j][t+1]:
        Visitados[j][t+1]=True
        d = revision(Visitados,j,t+1,elementos)+1
    return a+b+c+d

casos=int(input())
for i in range(casos):
    nodos=dict()
    aristas=dict()
    alto,ancho = map(int,input().split())
    elementos = []
    matrizVisitados = [[False for _ in range(ancho)] for _ in range(alto)]
    maximo = 0
    for k in range(alto):
        xd = input()
        elementos.append(xd)
        if 'X' in xd:
            maximo=1
    for j in range(len(elementos)):
        for t in range(len(elementos[j])):
            if elementos[j][t]=='X' and not matrizVisitados[j][t]:
                maximo=max(maximo,revision(matrizVisitados,j,t,elementos))
    print(maximo)
                
    