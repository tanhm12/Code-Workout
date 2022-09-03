class Solution:
    def numsSameConsecDiff(self, n: int, k: int):
        res = []
        sol = ['0' for _ in range(n)]
        int2str = {i: str(i) for i in range(10)}
        
        def generate(i):
            if i == n:
                res.append(int(''.join(sol)))
                return
            prev = int(sol[i-1])
            for j in int2str:
                if abs(prev-j) == k:
                    sol[i] = int2str[j]
                    generate(i+1)
        
        for i in range(1, 10):
            sol[0] = str(i)
            generate(1)
        
        return res
    

n = 2
k = 2

n = 3
k = 7

n = 9
k = 1

print(Solution().numsSameConsecDiff(n, k))
                    