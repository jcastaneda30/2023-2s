from collections import deque

C = int(input())
for i in range(C):
    entrada2 = deque(map(int,input().split()))
    while len(entrada2)>1:
        ultima=entrada2.pop()
        penultima=entrada2.pop()
        if (ultima+penultima)%2==0:
            entrada2.append((ultima+penultima)//2)

    print(f"{len(entrada2)} {entrada2[-1]}")
