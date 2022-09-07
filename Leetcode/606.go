package main

import (
	"fmt"
	"strings"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func travel(node *TreeNode, res *[]string) {
	if node == nil {
		return
	} else {
		*res = append(*res, fmt.Sprint(node.Val))
		if node.Left == nil && node.Right == nil {
			return
		}
		*res = append(*res, "(")
		travel(node.Left, res)
		*res = append(*res, ")")
		if node.Right == nil {
			return
		}
		*res = append(*res, "(")
		travel(node.Right, res)
		*res = append(*res, ")")
	}

}

func tree2str(root *TreeNode) string {
	res := make([]string, 0)
	travel(root, &res)
	return strings.Join(res, "")
}
