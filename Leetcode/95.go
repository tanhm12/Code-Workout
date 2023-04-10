package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func generateTrees2Params(left, right int) []*TreeNode {
	if left == right {
		return []*TreeNode{nil}
	} else {
		result := make([]*TreeNode, 0)
		for i := left; i < right; i++ {
			leftTrees := generateTrees2Params(left, i)
			rightTrees := generateTrees2Params(i+1, right)
			for _, leftTree := range leftTrees {
				for _, rightTree := range rightTrees {
					result = append(result, &TreeNode{i, leftTree, rightTree})
				}
			}
		}
		return result
	}

}

func generateTrees(n int) []*TreeNode {
	return generateTrees2Params(1, n+1)
}
