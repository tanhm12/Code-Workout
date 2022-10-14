package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func deleteMiddle(head *ListNode) *ListNode {
	if head.Next == nil {
		return nil
	}

	onep := head
	twop := head
	prep := onep

	for {
		if twop.Next == nil {
			break
		}
		if twop.Next.Next == nil {
			prep = onep
			break
		}
		prep = onep
		onep = onep.Next
		twop = twop.Next.Next
	}
	prep.Next = prep.Next.Next
	return head
}

// def find_mid(head: ListNode = head):
//         one_jump = head
//         two_jump = head

//         while True:
//             if two_jump.next is None:
//                 return one_jump.next
//             if two_jump.next.next is None:
//                 return one_jump.next
//             one_jump = one_jump.next
//             two_jump = two_jump.next.next
