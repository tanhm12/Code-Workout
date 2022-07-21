from typing import List


def findBall(grid: List[List[int]]):
    new_grid = [[0] + grid[i] + [0] for i in range(len(grid))]  # add bound
    new_grid.append([0] + [2] * len(grid[-1])+  [0])
    # print(new_grid)
    
    def travel(row, col):
        val = new_grid[row][col]
        # print(row, col, val)
        if val == 2:
            return col -1
        elif val == 0:
            return -1
        elif val == 1:
            right_val = new_grid[row][col+1]
            if right_val == 0 or right_val == -1:
                return -1
            else:
                return travel(row+1, col+1)
        else:
            left_val = new_grid[row][col-1]
            if left_val == 0 or left_val == 1:
                return -1
            else:
                return travel(row+1, col-1)
    
    res = []
    for i in range(len(grid[0])):
        out = travel(0, i+1)
        res.append(out)                
        
    return res
    

print(findBall(grid = [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]))
# print(findBall(grid=[[1]]))
# print(findBall(grid=[[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]))

