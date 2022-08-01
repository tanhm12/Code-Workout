
h, w = list(map(int, input().split()))
r = list(map(int, input().split()))
c = list(map(int, input().split()))

# count = 0
# c.sort()
# for i in range(h):
#     print(r[i], bisect.bisect_left(c, r[i]))
#     count += bisect.bisect_left(c, i) - r[i]

# mod = int(1e9) + 7
# print(count)
# print(2**count % mod)
def main():
    grid = [[0 for _ in range(w)] for i in range(h)]

    for i, item in enumerate(c):
        for j in range(item):
            grid[j][i] = 1
        if item < h:
            if grid[item][i] == 1:
                return 0
            grid[item][i] = 2
            
    # for i in grid:
    #     print(i)
        
    for i, item in enumerate(r):
        for j in range(item):
            if grid[i][j] == 2:
                return 0
            grid[i][j] = 1
        if item < w:
            if grid[i][item] == 1:
                return 0
            grid[i][item] = 2   
            
    # for i in grid:
    #     print(i)

    count = 0
    for i in range(h) :
        for j in range(w):
            if grid[i][j] == 0:
                count += 1

    mod = int(1e9) + 7
    # print(count)
    return 2**count % mod

print(main())
        