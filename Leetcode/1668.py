class Solution:
    def maxRepeating(self, sequence: str, word: str):
        c, j = 0, 0
        res = 0
        counter = 0
        
        while c < len(sequence):
            i = c
            while i < len(sequence):
                if sequence[i] == word[j]:
                    j += 1
                    i += 1
                    if j == len(word):
                        counter += 1
                        res = max(res, counter)
                        j = 0
                else:
                    counter = 0
                    j = 0
                    break
            c += counter * len(word) + 1
            j = 0
        
        return res
    

sequence = "ababc"
word = "ab"

sequence = "ababc"
word = "ba"

sequence = "ababacab"
word = "aba"

sequence = "aaabaaaabaaabaaaabaaaabaaaabaaaaba"
word = "aaaba"

sequence = "aaaaaaaaaaaaaaaaaa"
word = "aaaa"

sequence = "aaaaa"
word = "aaa"

print(Solution().maxRepeating(sequence, word))
        