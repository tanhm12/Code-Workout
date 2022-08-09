from typing import List

def numFactoredBinaryTrees(arr: List[int]):
    import math
    
    mod = int(1e9) + 7
    
    arr.sort()
    res = {arr[i]: 1 for i in range(len(arr))}
    for i, item in enumerate(arr):
        sqrt_item = round(math.sqrt(item))
        for j in range(i):
            if arr[j] <= sqrt_item:
                a = item // arr[j]
                if a * arr[j] == item and a in res:
                    if a != arr[j]:
                        res[item] += (res[a] * res[arr[j]] * 2) % mod
                    else:
                        res[item] += (res[a] ** 2) % mod
                        break
            else:
                break
    
    
    return sum(res.values()) % mod

# arr =  [4, 2 ]
arr = [2,4,5,10]
# arr = [10,20,100,200,1000,10000, 100000, 1000000, 10000000]

print(numFactoredBinaryTrees(arr))
    
    
    