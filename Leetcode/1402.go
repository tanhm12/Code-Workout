package main

import (
	"sort"
)

func maxSatisfaction(satisfaction []int) int {
	sort.Slice(satisfaction, func(i, j int) bool {
		return satisfaction[j] < satisfaction[i]
	})
	if satisfaction[0] <= 0 {
		return 0
	}
	pref_sum := satisfaction[0]
	res := satisfaction[0]
	n := len(satisfaction)
	for i := 1; i < n; i++ {
		if -satisfaction[i] >= pref_sum {
			return res
		} else {
			pref_sum += satisfaction[i]
			res += pref_sum
		}
	}
	return res
}
