package main

func max(a ...int) int {
	res := a[0]
	for i := 0; i < len(a); i++ {
		if a[i] > res {
			res = a[i]
		}
	}
	return res
}

//// Recursive memoization
// func longestPalindrome(s string, i, j int, mem [][]int) int {
// 	if i > j {
// 		return 0
// 	} else if i == j {
// 		mem[i][j] = 1
// 		return 1
// 	} else {
// 		if mem[i][j] != -1 {
// 			return mem[i][j]
// 		} else if s[i] == s[j] {
// 			mem[i][j] = max(2+longestPalindrome(s, i+1, j-1, mem), longestPalindrome(s, i+1, j, mem), longestPalindrome(s, i, j-1, mem))
// 		} else {
// 			mem[i][j] = max(longestPalindrome(s, i+1, j, mem), longestPalindrome(s, i, j-1, mem))
// 		}
// 		return mem[i][j]
// 	}
// }

// func longestPalindromeSubseq(s string) int {
// 	mem := make([][]int, len(s))
// 	for i, _ := range s {
// 		mem[i] = make([]int, len(s))
// 		for j, _ := range s {
// 			mem[i][j] = -1
// 		}
// 	}
// 	res := longestPalindrome(s, 0, len(s)-1, mem)
// 	return res
// }

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
