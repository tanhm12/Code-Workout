t = int(input())

def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    
    res = set()
    for i in range(len(nums) -1, -1, -1):
        if nums[i] in res:
            return i + 1
        else:
            res.add(nums[i])
    
    return 0


res = []
for i in range(t):
    res.append(solve())

for i in res:
    print(i)

    