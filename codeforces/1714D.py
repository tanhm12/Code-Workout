t = int(input())

def solve():
    so = input()
    n = int(input())
    osi = [input() for _ in range(n)]
    
    s = [i for i in osi if i in so]
    map_si = {si: osi.index(si) + 1 for si in s}
    
    if len(s) == 0:
        return -1, []
    
    s.sort(reverse=True, key=lambda x: len(x))
    check = [set() for i in range(len(so))]
    # print(s)
    
    counter = {si:[] for si in s}
    
    all_intervals = []
    for si in s:
        i = 0
        # print(so.count(si))
        while i <= len(so) - len(si):
            if so[i: i + len(si)] == si:
                all_intervals.append([i+1, -(i+len(si)), map_si[si]])
                
            i += 1
    # print(check)      
    if len(all_intervals) == 0:
        return -1, []
    all_intervals.sort()
    print(len(so), all_intervals)
    
    res = [all_intervals[0]]
    check = [False for _ in range(len(so))]
    for i in range(res[-1][0]-1, -res[-1][1] ):
        check[i] = True
    
    # print(res[0])
    i = 1
    while i < len(all_intervals):
        j = i
        max_interval = None
        while j < len(all_intervals) and all_intervals[j][0] <= -res[-1][1] + 1 and -all_intervals[j][1] > -res[-1][1]:
            if max_interval is None:
                max_interval = all_intervals[j]
            elif -all_intervals[j][1] > -max_interval[1] :
                max_interval =  all_intervals[j]
            j += 1
        if max_interval is None:
            return -1, []
        res.append(max_interval)
        i = j
    res = [[item[2], item[0]] for item in res]
    return len(res), "\n".join([" ".join(list(map(str, item))) for item in res])

res = []
for i in range(t):
    res.append(solve())

for i in res:
    print(i[0])
    if len(i[1]) > 0:
        print(i[1])