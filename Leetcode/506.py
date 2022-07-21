from typing import List

def findRelativeRanks(score: List[int]):
    pos = {str(i+1): j for i,j in enumerate(sorted(score, reverse=True))}
    
    pos["Gold Medal"] = pos["1"]
    del pos["1"]
    if "2" in pos:
        pos["Silver Medal"] = pos["2"]
        del pos["2"]
    if "3" in pos:
        pos["Bronze Medal"] = pos["3"]
        del pos["3"]
    
    pos = {pos[i]: i for i in pos}
    
    return [pos[score_i] for score_i in score]


score = [5,4,3,2,1]
score = [10,3,8,9,4]
print(findRelativeRanks(score))
    
    