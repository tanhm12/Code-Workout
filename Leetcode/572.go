package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
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

func dfs(node *TreeNode, res *[][]int) int {
	if node == nil {
		return 0
	}
	left := dfs(node.Left, res)
	right := dfs(node.Right, res)
	height := max(left, right) + 1
	*res = append(*res, []int{node.Val, height})
	return height
}

func compareData(a1 []int, a2 []int) bool {
	return a1[0] == a2[0] && a1[1] == a2[1]
}

func isSubtree(root *TreeNode, subRoot *TreeNode) bool {
	rootValues := make([][]int, 0)
	subRootValues := make([][]int, 0)

	dfs(root, &rootValues)
	dfs(subRoot, &subRootValues)

	last := len(subRootValues) - 1
	mid := (last + 1) / 2
	j := 0
	for i := 0; i <= len(rootValues)-last; i++ {
		if compareData(rootValues[i], subRootValues[j]) && compareData(rootValues[i+mid], subRootValues[mid]) && compareData(rootValues[i+last], subRootValues[last]) {
			ok := true
			for k := 0; k <= last; k++ {
				if !compareData(rootValues[i+k], subRootValues[k]) {
					ok = false
					break
				}
			}
			if ok {
				return true
			}
		}
	}
	return false
}
