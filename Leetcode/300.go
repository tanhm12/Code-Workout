package main

import (
	"fmt"
	"sort"
)

func min(a int, b int) int {
	if a <= b {
		return a
	} else {
		return b
	}
}

func lengthOfLIS(nums []int) int {
	result := make([]int, 1)
	result[0] = nums[0]

	var pos int

	for i := 1; i < len(nums); i++ {
		pos = sort.Search(len(result), func(j int) bool { return result[j] >= nums[i] })
		if pos >= len(result) {
			result = append(result, nums[i])
		} else {
			result[pos] = min(nums[i], result[pos])
		}
	}

	return len(result)
}

func main() {
	// nums := []int{10, 9, 2, 5, 3, 7, 101, 18}
	// nums := []int{0, 1, 0, 3, 2, 3}
	nums := []int{1, 3, 6, 7, 9, 4, 10, 5, 6}

	fmt.Println(lengthOfLIS(nums))
}
