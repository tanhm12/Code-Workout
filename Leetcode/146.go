package main

type DLLNode struct {
	Prev *DLLNode
	Next *DLLNode
	Key  int
	Val  int
}

type LRUCache struct {
	capacity int
	length   int
	head     *DLLNode
	tail     *DLLNode
	data     map[int]*DLLNode
}

func Constructor(capacity int) LRUCache {
	head := &DLLNode{}
	tail := &DLLNode{}
	head.Next = tail
	tail.Prev = head
	return LRUCache{capacity: capacity, length: 0, head: head, tail: tail,
		data: make(map[int]*DLLNode)}
}

func (this *LRUCache) MoveToHead(node *DLLNode) {
	if node.Next != nil {
		node.Next.Prev = node.Prev
		node.Prev.Next = node.Next
	}

	node.Next = this.head.Next
	node.Next.Prev = node
	this.head.Next = node
	node.Prev = this.head
}

func (this *LRUCache) Get(key int) int {
	if _, ok := this.data[key]; !ok {
		return -1
	}
	node := this.data[key]
	this.MoveToHead(node)

	return node.Val
}

func (this *LRUCache) Put(key int, value int) {
	var node *DLLNode
	if _, ok := this.data[key]; ok {
		this.data[key].Val = value
		this.MoveToHead(this.data[key])
		return
	} else if this.length == this.capacity {
		node = this.tail.Prev
		this.tail.Prev = node.Prev
		node.Prev.Next = this.tail
		delete(this.data, node.Key)
		this.length -= 1
	}
	node = &DLLNode{Val: value, Key: key}
	this.data[key] = node
	this.length += 1

	this.MoveToHead(node)

}

// Input
// ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
// [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
// Output
// [null, null, null, 1, null, -1, null, -1, 3, 4]

/**
 * Your LRUCache object will be instantiated and called as such:
 * obj := Constructor(capacity);
 * param_1 := obj.Get(key);
 * obj.Put(key,value);
 */
