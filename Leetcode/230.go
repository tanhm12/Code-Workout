package main

/*
*
Definition for a binary tree node.
*/
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func count(node *TreeNode, k int, currentPosition int) (int, int) {
	if node == nil {
		return currentPosition, -1
	}
	left, val := count(node.Left, k, currentPosition)
	if val != -1 {
		return 0, val
	}
	left = left + 1
	if left == k {
		return left, node.Val
	} else {
		right, val := count(node.Right, k, left)
		if val != -1 {
			return 0, val
		}
		return right, -1
	}
}

func kthSmallest(root *TreeNode, k int) int {
	_, res := count(root, k, 0)
	return res
}
