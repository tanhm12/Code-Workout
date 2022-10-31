package main

func checkSubarraySum(nums []int, k int) bool {
	remainder_map := make(map[int]int, 0)
	pref_nums := make([]int, 0)
	pref_nums = append(pref_nums, 0)
	for i := 0; i < len(nums); i++ {
		pref_nums = append(pref_nums, pref_nums[i]+nums[i])
	}

	var remainder int
	for i := 0; i < len(pref_nums); i++ {
		remainder = pref_nums[i] % k
		if val, ok := remainder_map[remainder]; ok {
			if i-val > 1 {
				return true
			}
		} else {
			remainder_map[remainder] = i
		}
	}

	return false
}
