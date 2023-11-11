def DFS(elementos):
    alto, ancho = len(elementos), len(elementos[0])
    matrizVisitados = [[False] * ancho for _ in range(alto)]
    maximo = 0

    def valid_move(j, t):
        return 0 <= j < alto and 0 <= t < ancho and elementos[j][t] == 'X' and not matrizVisitados[j][t]

    for j in range(alto):
        for t in range(ancho):
            if elementos[j][t] == 'X' and not matrizVisitados[j][t]:
                stack = [(j, t)]
                count = 0
                while stack:
                    cur_j, cur_t = stack.pop()
                    if valid_move(cur_j, cur_t):
                        matrizVisitados[cur_j][cur_t] = True
                        count += 1
                        stack.extend([(cur_j - 1, cur_t), (cur_j + 1, cur_t), (cur_j, cur_t - 1), (cur_j, cur_t + 1)])
                maximo = max(maximo, count)

    return maximo

casos = int(input())
for i in range(casos):
    alto, ancho = map(int, input().split())
    elementos = [input() for _ in range(alto)]
    maximo = DFS(elementos)
    print(maximo)
