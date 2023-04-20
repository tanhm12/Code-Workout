package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

type TreeNodeExtended struct {
	node  *TreeNode
	depth int
	pos   int // pos at depth
}

type Queue struct {
	data    []TreeNodeExtended
	pointer int
}

func (q *Queue) push(element TreeNodeExtended) {
	q.data = append(q.data, element)
}

func (q *Queue) pop() TreeNodeExtended {
	res := q.data[q.pointer]
	q.pointer += 1
	return res
}

func (q *Queue) empty() bool {
	return q.pointer >= len(q.data)
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

func widthOfBinaryTree(root *TreeNode) int {
	q := Queue{data: make([]TreeNodeExtended, 0), pointer: 0}
	q.push(TreeNodeExtended{root, 0, 0})
	var curNode TreeNodeExtended
	curDepth := 0
	curPos := 0
	var newDepth, newLeftPos int
	res := 1
	for !q.empty() {
		curNode = q.pop()
		if curNode.depth == curDepth {
			res = max(res, curNode.pos-curPos+1)
		} else {
			curDepth = curNode.depth
			curPos = curNode.pos
		}
		newDepth = curNode.depth + 1
		newLeftPos = 2 * curNode.pos
		if curNode.node.Left != nil {
			q.push(TreeNodeExtended{curNode.node.Left, newDepth, newLeftPos})
		}
		if curNode.node.Right != nil {
			q.push(TreeNodeExtended{curNode.node.Right, newDepth, newLeftPos + 1})
		}
	}
	return res
}
