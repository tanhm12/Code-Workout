from typing import List

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda x: len(x))
        res = {w: 1 for w in words}
        for word in words:
            for i in range(len(word)):
                sub_word = word[:i] + word[i+1:]
                if sub_word in res:
                    res[word] = max(res[word], res[sub_word] + 1)
        
        return max(res.values())
        
        