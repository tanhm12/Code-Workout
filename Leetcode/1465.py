from typing import List

def maxArea(h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]):
    horizontalCuts = sorted(horizontalCuts)
    verticalCuts = sorted(verticalCuts)
    
    
    def find_max(cuts, x):
        maxx = cuts[0]
        for i in range(1,  len(cuts)):
            maxx =  max(maxx, cuts[i] - cuts[i-1])
        maxx =  max(maxx, x - cuts[-1])
        
        return maxx
    
    return find_max(horizontalCuts, h) *  find_max(verticalCuts, w)rr


print(maxArea(h = 5, w = 4, horizontalCuts = [1,2,4], verticalCuts = [1,3]))
print(maxArea(h = 5, w = 4, horizontalCuts = [3,1], verticalCuts = [1]))
print(maxArea(h = 5, w = 4, horizontalCuts = [3], verticalCuts = [3]))
# print(maxArea())
        