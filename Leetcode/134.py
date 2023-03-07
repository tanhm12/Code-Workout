from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        gas_add = [gas[i] - cost[i] for i in range(n)]
        
        gas_agg = 0
        cur_tank = 0
        start = 0
        for i in range(n):
            cur_tank += gas_add[i]
            gas_agg += gas_add[i]
            if cur_tank < 0:
                start = i + 1
                cur_tank = 0
        
        if gas_agg < 0:
            return -1
        return start
            
            