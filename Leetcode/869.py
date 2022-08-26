class Solution:
    def reorderedPowerOf2(self, n: int):
        from collections import Counter
        countern = Counter(list(map(int, list(str(n)))))
        for i in range(32):
            if Counter(list(map(int, list(str(2**i)))))  == countern:
                return True
        
        return False

n = 10
n=1
n=123456
# n = 2410

print(Solution().reorderedPowerOf2(n))
