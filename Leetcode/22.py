from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        all_sols = []
        n *= 2
        def gen(cur_sol, cur_stack, remain_open):
            if len(cur_sol) == n:
                all_sols.append(''.join(cur_sol))
                return 

            if remain_open > 0:
                gen(cur_sol+['('], cur_stack + 1, remain_open-1)
            
            if cur_stack > 0:
                gen(cur_sol + [")"], cur_stack-1, remain_open)
            
        gen([], 0, n//2)
        return all_sols


print(Solution().generateParenthesis(3))




