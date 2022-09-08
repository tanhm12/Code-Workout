package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func travel(node *TreeNode, result *[]int) {
	if node == nil {
		return
	}
	travel(node.Left, result)
	*result = append(*result, node.Val)
	travel(node.Right, result)
}

func inorderTraversal(root *TreeNode) []int {
	result := make([]int, 0)
	travel(root, &result)
	return result
}
