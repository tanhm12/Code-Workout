    def findWordsFromChar(ci, cj):
        check = [[False for _ in range(n)] for _ in range(m)]
        current_sol = ["" for _ in range(10)]
        current_sol[0] = board[i][j]
        def travel(i, j, pos):
            if pos == 10:
                return []
            else:
                res = []
                if trie.search(current_sol, pos):
                    res = ["".join(current_sol[:pos+1])]
                check[i][j] = True
                prev_sol_pos = current_sol[pos]
                for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                    if 0 <= x <m and 0<=y <n and not check[x][y]:
                        check[x][y] = True
                        current_sol[pos] = board[x][y]
                        # current_string = "".join(current_sol[:pos+1])
                        # if trie.search(current_string) and current_string not in solutions:
                        print(ci,cj, x, y,"".join(current_sol[:pos+1]))
                        if trie.startsWith(current_sol, pos):
                            
                            res.extend(travel(x, y, pos+1))
                        current_sol[pos] = prev_sol_pos
                        check[i][j] = False