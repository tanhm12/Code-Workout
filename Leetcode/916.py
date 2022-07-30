from typing import List

def wordSubsets(words1: List[str], words2: List[str]):
    
    from collections import defaultdict
    all_chars = defaultdict(int)
    for w in words2:
        dw = defaultdict(int)
        for c in w:
            dw[c] += 1
        for c in dw:
            all_chars[c] = max(all_chars[c], dw[c])
                
        
    res = []
    for word in words1:
        dw = defaultdict(int)
        for c in word:
            dw[c] += 1
            
        inflag = True
        for c in all_chars:
            if dw[c] < all_chars[c]:
                inflag = False
                break
        if inflag:
            res.append(word)
    
    return res
    
    
words1 = ["amazon","apple","facebook","google","leetcode"]
words2 = ["e","o"]

words1 = ["amazon","apple","facebook","google","leetcode"]
words2=  ["e","oo"]
print(wordSubsets(words1, words2))
    