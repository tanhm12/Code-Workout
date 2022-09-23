import sys

row, col = list(map(int, input().split()))
row -= 1
col -= 1

res = [0 for i in range(8)]  # (row, col) = (row, res[row])
remain = set(range(8))

def check(res):
    for i in range(len(res)-1):
        for j in range(i+1, len(res)):
            if res[i] - i == res[j] - j or res[i] - res[j] == j - i:
                return False
            
    return True
    

def find(pos):
    global remain
    pos = pos % 8
    if pos == row:
        if check(res):
            m = [['.' for _ in range(8)] for _ in range(8)]
            for i, item in enumerate(res):
                m[i][item] = 'w'
            print("\n".join([''.join(line) for line in m]))
            sys.exit(0)
        return 
    
    for i in list(remain):
        remain -= set([i])
        res[pos] = i
        find(pos + 1)
        remain.update(set([i]))

res[row] = col
remain -= set([col])
find(row + 1)

# from itertools import permutations
# for res in permutations(list(range(8))):
#     if check(res):
#         m = [['.' for _ in range(8)] for _ in range(8)]
#         for i, item in enumerate(res):
#             m[i][item] = 'w'
#         print("\n".join([''.join(line) for line in m]))
#         break

        
    