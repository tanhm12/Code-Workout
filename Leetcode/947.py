from typing import List

class Solution:

    def removeStones(self, stones: List[List[int]]) -> int:
        from collections import defaultdict
        x_dict = defaultdict(list)
        y_dict = defaultdict(list)
        for i, stone in enumerate(stones):
            x_dict[stone[0]].append(i)
            y_dict[stone[1]].append(i)

        check = [False for _ in range(len(stones))] 

        def dfs(i):
            check[i] = True
            
            for j in x_dict[stones[i][0]]:
                if not check[j] :
                    dfs(j) 
            for j in y_dict[stones[i][1]]:
                if not check[j] :
                    dfs(j)

        num_clusters = 0
        for i in range(len(stones)):
            if not check[i]:
                num_clusters += 1 
                dfs(i)
        
        return len(stones) - num_clusters
