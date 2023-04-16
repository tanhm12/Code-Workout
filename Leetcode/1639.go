package main

func numWays(words []string, target string) int {
	n := len(words[0])
	m := len(target)
	if m > n {
		return 0
	}
	mod := int64(1000000007)
	counter := make([][]int, n)
	for i := 0; i < n; i++ {
		counter[i] = make([]int, 26)
		for _, w := range words {
			counter[i][int(w[i])-97]++
		}
	}

	dp := make([][]int64, m+1)
	dp[0] = make([]int64, n+1)
	for i := 0; i <= n; i++ {
		dp[0][i] = 1
	}

	/*
		dp[i, j] is the number of ways to form target[:i] using first j characters of all string in words
		dp[i, j] = k * dp[i-1, j-1] + dp[i, j-1] where
			k is the number of string s in words where s[j-1] == target[i-1]
			for s in words if s[j-1] == target[i-1]:  k * dp[i-1, j-1] is the case to form target[:i] from target[:i-1] and target[i-1] (from words)
			for others s remain: dp[i, j-1]
	*/
	for i := 1; i <= m; i++ {
		dp[i] = make([]int64, n+1)
		for j := i; j <= n; j++ {
			// beware of redundant sum (must be dp[i][j-1], not sum(dp[i][x]) where x from i to j-1)
			dp[i][j] = (int64(counter[j-1][int(target[i-1])-97])*dp[i-1][j-1] + dp[i][j-1]) % mod
		}
	}

	return int(dp[m][n])
}
