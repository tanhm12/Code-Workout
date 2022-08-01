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
    
    res = []
    for si in s:
        i = 0
        # print(so.count(si))
        while i <= len(so) - len(si):
            
            if so[i: i + len(si)] == si:
                is_one_False = False
                for j in range(i, i + len(si)):
                    # if check[j] is False:
                    #     is_one_False = True
                    check[j].add(map_si[si])
                # if is_one_False:
                # print(si, i)
                res.append([map_si[si], i+1])
                    
                # i += len(si)
                # continue
                
                counter[si].append([i+1, i + len(si)])
                
            i += 1
    print(check)      
    # print(res)
    print({map_si[si]: counter[si] for si in counter})
    
    # check.sort(key=lambda x: len(x))
    # if len(check[0]) == 0:
    #     return -1, []
    res = 0
    i = 0
    while i < len(so):
        if len(check[i]) == 0:
            return -1, []
        for item in check[i]:
            
        
    # if not all(check):
    #     return -1, []
    # return len(res), "\n".join([" ".join(list(map(str, item))) for item in res])

res = []
for i in range(t):
    res.append(solve())

for i in res:
    print(i[0])
    if len(i[1]) > 0:
        print(i[1])