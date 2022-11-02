package main

func isToeplitzMatrix(matrix [][]int) bool {
	m := len(matrix)
	n := len(matrix[0])
	var cur int
	for i := 0; i < m; i++ {
		cur = matrix[i][0]
		for j := 1; j < n; j++ {
			if i >= m || j >= n {
				break
			}
			if matrix[i+j][j] != cur {
				return false
			}
		}
	}
	for i := 0; i < m; i++ {
		cur = matrix[i][0]
		for j := 1; j < n; j++ {
			if i >= m || j >= n {
				break
			}
			if matrix[j][j+i] != cur {
				return false
			}
		}
	}

	return true
}
