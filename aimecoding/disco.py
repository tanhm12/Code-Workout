n = int(input())

mod = int(1e8)
res = [[1,1,1] for i in range(n)]
for i in range(1, n):
    res[i][0] = sum([res[i-1][j] for j in range(3)]) % mod
    res[i][1] = (res[i-1][0] + res[i-1][2]) % mod
    res[i][2] = (res[i-1][0] + res[i-1][1]) % mod
    
print((sum(res[-1])) % mod)
