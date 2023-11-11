from collections import deque

class TrieNode:
    def __init__(self):
        self.children = {}
        self.contador = 0
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.count = 0

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node.children[char].contador+=1
            node = node.children[char]
        if not node.is_end_of_word:
            node.is_end_of_word = True
            self.count += 1

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def startsWithPrefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return len(node.children) > 0

    def delete(self, word):
        q = deque()
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            else:
                q.append(node)
                node = node.children[char]
        if len(node.children) > 0:
            node.is_end_of_word = False
        else:
            for char in word[::-1]:
                node = q.pop()
                if node.is_end_of_word or len(node.children) > 1:
                    break
                else:
                    node.children.pop(char)
            self.count -= 1
            return True

    def _traverseRecursively(self, node, current_word, words_list):
        if node.contador==1:
            words_list.append(current_word)
            return
        for char, child_node in node.children.items():
            self._traverseRecursively(child_node, current_word + char, words_list)

    def traverse(self):
        words_list = []
        self._traverseRecursively(self.root, '', words_list)
        return words_list

while True:
    casos = int(input())
    if casos == 0:
        break
    a=Trie()
    for i in range(casos):
        palabra = input()
        a.insert(palabra)
    lista = a.traverse()
    print(sum(len(i) for i in lista))


