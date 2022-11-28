from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        from collections import defaultdict, Counter
        m, n = len(board), len(board[0])
        check = [[False for i in range(n)] for j in range(m)]

        board_dict = defaultdict(int)
        for row in board:
            for w in row:
                board_dict[w] += 1
        
        ## pre-check counter
        counter_word = Counter(word)
        for c in counter_word:
            if board_dict[c] < counter_word[c]:
                return False
        
        ## pre-check to prevent looping too much in cases like "aaaaaab"
        if board_dict[word[0]] > board_dict[word[-1]]:
            word = word[::-1]

        ## dfs
        def search(i, j, pos):
            if board[i][j] == word[pos]:
                check[i][j] = True
                pos += 1
                if pos == len(word):
                    return True
                res = False
                for row, col in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                    if 0<=row<m and 0<=col<n and not check[row][col]:
                        res = res or search(row, col, pos)
                check[i][j] = False
                return res
            else:
                return False

        for i in range(m):
            for j in range(n):
                if search(i, j, 0):
                    return True
        
        return False 


board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]] 
word = "ABCCED"

# board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
# word = "SEE"

# board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
# word = "ABCB"

# board = [["a","a"]]
# word = "aaa"

# board = [["C","A","A"],["A","A","A"],["B","C","D"]]
# word = "AAB"

# board = [["a"]]
# word = "a"
board = [["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","B"],["A","A","A","A","B","A"]]
word = "AAAAAAAAAAAAABB"

print(Solution().exist(board, word))
        

