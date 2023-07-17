from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1.val == 0:
            return l2
        elif l2.val == 0:
            return l1
        
        def get_sum(ll):
            s = 0
            while ll is not None:
                s = s*10 + ll.val
                ll = ll.next
            return s
        s1 = get_sum(l1)
        s2 = get_sum(l2)
        s = s1 + s2
        new_head = None
        while s > 0:
            cur = ListNode(s % 10)
            cur.next = new_head
            new_head = cur
            s = s // 10
        return new_head
        
        