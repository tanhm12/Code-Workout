class Solution:
    def checkPerfectNumber(self, num: int):
        if num == 1:
            return False
        import math
        s = 1
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                s += (i + num//i)
                if s > num: 
                    return False
        
        return s == num
        
while True:
    print(Solution().checkPerfectNumber(int(input())))        