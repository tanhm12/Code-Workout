from typing import List

def findAndReplacePattern(words: List[str], pattern: str):
    def get_group(w):
        group_map = {}
        for c in w:
            if c not in group_map:
                group_map[c] = len(group_map)
        group = [[] for _ in range(len(group_map))]
        for i, c in enumerate(w):
            group[group_map[c]].append(i)
        return group
        
    def check(group1, group2):
        if len(group1) != len(group2): 
            return False
        for i in range(len(group1)):
            if group1[i] != group2[i]:
                return False
        
        return True
    
    res = []
    pattern_group = get_group(pattern)
    for w in words:
        if check(pattern_group, get_group(w)):
            res.append(w)
    
    return res

words = ["abc","deq","mee","aqq","dkd","ccc"]
pattern = "abb"


words = ["a","b","c"]
pattern = "a"

print(findAndReplacePattern(words, pattern))

