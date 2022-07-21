from typing import List

def candy(ratings: List[int]):
    if len(ratings) == 1:
        return 1

    # print(ratings)
    res = len(ratings)

    start = -1
    for i in range(1, len(ratings)): 
        if ratings[i] != ratings[i-1]:
            start = i-1
            break
    if start == -1:
        return res

    end = len(ratings)
    for i in range(len(ratings) - 1, -1, -1): 
        if ratings[i] != ratings[i-1]:
            end = i + 1
            break

    if end <= start + 1:
        return res

    # print(start, end)

    marks = [[start, 'v']] if ratings[start+1] > ratings[start] else [[start,  'p']]

    for i in range(start + 2, end):
        current_mark = marks[-1]
        if ratings[i] > ratings[i-1]:
            if current_mark[1] != 'v':
                marks.append([i - 1, 'v'])
        elif ratings[i] < ratings[i-1]:
            if current_mark[1] != 'p':
                marks.append([i - 1, 'p'])
        else:
            if current_mark[1] == 'v':
                marks.append([i - 1, 'p'])
            elif current_mark[1] == 'p':
                marks.append([i - 1, 'v'])
            marks.append([i, 'notvp'])
    
    # current_patterns = marks[-1][1]
    # for i in range(start + 2, end):
    #     current_mark = marks[-1]
    #     if ratings[i] > ratings[i-1]:
    #         if current_patterns != 'v':
    #             marks.append([i - 1, 'v'])
    #             current_patterns = 'p'
    #     elif ratings[i] < ratings[i-1]:
    #         if current_mark[1] != 'p':
    #             marks.append([i - 1, 'p'])
    #             current_patterns = 'v'
    #     else:
    #         marks.append([i-1, 'notpv'])
    #         current_patterns = 'notpv'
            

    current_mark = marks[-1]
    if current_mark[-1][0] == 'v':
        marks.append([end-1, 'p'])
    else:
        marks.append([end-1, 'v'])
    # print(marks)


    def cal_sum(x):
        return x * (x+1) // 2

    for i in range(len(marks)):
        if marks[i][1] == 'p':
            left = 0
            if i > 0:
                left = marks[i][0] - marks[i-1][0]

            right = 0
            if i+1 < len(marks):
                right = marks[i+1][0] - marks[i][0]

            maxx, minn = left, right
            if left < right:
                maxx, minn = right, left

            res += cal_sum(minn) - minn + cal_sum(maxx + 1) - maxx - 1

    return res


import numpy as np

# ratings = list(np.random.randint(110, 115, (np.random.randint(10, 20),)))
ratings = [114, 113, 111, 111, 113, 113, 112, 112, 110, 112, 114, 111, 111, 113, 111, 111, 110, 110, 113]
# ratings = [113, 114, 114, 114, 110, 113, 112, 112, 113, 111, 114, 114, 113, 112]
# ratings = [110, 110, 111, 112, 110, 113, 112, 110, 114, 114]

print(len(ratings), ratings)
print(candy(ratings))