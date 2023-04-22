package main

// func min(a int, b int) int {
// 	if a <= b {
// 		return a
// 	} else {
// 		return b
// 	}
// }

// func minInsertionsCache(s string, i, j int, cache [][]int) int {
// 	if i >= j {
// 		return 0
// 	} else {
// 		if cache[i][j] > -1 {
// 			return cache[i][j]
// 		} else {
// 			if s[i] == s[j] {
// 				cache[i][j] = minInsertionsCache(s, i+1, j-1, cache)
// 			} else {
// 				cache[i][j] = min(minInsertionsCache(s, i+1, j, cache), minInsertionsCache(s, i, j-1, cache)) + 1
// 			}
// 			return cache[i][j]
// 		}
// 	}
// }

// func minInsertions(s string) int {
// 	dp := make([][]int, len(s)+1)
// 	for i := range dp {
// 		dp[i] = make([]int, len(dp))
// 		for j := range dp[i] {
// 			dp[i][j] = -1
// 		}
// 	}
// 	return minInsertionsCache(s, 0, len(s)-1, dp)
// }

func max(a ...int) int {
	res := a[0]
	for i := 0; i < len(a); i++ {
		if a[i] > res {
			res = a[i]
		}
	}
	return res
}

func longestPalindromeSubseq(s string) int {
	dp := make([][]int, len(s))
	for i, _ := range s {
		dp[i] = make([]int, len(s))
		dp[i][i] = 1
	}
	for i := len(s) - 2; i >= 0; i-- {
		for j := i + 1; j < len(s); j++ {
			if s[i] == s[j] {
				if i+1 == j {
					dp[i][j] = 2
				} else {
					dp[i][j] = max(2+dp[i+1][j-1], dp[i][j-1], dp[i+1][j])
				}
			} else {
				dp[i][j] = max(dp[i][j-1], dp[i+1][j])
			}
		}
	}

	return dp[0][len(s)-1]
}

// the problem can be reduced to find the longest palindrome subsequence in s or find the minium chars need to be removed to make s palindrome, because the minium chars need to be added is equal to that minimum chars being removed
func minInsertions(s string) int {
	return len(s) - longestPalindromeSubseq(s)
}
