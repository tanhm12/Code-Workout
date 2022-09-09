package main

import (
	"fmt"
)

func isPalindrome(arr string, i int, j int) bool {
	for i < j {
		if arr[i] != arr[j] {
			return false
		}
		i++
		j--
	}
	return true
}

func validPalindrome(s string) bool {
	i := 0
	j := len(s) - 1
	for i < j {
		if s[i] != s[j] {
			return isPalindrome(s, i+1, j) || isPalindrome(s, i, j-1)
		}
		i++
		j--
	}
	return true
}

func main() {
	s := "abca"
	fmt.Println(validPalindrome((s)))
}
