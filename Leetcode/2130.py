from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        def find_middle(head):
            one = head
            two = head
            while one and two and two.next and two.next.next:
                two = two.next.next
                one = one.next
            return one.next
        
        def reverse(node):
            cur = None
            next_node = node
            count = 0
            while next_node is not None:
                next_node = node.next
                node.next = cur
                cur = node
                node = next_node
                count += 1
            
            return cur, count
        
        middle = find_middle(head)
        last, half = reverse(middle)
        res = 0
        for i in range(half):
            res = max(res, head.val + last.val)            
            head = head.next
            last = last.next
        
        return res

        
                    
