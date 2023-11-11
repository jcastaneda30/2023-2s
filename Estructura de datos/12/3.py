class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.contador = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.count = 0

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node.children[char].contador += 1 
            node = node.children[char]
        if not node.is_end_of_word:
            node.is_end_of_word = True
            self.count += 1

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children or len(node.children)>1 or node.contador!=self.count:
                    return False
            node = node.children[char]
        return True

# Ejemplo de uso:
# Ejemplo de uso:
while True:
    a = Trie()
    casos = int(input())
    pequeno = "a"*33
    if casos == 0:
        break
    for i in range(casos):
        numero = input()
        if len(numero)<len(pequeno):
            pequeno=numero
        a.insert(numero)
    a.count = casos
    a.root.contador = casos
    if len(a.root.children) > 1:
        print("-")
        continue
    estoyMamdo = False
    for j in range(1, len(pequeno) + 1):
        pequeno_actual = list(pequeno[:j])  # Crear una copia para cada iteración
        if not a.search(pequeno_actual):
            print(''.join(pequeno_actual[:j-1]))
            break
        if j==len(pequeno):
            print(''.join(pequeno_actual[:j]))


