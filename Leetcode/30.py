from typing import List

def findSubstring(s: str, _words: List[str]):
    wlen = len(_words[0])
    from collections import Counter, defaultdict
    words = defaultdict(int)
    words.update(Counter(_words))
    # print(words)
    
    res = []
    start = 0
    cur = 0
    
    
    while cur < len(s):
        cword = s[cur: cur + wlen]
        # print(cword, cur, start, words)
        if cword in words:
            words[cword] -= 1
            if words[cword] == 0:
                del words[cword]
            
            cur += wlen
            
            if len(words) == 0:
                res.append(start)
            
        else:
            words = defaultdict(int)
            words.update(Counter(_words))
        
            start += 1
            cur = start
    return res
            
                


s = "barfoothefoobarman"
words = ["foo","bar"]

# s = "wordgoodgoodgoodbestword"
# words = ["word","good","best","word"]

# s = "barfoofoobarthefoobarman"
# words = ["bar","foo","the"]

# s = "wordgoodgoodgoodbestword"
# words = ["word","good","best","good"]

# s = "aaaaaaaaaaaaaa"
# words = ["aa","aa"]

print(findSubstring(s, words))            
                
    
