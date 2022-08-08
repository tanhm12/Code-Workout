package main

import (
	"fmt"
)

func min(a int, b int) int {
	if a <= b {
		return a
	} else {
		return b
	}
}

func reverseStr(s string, k int) string {
	res := make([]byte, 0)
	for i := 0; i < len(s); i += 2 * k {
		for j := min(len(s), i+k) - 1; j >= i; j-- {
			res = append(res, s[j])
		}
		for j := min(len(s), i+k); j < min(len(s), i+2*k); j++ {
			res = append(res, s[j])
		}
	}
	return string(res)
}

func main() {
	s := "abcdefg"
	k := 7

	fmt.Println(reverseStr(s, k))
}
