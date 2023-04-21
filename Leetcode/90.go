package main

import "sort"

func clone(arr []int) []int {
	res := make([]int, len(arr))
	copy(res, arr)
	return res
}

func subsetsWithDup(nums []int) [][]int {
	sort.Slice(nums, func(i, j int) bool { return nums[i] < nums[j] })
	res := make([][]int, 0)
	res = append(res, make([]int, 0))
	needAdded := 0
	for i, num := range nums {
		if i == 0 || nums[i] != nums[i-1] {
			needAdded = len(res) // keep track to last subset that need to append num
		}
		start := len(res) - needAdded
		end := len(res)
		for j := start; j < end; j++ {
			res = append(res, append(clone(res[j]), num))
		}
	}
	return res
}
