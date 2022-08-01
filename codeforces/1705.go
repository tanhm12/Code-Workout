package main

import "fmt"

type Pair struct {
	l int
	r int
}

func readIntInput(length int) []int {
	arr := make([]int, length+1)

	for i := 0; i < length; i++ {
		fmt.Scanf("%d", &arr[i])
	}
	return arr
}

func readPairInput(length int) []Pair {
	arr := make([]Pair, length+1)

	for i := 0; i < length; i++ {
		p := Pair{}
		fmt.Scanf("%d %d", &p.l, &p.r)
	}
	return arr
}

func solve(n int, c int, q int, commands []Pair, queries []int, s string) {
	n = 0
}

func main() {
	var t, n, c, q int
	var s string
	fmt.Scanf("%d", &t)
	for i := 0; i < t; i++ {
		fmt.Scanf("%d %d %d", &n, &c, &q)
		fmt.Scanf("%s", &s)
		commands := readPairInput(c)
		queries := readIntInput(q)
		solve(n, c, q, commands, queries, s)
	}
}
