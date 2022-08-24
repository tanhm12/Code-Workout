from collections import Counter
from typing import List

class Solution:
    def longestPalindrome(self, words: List[str]):
        counter = Counter(words)
        
        res = 0
        self_palindrome = 0
        remain = len(counter)
        while remain > 0:
            w = next(iter(counter))
            remain -= 1
            reverse_w = w[::-1]
            if w[0] == w[1]:
                if counter[w] % 2 == 0:
                    res += counter[w]
                else:
                    if counter[w] > self_palindrome:
                        res += max(self_palindrome - 1, 0)
                        self_palindrome = counter[w]
                    else:
                        res += counter[w] - 1
            elif reverse_w in counter:
                res += 2 * min(counter[w], counter[reverse_w])
                remain -= 1
                del counter[reverse_w]            
            del counter[w]

        return 2 * (res + self_palindrome)

words = ["lc","cl","gg"]
# words = ["ab","ty","yt","lc","cl","ab"]
# words = ["cc","ll","xx"]

print(Solution().longestPalindrome(words))    
        