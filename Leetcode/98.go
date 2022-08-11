package main

import (
	"fmt"
	"math"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func validate(node *TreeNode, min_val int64, max_val int64) bool {
	if node == nil {
		return true
	} else if (node.Left == nil || node.Left.Val < node.Val && int64(node.Left.Val) > min_val) && (node.Right == nil || node.Right.Val > node.Val && int64(node.Right.Val) < max_val) {
		return validate(node.Left, min_val, int64(node.Val)) && validate(node.Right, int64(node.Val), max_val)
	}
	return false
}

func isValidBST(root *TreeNode) bool {
	return validate(root, math.MinInt64, math.MaxInt64)
}

func main() {
	fmt.Printf("%d %d", math.MaxInt32, math.MinInt32)
}
