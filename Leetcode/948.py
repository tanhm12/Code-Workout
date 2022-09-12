from typing import List

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int):
        if len(tokens) == 0:
            return 0
        score = 0
        tokens.sort()
        
        smallp = 0
        largep = len(tokens) - 1
        
        while True:
            while smallp <= largep and power >= tokens[smallp] :
                power -= tokens[smallp]
                smallp += 1
                score += 1
            print(smallp, largep, power, score)
            if smallp >= largep or score == 0:
                break
            
            power += tokens[largep]
            largep -= 1
            score -= 1
        
        return score
            

tokens = [100]
power = 50

tokens = [100,200]
power = 150

# tokens = [100,200,300,400]
# power = 200

tokens = [100]
power = 150

tokens = [71,55,82]
power = 54

print(Solution().bagOfTokensScore(tokens, power))            
                