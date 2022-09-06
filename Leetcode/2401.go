package main

import "fmt"

func longestNiceSubarray(nums []int) int {
	result := 1

	cur := 1
	accum := nums[0]

	for i := 1; i < len(nums); i++ {
		if nums[i]&accum == 0 {
			accum = nums[i] + accum
			cur += 1
		} else {
			if cur > result {
				result = cur
			}
			for j := i - cur; j < i; j++ {
				accum -= nums[j]
				cur -= 1
				if accum&nums[i] == 0 {
					cur += 1
					accum += nums[i]
					break
				}
			}

		}
	}
	if cur > result {
		result = cur
	}
	return result
}

func main() {
	nums := []int{3, 1, 5, 11, 13}
	// nums := []int{1, 3, 8, 48, 10}
	// nums := []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3}
	// nums := []int{135745088, 609245787, 16, 2048, 2097152}
	// nums := []int{264, 65552, 50331652, 1, 1048576, 16384, 544}
	// nums := []int{84139415, 693324769, 614626365, 497710833, 615598711, 264, 65552, 50331652, 1, 1048576, 16384, 544, 270532608, 151813349, 221976871, 678178917, 845710321, 751376227, 331656525, 739558112, 267703680}
	fmt.Println(longestNiceSubarray((nums)))
}
