class Solution:
    def concatenatedBinary(self, n: int):
        MOD = int(1e9) + 7
        res = 1
        for i in range(2, n + 1):
            # print(i, self.count_bits(i))
            res = ((res << i.bit_length()) + i) % MOD
        
        return res


n = 3
n = 12
n = int(1e5)

print(Solution().concatenatedBinary(n))
            
        