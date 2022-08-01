# def uniquePaths(m: int, n: int):
#     count = [[1 for _ in range(n)] for i in range(m)]
#     for i in range(1, m):
#         for j in range(1, n):
#             count[i][j] =  count[i-1][j] + count[i][j-1]
    
#     return count[m-1][n-1]


def uniquePaths(m: int, n: int):
    minn, maxx = m-1, n-1
    if minn >  maxx:
        minn, maxx = maxx, minn
    up = [i for i in range(maxx+1, maxx + minn + 1)]
    down = [i for i in range(1, minn + 1)]
    # print(up, down)
    for i in range(len(up)-1,-1,-1):
        for j in range(len(down)-1,-1,-1):
            if up[i] % down[j] == 0 and down[j] > 1:
                up[i] = up[i] // down[j]
                down[j] = 1
    # print(up, down)            

    res = 1
    for item in up:
        res *= item
    for item in down:
        res = res// item

    return res

print(uniquePaths(100,100))