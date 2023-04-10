package main

import (
	"fmt"
	"sort"
)

func dfs(candidates []int, target int, canIdx int, curSol []int, curIdx int, result *[][]int) {
	if target < 0 {
		return
	} else if target == 0 {
		newRecord := make([]int, curIdx)
		for i := 0; i < curIdx; i++ {
			newRecord[i] = curSol[i]
		}
		*result = append(*result, newRecord)
	} else {
		for i := canIdx; i < len(candidates); i++ {
			if candidates[i] > target {
				return
			}
			if i > canIdx && candidates[i] == candidates[i-1] {
				continue
			}
			curSol[curIdx] = candidates[i]
			dfs(candidates, target-candidates[i], i+1, curSol, curIdx+1, result)
		}
	}
}

func combinationSum2(candidates []int, target int) [][]int {
	sort.Slice(candidates, func(i, j int) bool {
		return candidates[i] < candidates[j]
	})

	result := make([][]int, 0)
	curSol := make([]int, 101) // pre-allocate
	dfs(candidates, target, 0, curSol, 0, &result)
	return result
}

func main() {
	candidates := []int{2, 5, 2, 1, 2}
	target := 5
	result := combinationSum2(candidates, target)
	for _, arr := range result {
		fmt.Println(arr)
	}
}
