package main

import (
	"fmt"
)

func merge(nums1 []int, m int, nums2 []int, n int) {
	if n == 0 {
		return
	}
	var p1, p2 int = m - 1, n - 1
	// var val int;
	for p1 >= 0 && p2 >= 0 {
		if nums1[p1] <= nums2[p2] {
			nums1[p1+p2+1] = nums2[p2]
			p2--
		} else {
			nums1[p1+p2+1] = nums1[p1]
			p1--
		}
	}

	if p1 < 0 {
		for i := p2; i >= 0; i-- {
			nums1[i] = nums2[i]
		}
	}
}

func main() {
	nums1 := []int{1, 2, 3, 0, 0, 0}
	m := 3
	nums2 := []int{1, 2, 3}
	n := 3

	// nums1 := []int{0, 0}
	// m := 1
	// nums2 := []int{1}
	// n := 1

	merge(nums1, m, nums2, n)
	fmt.Printf("%v", nums1)
	// fmt.Println(lengthOfLIS(nums))
}
