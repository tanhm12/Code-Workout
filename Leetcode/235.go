package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func swap(a, b *int) {
	c := *a
	*a = *b
	*b = c
}

func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
	min_val := p.Val
	max_val := q.Val
	if min_val > max_val {
		swap(&min_val, &max_val)
	}
	if min_val <= root.Val && root.Val <= max_val {
		return root
	} else if root.Val < min_val {
		return lowestCommonAncestor(root.Right, p, q)
	} else {
		return lowestCommonAncestor(root.Left, p, q)
	}
}
