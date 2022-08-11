def maximumSum(a, m):
    if len(a) == 1:
        return a[0] % m
    
    for i in range(len(a)):
        a[i] = a[i] % m
    
    pref_sum = [[0, 0] for _ in range(len(a) + 1)]
    pref_sum[0] = [0, -1]
    for i in range(len(a)):
        pref_sum[i+1][0] = (pref_sum[i][0] + a[i]) % m
        pref_sum[i+1][1] = i
    
    pref_sum.sort()
    
    
    print(pref_sum)
    
    
    # return res

a = "3 3 9 9 5 10 12 4"
a = list(map(int, a.split()))
m = 7

# a = "3 9"
# a = list(map(int, a.split()))
# m = 7

print(maximumSum(a, m))
    