def countLuck(matrix, k):
    des = k
    res = "Oops!"
    n = len(matrix)
    m = len(matrix[0])
    check = [[False for i in range(m)] for j in range(n)]
    wave = 0
    
    def is_valid(i, j):
        if 0<=i<n and 0<=j<m:
            return True
        return False
    
    # print(matrix)
    
    def travel(i, j):
        nonlocal wave, res
        all_next_points = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
        possible_next_points = []
        for k, h in all_next_points:
            if is_valid(k,h) and not check[k][h] and matrix[k][h] != 'X':
                check[k][h] = True
                possible_next_points.append((k, h))
        
        # print(i, j, matrix[i][j], possible_next_points, wave)
        if len(possible_next_points) > 1:
            wave += 1
            
        for k, h in possible_next_points:
            if matrix[k][h] == '*' and wave == des:
                res = "Impressed"
                return
            travel(k, h)
        
        if len(possible_next_points) > 1:
            wave -= 1
            
    
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == "M":
                check[i][j] = True
                travel(i, j)
                break
    
    return res



k = 1
matrix = """*.M
.X.""".split("\n")  


k = 3
matrix = """.X.X......X
.X*.X.XXX.X
.XX.X.XM...
......XXXX.""".split("\n")  

k = 4
matrix = """.X.X......X
.X*.X.XXX.X
.XX.X.XM...
......XXXX.""".split("\n")  

print(countLuck(matrix, k))
    