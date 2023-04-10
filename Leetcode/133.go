package main

type Node struct {
	Val       int
	Neighbors []*Node
}

func travel(refNode, node *Node, mark map[int]*Node) {
	for _, refNeighbor := range refNode.Neighbors {
		if _, ok := mark[refNeighbor.Val]; !ok {
			newNode := &Node{refNeighbor.Val, make([]*Node, 0)}
			mark[refNeighbor.Val] = newNode
			travel(refNeighbor, newNode, mark)
		}
		node.Neighbors = append(node.Neighbors, mark[refNeighbor.Val])
	}
}

func cloneGraph(node *Node) *Node {
	if node == nil {
		return nil
	}
	clonedNode := &Node{node.Val, make([]*Node, 0)}
	mark := make(map[int]*Node, 0)
	mark[node.Val] = clonedNode
	travel(node, clonedNode, mark)
	return clonedNode
}
