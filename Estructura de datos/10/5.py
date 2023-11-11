candidatos = {}
votantes = {}
eliminados=set()
while True:
    votante,candidato=map(int,input().split())
    if votante==0 and candidato==0:
        break
    if votante not in votantes:
        votantes[votante]=candidato
        if candidato not in candidatos:
            candidatos[candidato]=1
        else:
            candidatos[candidato]+=1
    else:
        if votante not in eliminados:
            candidatos[votantes[votante]]-=1
            eliminados.add(votante)
cosas=[]
for clave, valor in candidatos.items():
    if valor !=0:
        cosas.append((clave,valor))
cosas = sorted(cosas,key=lambda x: (-x[1],-x[0]))
for i in cosas:
    print(f"{i[0]} {i[1]}")
