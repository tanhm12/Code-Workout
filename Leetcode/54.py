from typing import List
import numpy as np

def spiralOrder(matrix: List[List[int]]):
    import numpy as np
    matrix = np.array(matrix)
    m, n = matrix.shape  # mxn matrix
    
    def get_outermost(row, col):
        if col == n-col-1:
            res =  [[j, col] for j in range(row, m-row)]
        elif row == m-row-1:
            res = [[row, i] for i in range(col, n-col)]
        else:
            res =  [[row, i] for i in range(col, n-col)] + \
                    [[j, n-col-1] for j in range(row+1, m-row-1)] + \
                    [[m-row-1, i] for i in range(n-col-1, col-1, -1)] + \
                    [[j, col] for j in range(m-row-2, row, -1)]
        # print(row, col, res)
        return res
    
    ids = []         
    row, col = 0, 0
    while row <= (m-1) // 2 and col <= (n-1) // 2:
        ids += get_outermost(row, col)
        row += 1
        col += 1
    # print(ids)
    
    return [matrix[idx[0], idx[1]] for idx in ids]


matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

# print(spiralOrder(matrix))
print(spiralOrder(np.array(matrix).T))
        