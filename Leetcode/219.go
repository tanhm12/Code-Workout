package main

func containsNearbyDuplicate(nums []int, k int) bool {
	if k == 0 {
		return false
	}
	s := map[int]bool{}
	for i := 0; i < len(nums); i++ {
		_, ok := s[nums[i]]
		if ok {
			return true
		} else {
			if len(s) == k {
				delete(s, nums[i-k])
			}
			s[nums[i]] = true
		}
	}
	return false
}
