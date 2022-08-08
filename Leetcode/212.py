from typing import Dict

class Node:
    def __init__(self, is_end, children=None):
        # self.value: str = value
        self.is_end: bool = is_end
        
        if children is None:
            self.children: Dict[str, Node] = {}
    
    def isLeaf(self):
        return len(self.children) == 0
    
    def insert(self, word):
        node = self
        for c in word:
            if c not in node.children:
                node.children[c] =  Node(False) 
            node = node.children[c]
        node.is_end = True
        
    def startsWith(self, prefix: str, last_id=None):
        if last_id is None:
            last_id = len(prefix) - 1
        node: Node = self
        for i in range(last_id+1):
            c = prefix[i]
            if c not in node.children:
                return False, False
            node = node.children[c]
        
        return True, node.is_end
    
    def remove(self, word: str, id=0, last_id=None):
        if self.isLeaf():
            self.is_end = False
            return
        if last_id is None:
            last_id = len(word) - 1
        if id <= last_id and word[id] in self.children:
            if id == last_id:
                self.is_end = False
            self.children[word[id]].remove(word, id+1, last_id)
            if self.children[word[id]].isLeaf():
                del self.children[word[id]]
        
    
from typing import List

def findWords(board: List[List[str]], words: List[str]):
    m, n = len(board), len(board[0])
    solutions = set()
    
    trie = Node(False)
    for word in words:
        trie.insert(word)
    
    # for word in words:
    #     trie.remove(word)
    #     print(word, trie.startsWith(word))
    # print(trie.s)
        
    def findWordsFromChar(ci, cj):
        check = [[False for _ in range(n)] for _ in range(m)]
        current_sol = ["" for _ in range(10)]
        current_sol[0] = board[i][j]
        def travel(i, j, pos):
            if pos == 10:
                return []
            res = set()
            prev_sol_pos = current_sol[pos]
            for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 <= x <m and 0<=y <n and not check[x][y]:
                    check[x][y] = True
                    current_sol[pos] = board[x][y]
                    # if trie.search(current_string) and current_string not in solutions:
                    # print(ci,cj, x, y,"".join(current_sol[:pos+1]))
                    start_with, is_end = trie.startsWith(current_sol, pos)
                    
                    if start_with:
                        res.update(travel(x, y, pos+1))
                    if is_end:
                        current_string =  "".join(current_sol[:pos+1])
                        res.add(current_string)
                        trie.remove(current_string)
                        
                    current_sol[pos] = prev_sol_pos
                    check[x][y] = False
        
            return res
        start_with, is_end = trie.startsWith(current_sol, 0)
        if start_with:
            check[ci][cj] = True
            result = travel(ci,cj, 1)
            if is_end:
                result.add(board[ci][cj])
            return result
        
        return []
    
    # for i in range(m):
    #     print(board[i])
    
            
    
    for i in range(m):
        for j in range(n):
            t = findWordsFromChar(i, j)
            # print(i, j, t)
            solutions.update(t)
            
            
    
    return list(solutions)


board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain", "aateih", "aaan"]        

# board = [["a","b"],["c","d"]]
# words = ["abcb"]       

board = [["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"]]
words = ["lllllll","fffffff","ssss","s","rr","xxxx","ttt","eee","ppppppp","iiiiiiiii","xxxxxxxxxx","pppppp","xxxxxx","yy","jj","ccc","zzz","ffffffff","r","mmmmmmmmm","tttttttt","mm","ttttt","qqqqqqqqqq","z","aaaaaaaa","nnnnnnnnn","v","g","ddddddd","eeeeeeeee","aaaaaaa","ee","n","kkkkkkkkk","ff","qq","vvvvv","kkkk","e","nnn","ooo","kkkkk","o","ooooooo","jjj","lll","ssssssss","mmmm","qqqqq","gggggg","rrrrrrrrrr","iiii","bbbbbbbbb","aaaaaa","hhhh","qqq","zzzzzzzzz","xxxxxxxxx","ww","iiiiiii","pp","vvvvvvvvvv","eeeee","nnnnnnn","nnnnnn","nn","nnnnnnnn","wwwwwwww","vvvvvvvv","fffffffff","aaa","p","ddd","ppppppppp","fffff","aaaaaaaaa","oooooooo","jjjj","xxx","zz","hhhhh","uuuuu","f","ddddddddd","zzzzzz","cccccc","kkkkkk","bbbbbbbb","hhhhhhhhhh","uuuuuuu","cccccccccc","jjjjj","gg","ppp","ccccccccc","rrrrrr","c","cccccccc","yyyyy","uuuu","jjjjjjjj","bb","hhh","l","u","yyyyyy","vvv","mmm","ffffff","eeeeeee","qqqqqqq","zzzzzzzzzz","ggg","zzzzzzz","dddddddddd","jjjjjjj","bbbbb","ttttttt","dddddddd","wwwwwww","vvvvvv","iii","ttttttttt","ggggggg","xx","oooooo","cc","rrrr","qqqq","sssssss","oooo","lllllllll","ii","tttttttttt","uuuuuu","kkkkkkkk","wwwwwwwwww","pppppppppp","uuuuuuuu","yyyyyyy","cccc","ggggg","ddddd","llllllllll","tttt","pppppppp","rrrrrrr","nnnn","x","yyy","iiiiiiiiii","iiiiii","llll","nnnnnnnnnn","aaaaaaaaaa","eeeeeeeeee","m","uuu","rrrrrrrr","h","b","vvvvvvv","ll","vv","mmmmmmm","zzzzz","uu","ccccccc","xxxxxxx","ss","eeeeeeee","llllllll","eeee","y","ppppp","qqqqqq","mmmmmm","gggg","yyyyyyyyy","jjjjjj","rrrrr","a","bbbb","ssssss","sss","ooooo","ffffffffff","kkk","xxxxxxxx","wwwwwwwww","w","iiiiiiii","ffff","dddddd","bbbbbb","uuuuuuuuu","kkkkkkk","gggggggggg","qqqqqqqq","vvvvvvvvv","bbbbbbbbbb","nnnnn","tt","wwww","iiiii","hhhhhhh","zzzzzzzz","ssssssssss","j","fff","bbbbbbb","aaaa","mmmmmmmmmm","jjjjjjjjjj","sssss","yyyyyyyy","hh","q","rrrrrrrrr","mmmmmmmm","wwwww","www","rrr","lllll","uuuuuuuuuu","oo","jjjjjjjjj","dddd","pppp","hhhhhhhhh","kk","gggggggg","xxxxx","vvvv","d","qqqqqqqqq","dd","ggggggggg","t","yyyy","bbb","yyyyyyyyyy","tttttt","ccccc","aa","eeeeee","llllll","kkkkkkkkkk","sssssssss","i","hhhhhh","oooooooooo","wwwwww","ooooooooo","zzzz","k","hhhhhhhh","aaaaa","mmmmm"]

board = [["o","a","b","n"],["o","t","a","e"],["a","h","k","r"],["a","f","l","v"]]
words = ["oa","oaa"]

print(findWords(board, words))
                
                