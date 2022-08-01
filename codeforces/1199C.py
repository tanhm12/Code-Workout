n, I = list(map(int, input().split()))
arr = list(map(int, input().split()))
max_unique = 2 ** (8*I // len(arr))


import math
def main():
    from collections import Counter
    counter = sorted(list(Counter(arr).items()), key=lambda x: x[0])
    
    if len(counter) <= max_unique:
        return 0
    
    total = 0
    for i in range(max_unique):
        total += counter[i][1]
    
    res = total
    for i in range(max_unique, len(counter)):
        total = total + counter[i][1] - counter[i-max_unique][1]
        # print(max_unique, total,res )
        res = max(res, total)
    return len(arr) - res
            
print(main())
