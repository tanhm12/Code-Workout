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

func max(a ...int) int {
	res := a[0]
	for i := 0; i < len(a); i++ {
		if a[i] > res {
			res = a[i]
		}
	}
	return res
}

func solve(cookies []int, cur_sol []int, pos int, sol *int) {
	if pos >= len(cookies) {
		// fmt.Println(cur_sol)
		*sol = min(*sol, max(cur_sol...))
	} else {
		for j := 0; j < len(cur_sol); j++ {
			cur_sol[j] += cookies[pos]
			if cur_sol[j] >= *sol {
				cur_sol[j] -= cookies[pos]
				continue
			}
			solve(cookies, cur_sol, pos+1, sol)
			cur_sol[j] -= cookies[pos]
		}

	}
}

func distributeCookies(cookies []int, k int) int {
	cur_sol := make([]int, k)
	sol := 8 * 100000
	solve(cookies, cur_sol, 0, &sol)
	return sol
}

func main() {
	cookies := []int{6, 1, 3, 2, 2, 4, 1, 2}
	k := 8
	fmt.Println(distributeCookies(cookies, k))
}
