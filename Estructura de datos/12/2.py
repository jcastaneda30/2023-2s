

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.palabras = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.count = 0

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node.children[char].palabras+=1
            node = node.children[char]
        if not node.is_end_of_word:
            node.is_end_of_word = True
            self.count += 1
    
    def DFS(self, nodo, lista, palabra):
        if nodo.is_end_of_word:
            lista[0]=lista[0]+1
        for char in nodo.children:
            palabra.append(char)
            self.DFS(nodo.children[char], lista, palabra)
            palabra.pop()
        
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return 0
            node = node.children[char]
        return node


    def startsWithPrefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def _deleteHelper(self, node, word, index):
        if index == len(word):
            if node.is_end_of_word:
                node.is_end_of_word = False
                self.count -= 1
                # Eliminar el nodo si no tiene otros hijos
                return len(node.children) == 0
            return False

        char = word[index]
        if char not in node.children:
            return False

        should_delete_child = self._deleteHelper(node.children[char], word, index + 1)

        if should_delete_child:
            del node.children[char]
            # Eliminar el nodo si no es el final de otra palabra
            return len(node.children) == 0

        return False

    def delete(self, word):
        self._deleteHelper(self.root, word, 0)

    def _traverseRecursively(self, node, current_word, words_list):
        if node.is_end_of_word:
            words_list.append(current_word)
        for char, child_node in node.children.items():
            self._traverseRecursively(child_node, current_word + char, words_list)

    def traverse(self):
        words_list = []
        self._traverseRecursively(self.root, '', words_list)
        return words_list

casos = int(input())
a = Trie()

for i in range(casos):
    palabra = input()
    a.insert(palabra)

juego = int(input())

for j in range(juego):
    prefijo = input()
    palabraas= a.search(prefijo)
    if palabraas==0:
         print(0)
         continue
    # listaPalabras = [0]
    # a.DFS(palabraas,listaPalabras,list(prefijo))
    # print(listaPalabras[0])
    print(palabraas.palabras)
