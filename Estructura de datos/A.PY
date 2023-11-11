C = int(input())
for i in range(C):
    palabra = input().split()
    derecho = ["L","A","N","U"]
    reves = ["U","N","A","L"]
    for caracter in palabra:
        if derecho[-1]==caracter:
            derecho.pop()
            if len(derecho)==0:
                break
        if reves[-1]==caracter:
            reves.pop()
            if len(reves)==0:
                break
    if(len(derecho)==0 or len(reves)==0):
        print("YES")
    else:
        print("NO")