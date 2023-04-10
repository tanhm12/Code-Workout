package main

func makeMap(brackets string) map[byte]int {
	result := make(map[byte]int)
	for i := 0; i < len(brackets); i++ {
		result[brackets[i]] = i
	}
	return result
}
func isValid(s string) bool {
	openBrackets := makeMap("({[")
	closeBrackets := makeMap(")}]")
	stack := make([]int, 0)
	var c byte

	for i := 0; i < len(s); i++ {
		c = s[i]
		if _, ok := openBrackets[c]; ok {
			stack = append(stack, openBrackets[c])
		} else {
			if len(stack) == 0 {
				return false
			} else if stack[len(stack)-1] != closeBrackets[c] {
				return false
			} else {
				stack = stack[:len(stack)-1]
			}
		}
	}
	return len(stack) == 0
}
