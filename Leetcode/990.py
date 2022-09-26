from typing import List

class Solution:
    def __init__(self, ):
        self.parent = {c: c for c in "abcdefghijklmnopqrstuvwxyz"}
        self.size = {c: 1 for c in "abcdefghijklmnopqrstuvwxyz"}
        
    def find_parent(self, c):
        if c !=  self.parent[c]:
            self.parent[c] = self.find_parent(self.parent[c])
        return self.parent[c]
    
    def merge(self, a, b):
        a = self.find_parent(a)
        b = self.find_parent(b)
        if a == b:
            return
        
        if self.size[a] > self.size[b]:
            a, b = b, a
        self.parent[a] = b
        self.size[b] += self.size[a]
    
    def equationsPossible(self, equations: List[str]):
        not_e_ids = []
        for i, e in enumerate(equations):
            if e[1] == "!":
                not_e_ids.append(i)
            else:
                a, b = e[0], e[-1]
                self.merge(a, b)
                
        for i in not_e_ids:
            e = equations[i]
            a, b = e[0], e[-1]
            if self.find_parent(a) == self.find_parent(b):
                return False
        
        return True
    
    
equations = ["b==a","a==b"]
equations = ["a==b","b!=c", "a!=c", "b==d", "c==d"]

print(Solution().equationsPossible(equations))
        