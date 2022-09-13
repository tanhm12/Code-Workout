from typing import List

class Solution:
    def validUtf8(self, data: List[int]):
        def check_type(num):
            if 0 <= num <= 127:
                return 0
            elif num <= 191:
                return -1
            elif num <= 223:
                return 1
            elif num <= 239:
                return 2
            elif num <= 247:
                return 3
            else:
                return None

        remain = 0
        for num in data:
            tp = check_type(num)
            # print(remain, tp)
            if tp is None:
                return False
            if remain == 0 and tp < 0:
                return False
            elif remain > 0 and  tp >= 0:
                return False
            remain += tp
        
        if remain == 0:
            return True
        else:
            return False
    
data = [197,130,1]
data = [235,140,4]

print(Solution().validUtf8(data))
                
        