package main

import "fmt"

func findIndex(value int, arr []int, from int) int {
	for ; from >= 0; from-- {
		if arr[from] <= value {
			return from + 1
		}
	}
	return 0
}

func min(a ...int) int {
	res := a[0]
	for i := 0; i < len(a); i++ {
		if a[i] < res {
			res = a[i]
		}
	}
	return res
}

func mincostTickets(days []int, costs []int) int {
	res := []int{0}
	for i := 0; i < len(days); i++ {
		fmt.Println(i, days[i], findIndex(days[i]-7, days, i))
		val := min(
			costs[0]+res[i],
			costs[1]+res[findIndex(days[i]-7, days, i)],
			costs[2]+res[findIndex(days[i]-30, days, i)],
		)
		res = append(res, val)
	}
	return res[len(res)-1]
}

func main() {
	days := []int{1, 4, 6, 7, 8, 20}
	costs := []int{2, 7, 15}

	fmt.Println(mincostTickets(days, costs))

}
