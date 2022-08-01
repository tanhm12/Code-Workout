t = int(input())


def minus(a, b):
    a = 60 * a[0] + a[1]
    b = 60 * b[0] + b[1]
    
    if b > a:
        a += 60 * 24
    
    return a - b

def solve():
    n, H, M = list(map(int, input().split()))
    alarms = [list(map(int, input().split())) for i in range(n)]
    
    res = 24 * 60
    for alarm in alarms:
        res = min(res, minus(alarm, [H, M]))
    
    
    return f"{res // 60} {res % 60}"
    

res = []
for i in range(t):
    res.append(solve())

for i in res:
    print(i)

