palabras=[]
palabrasSet=set()
while True:
    entrada=input()
    if(entrada=="#"): break
    palabras.append(entrada)
    palabrasSet.add(entrada)
palabras.sort()
for i in palabras:
    for j in range(len(i)):
        if i[:j] in palabrasSet and i[j:] in palabrasSet:
            a = [i[:j] , i[j:]]
            print(f"{i} = {a[0]} + {a[1]}")
