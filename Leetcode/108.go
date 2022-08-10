package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func travel(nums []int, left int, right int) *TreeNode {
	if left > right {
		return nil
	}
	var mid int = (left + right) / 2
	// fmt.Printf("%d %d %d %d\n", mid, nums[mid], left, right)

	node := TreeNode{
		Val:   nums[mid],
		Left:  travel(nums, left, mid-1),
		Right: travel(nums, mid+1, right),
	}
	// fmt.Println(node.Val, node.Left, node.Right)

	return &node

}

func sortedArrayToBST(nums []int) *TreeNode {
	root := travel(nums, 0, len(nums)-1)
	return root
}

func main() {
	nums1 := []int{1, 2, 3, 4, 5, 6}

	// nums1 := []int{0, 0}
	// m := 1
	// nums2 := []int{1}
	// n := 1

	sortedArrayToBST(nums1)
}
