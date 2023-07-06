package main

import "fmt"

func min(a ...int) int {
	res := a[0]
	for i := 0; i < len(a); i++ {
		if a[i] < res {
			res = a[i]
		}
	}
	return res
}

func minSubArrayLen(tgt int, nums []int) int {
	target := int64(tgt)
	cur_sum := int64(0)
	res := 1000001
	first := 0
	idx := 0

	for ; idx < len(nums); idx++ {
		cur_sum += int64(nums[idx])
		for cur_sum >= target {
			cur_sum -= int64(nums[first])
			res = min(res, idx-first+1)
			// fmt.Println(res, cur_sum, idx, first)
			first += 1
		}
	}

	// fmt.Println(res, cur_sum, first)

	if res == 1000001 {
		return 0
	}
	if cur_sum >= target {
		res = min(res, len(nums)-first)
	}
	return res
}

func main() {
	target := 7
	nums := []int{2, 3, 1, 2, 4, 3}

	target = 213
	nums = []int{12, 28, 83, 4, 25, 26, 25, 2, 25, 25, 25, 12}

	target = 80
	nums = []int{10, 5, 13, 4, 8, 4, 5, 11, 14, 9, 16, 10, 20, 8}
	for idx, i := range nums {
		fmt.Print(i, idx, " | ")
	}
	fmt.Print("\n")
	fmt.Println(minSubArrayLen(target, nums))
}
