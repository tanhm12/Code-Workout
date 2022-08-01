t = int(input())

def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    for i in range(len(nums)):
        if str(nums[i]).endswith('0'):
            continue
        elif str(nums[i]).endswith('5'):
            nums[i] += 5
        else:
            while not str(nums[i]).endswith('2'):
                nums[i] += nums[i] % 10
            nums[i] %= 20
    res = nums[0]
    for i in range(1, len(nums)):
        if nums[i] != res:
            return "NO"
    return "YES"

res = []
for i in range(t):
    res.append(solve())

for i in res:
    print(i)