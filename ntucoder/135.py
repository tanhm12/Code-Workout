n, m = list(map(int, input().split()))

arr = list(map(int, input().split()))

def find():
    if n == 1:
        return -1, None
    s = 0
    e = 1
    while e < n:
        distance = arr[e] - arr[s]
        if distance < m:
            e += 1
        elif distance > m:
            s += 1
        else:
            return arr[s], arr[e]
    
    return -1, None

res = find()

if res[1]:
    print(f"{res[0]} {res[1]}")
else:
    print(-1)
