n = int(input())
arr = list(map(int, input().split()))

def cal_target(r):
    return sum([i * r[i-1] for i in range(1, len(r) + 1)])

k = 3
r = arr[:k]
target = cal_target(r)
cands = {i: 0 for i in range(k)}

cached = False
MAX = -int(1e9)
max_cand = 0

for i in range(k, len(arr)):
    if not cached:
        MAX = -int(1e9)
        max_cand = 0
        for c in cands:
            s = 0
            counter = 1
            for j in range(k):
                if j  == c:
                    continue
                s += counter * r[j]
                counter += 1
            cands[c] = s
            if s > MAX:
                MAX = s
                max_cand = c
    
    if MAX + k * arr[i] > target:
        r = [r[j] for j in range(k) if j != max_cand] + [arr[i]]
        target = cal_target(r)   
        cached = False 
    else:
        cached = True

print(target)


