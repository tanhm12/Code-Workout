def stepPerms(n):
    res = [1, 1, 2]
    for i in range(3, n+1):
        res.append(res[i-3] + res[i-2] + res[i-1])
    
    return res[n]

print(stepPerms(7))