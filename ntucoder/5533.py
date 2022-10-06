n, v = list(map(int, input().split()))

acc = [0]
for i in range(n):
    acc.append(int(input()) + acc[-1])

res = 0
mark = 1
for i in range(1, len(acc)):
    while mark < len(acc) and acc[mark] < acc[i-1] + v:
        mark += 1
        
    if mark < len(acc):
        res += len(acc) - mark
    else:
        break

print(res)
