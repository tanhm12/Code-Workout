def luckBalance(k, contests):
    contests = [(-j, i) for i, j in contests]
    contests.sort()
    mark = len(contests)
    for i, item in enumerate(contests):
        if item[0] == 0:
            mark = i
            break
    mark = max(0, mark-k)
    # print(mark, contests)
    return sum([item[1] for item in contests[mark:]]) - sum([item[1] for item in contests[:mark]])


k = 3
contests = [[5, 1], [2, 1], [1, 1], [8, 1], [10, 0], [5, 0]]
print(luckBalance(k, contests))