N = int(input())

for i in range(N):
    expresion = input().strip()
    pila = []
    a = False

    for k in expresion:
        if k in "[{(":
            pila.append(k)
        elif k in ")}]":
            if len(pila) == 0:
                a = True
                print("incorrecta")
                break
            else:
                ultimo = pila.pop()
            if (k == ')' and ultimo != '(') or (k == ']' and ultimo != '[') or (k == '}' and ultimo != '{'):
                print("incorrecta")
                a = True
                break
    if not a and len(pila) == 0:
        print("correcta")
    elif not a and len(pila) > 0:
        print("incorrecta")
