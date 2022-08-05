from typing import Dict

class Node:
    def __init__(self, is_end, children=None):
        # self.value: str = value
        self.is_end: bool = is_end
        
        if children is None:
            self.children: Dict[str, Node] = {}
    
    def isLeaf(self):
        return len(self.children) == 0
            


class Trie:
    def __init__(self):
        self.root: Node = Node(False)
        

    def insert(self, word: str):
        node: Node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] =  Node(False) 
            node = node.children[c]
        node.is_end = True


    def search(self, word: str):
        node: Node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        if node.is_end:
            return True
        return False
        

    def startsWith(self, prefix: str):
        node: Node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        
        return True
            
            
# queries = ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
# params = [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]

queries = ["Trie", "insert", "search", "search", "insert", "startsWith", "insert", "search"]
params = [[], ["apple"], ["apple"], ["app"], ["apb"], ["app"], ["app"], ["app"]]

queries = ["Trie","startsWith"]
params = [[],["a"]]

obj = Trie()

res = [None]

for i in range(1, len(queries)):
    t = None
    if queries[i] == "insert":
        obj.insert(params[i][0])
    elif queries[i] == "search":
        t = obj.search(params[i][0])
    else:
        t = obj.startsWith(params[i][0])
    res.append(t)

print(res)
        