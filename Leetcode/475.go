package main

import "sort"

func check(houses []int, heaters []int, radius int) bool {
	h := 0
	s, e := 0, 0
	for i := 0; i < len(heaters); i++ {
		s = heaters[i] - radius
		e = heaters[i] + radius
		for ; h < len(houses); h++ {
			if houses[h] < s {
				return false
			} else if houses[h] > e {
				break
			}
		}
		if h >= len(houses) {
			return true
		}
	}
	return h >= len(houses)
}

func findRadius(houses []int, heaters []int) int {
	sort.Slice(heaters, func(i, j int) bool {
		return heaters[i] < heaters[j]
	})
	sort.Slice(houses, func(i, j int) bool {
		return houses[i] < houses[j]
	})

	l := 0
	r := houses[len(houses)-1]
	if r < heaters[len(heaters)-1] {
		r = heaters[len(heaters)-1]
	}
	radius := 0
	for l < r {
		radius = (l + r) / 2
		if check(houses, heaters, radius) {
			r = radius
		} else {
			l = radius + 1
		}
	}
	return l
}
