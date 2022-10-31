def printShortestPath(n, i_start, j_start, i_end, j_end):
    moves_map = {
        "UL": (-2, -1),
        "UR": (-2, 1),
        "R": (0, 2),
        "LR": (2, 1),
        "LL": (2, -1),
        "L": (0, -2)
    }

    def move(pos, name):
        i, j = pos
        ni, nj = moves_map[name]
        return i + ni, j + nj
    
    def is_valid(pos):
        i, j = pos
        if 0 <= i < n and 0 <= j < n:
            return True
        return False

    check_marks = [[False for _ in range(n)] for __ in range(n)]
    check = lambda pos: check_marks[pos[0]][pos[1]]
    def set_check_marks(pos): 
        check_marks[pos[0]][pos[1]] = True
    
    from queue import Queue
    
    q = Queue()
    q.put([[i_start, j_start], []])
    set_check_marks((i_start, j_start))
    while not q.empty():
        pos, moves = q.get()
        if pos[0] == i_end and pos[1] == j_end:
            print(len(moves))
            print(" ".join(moves))
            return 
        
        for name in moves_map:
            next_pos = move(pos, name)
            if is_valid(next_pos) and not check(next_pos):
                set_check_marks(next_pos)
                q.put([next_pos, moves[:] + [name]])
    
    print("Impossible")
    return 

if __name__ == '__main__':
    n = int(input().strip())

    first_multiple_input = input().rstrip().split()

    i_start = int(first_multiple_input[0])

    j_start = int(first_multiple_input[1])

    i_end = int(first_multiple_input[2])

    j_end = int(first_multiple_input[3])

    printShortestPath(n, i_start, j_start, i_end, j_end)
