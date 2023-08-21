def maxStrength(n):
    cache = [1] * 10
    for i in range(1, 10):
        cache[i] =  cache[i-1] * i
    
    def cal(x):
        res = 0
        while x > 0:
           res += cache[x%10]
           x = x // 10
        return res
    
    s = set([n])
    cur = n
    while True:
        new_id = cal(cur)
        if new_id in s:
            return max(s) * len(s)
        else:
            cur = new_id
            s.add(new_id)
    
print(maxStrength(540))
    
    