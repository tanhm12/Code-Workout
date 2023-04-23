package main

import "fmt"

func gen(cur, n int, res *[]int) {
	offset := cur % 10
	for i := offset; i < 10; i++ {
		if cur > n {
			break
		}
		*res = append(*res, cur)
		gen(cur*10, n, res)
		cur += 1
	}
}

func lexicalOrder(n int) []int {
	res := make([]int, 0)
	cur := 1
	gen(cur, n, &res)
	return res
}

func main() {
	n := 30
	fmt.Println(lexicalOrder(n))
}
