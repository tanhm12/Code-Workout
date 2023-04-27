package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func buildTreeIdx(preorder []int, inorder []int, preorderIdx *int, inorderStart, inorderEnd int) *TreeNode {
	if inorderStart >= inorderEnd {
		return nil
	}
	val := preorder[*preorderIdx]
	*preorderIdx += 1
	node := &TreeNode{val, nil, nil}
	for i := inorderStart; i < inorderEnd; i++ {
		if inorder[i] == val {
			node.Left = buildTreeIdx(preorder, inorder, preorderIdx, inorderStart, i)
			node.Right = buildTreeIdx(preorder, inorder, preorderIdx, i+1, inorderEnd)
			return node
		}
	}
	return nil
}

func buildTree(preorder []int, inorder []int) *TreeNode {
	preorderIdx := 0
	return buildTreeIdx(preorder, inorder, &preorderIdx, 0, len(inorder))
}
