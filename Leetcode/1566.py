from typing import List

class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int):
        for i in range(len(arr)-m*k+1):
            flag = True
            for j in range(m):
                for h in range(1, k):
                    if arr[m*h+j+i] != arr[i+j]:
                        # print(i,j,m,h)
                        flag = False
                        break
                    
                if not flag:
                    break
            if flag: 
                return True
            
        return False
    
# print(Solution().containsPattern(arr = [1,2,1,2,1,3], m = 2, k = 3))
print(Solution().containsPattern(arr = [1,2,1,2,1,1,1,3], m = 2, k = 2))
# print(Solution().containsPattern(arr = [1,2,4,4,4,4], m = 1, k = 3))
# print(Solution().containsPattern(arr = [1,2,4,4,4,4], m = 2, k = 2))
# print(Solution().containsPattern(arr = [1,2,3,1,2], m = 2, k = 2))
# print(Solution().containsPattern(arr = [1,2], m = 1, k = 2))      
        