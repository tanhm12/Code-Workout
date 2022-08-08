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


    def search(self, word: str, last_id):
        node: Node = self.root
        for i in range(last_id+1):
            c = word[i]
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
    
    
from typing import List

def findWords(board: List[List[str]], words: List[str]):
    m, n = len(board), len(board[0])
    
    trie = Trie()
    for word in words:
        trie.insert(word)
        
    def findWordsFromChar(ci, cj):
        check = [[False for _ in range(n)] for _ in range(m)]
        current_sol = ["" for _ in range(10)]
        def travel(i, j, pos):
            res = []
            prev_sol_pos = current_sol[pos]
            for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 <= x <m and 0<=j < y and pos < 9 and not check[x][y]:
                    check[x][y] = True
                    current_sol[pos] = board[i][j]
                    if trie.search(current_sol, pos):
                        res.append("".join(current_sol[:pos+1]))
                        res.ex
                    
                
                