package main

func abs(num int) int {
	if num >= 0 {
		return num
	} else {
		return -num
	}
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

func min(a ...int) int {
	res := a[0]
	for i := 0; i < len(a); i++ {
		if a[i] < res {
			res = a[i]
		}
	}
	return res
}

func maxConsecutiveAnswers(answerKey string, k int) int {
	ct := 0
	cf := 0
	t := "T"[0]
	first := 0
	var diff int
	res := k
	for i := 0; i < len(answerKey); i++ {
		if answerKey[i] == t {
			ct += 1
		} else {
			cf += 1
		}
		diff = min(ct, cf)
		for ; diff > k; first++ {
			if answerKey[first] == t {
				ct -= 1
			} else {
				cf -= 1
			}
			diff = min(ct, cf)
		}
		res = max(res, ct+cf)
	}
	return res
}
