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
                # is_one_False = False
                # for j in range(i, i + len(si)):
                #     # if check[j] is False:
                #     #     is_one_False = True
                #     check[j].add(map_si[si])
                # if is_one_False:
                # print(si, i)
                all_intervals.append([i+1, -(i+len(si)), map_si[si]])
                # print(all_intervals[-1])
                    
                # i += len(si)
                # continue
                
                # counter[si].append([i+1, i + len(si)])
                
            i += 1
    # print(check)      
    # # print(res)
    # print({map_si[si]: counter[si] for si in counter})
    if len(all_intervals) == 0:
        # print(so, all_intervals)
        return -1, []
    all_intervals.sort()
    
    # check.sort(key=lambda x: len(x))
    # if len(check[0]) == 0:
    #     return -1, []
    res = [all_intervals[0]]
    check = [False for _ in range(len(so))]
    for i in range(res[-1][0]-1, -res[-1][1] + 1):
        check[i] = True
    
    # print(res[0])
    for i in range(1, len(all_intervals)):
        # print(all_intervals[i])
        if all_intervals[i][0] == -res[-1][1] + 1:
            res.append([i for i in all_intervals[i]])
            for j in range(res[-1][0]-1, -res[-1][1]):
                check[j] = True
            # print(all_intervals[i])
    
    # print(check)
    if not all(check):
        # print(check)
        return -1, []
    res = [[item[2], item[0]] for item in res]
    return len(res), "\n".join([" ".join(list(map(str, item))) for item in res])

res = []
for i in range(t):
    res.append(solve())

for i in res:
    print(i[0])
    if len(i[1]) > 0:
        print(i[1])