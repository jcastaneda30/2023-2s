from collections import deque
from collections import deque

entrada = int(input())
for i in range(entrada):
    my_deque = deque()
    caso=list(map(int,input().split()))
    for i in caso:
        my_deque.append(i)
    while len(my_deque)>1:
        ultimo = my_deque.pop()
        penultimo = my_deque.pop()
        if(ultimo+penultimo)%2==0:
            my_deque.append((ultimo+penultimo)//2)
        else:
            my_deque.append(penultimo)
            my_deque.append(ultimo)
            break
    print(f"{len(my_deque)} {my_deque[-1]}")