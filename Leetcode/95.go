package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func cloneTree(node *TreeNode) *TreeNode {
	if node == nil {
		return nil
	}
	return &TreeNode{node.Val, cloneTree(node.Left), cloneTree(node.Right)}
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
					result = append(result, &TreeNode{i, cloneTree(leftTree), cloneTree(rightTree)})
				}
			}
		}
		return result
	}

}

func generateTrees(n int) []*TreeNode {
	return generateTrees2Params(1, n+1)
}
