from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        

class Solution:
    def oddEvenList(self, head: Optional[ListNode]):
        if head is None or head.next is None:
            return head
        
        ohead, op = head, head
        ehead, ep = head.next, head.next
        
        while True:
            if ep.next is None:
                break
            op.next = ep.next
            op = op.next
            
            
            ep.next = op.next
            if op.next is None:
                break
            ep = ep.next
        
        op.next = ehead
        
        return ohead
    
    

def make_ll_from_array(arr):
    head = ListNode()
    node = head
    
    for i, item in enumerate(arr):
        node.val = item
        if i == len(arr) - 1:
            node.next = None
            break
        node.next = ListNode()
        node = node.next
    
    node = None
    return head

ll = make_ll_from_array([1,2,3,4, 5])

ll = Solution().oddEvenList(ll)
while ll is not None:
    print(ll.__dict__)
    ll = ll.next
            
            
        