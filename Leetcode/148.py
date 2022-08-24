from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def __init__(self):
        self.dummy_head = ListNode()
        self.cur = self.dummy_head
        
    def find_mid(self, head: ListNode):
        one_jump = head
        two_jump = head
        
        while True:
            if two_jump.next is None:
                return one_jump
            if two_jump.next.next is None:
                return one_jump
            one_jump = one_jump.next
            two_jump = two_jump.next.next
            
            
    def merge(self, head1: ListNode, head2: ListNode):
        self.cur = self.dummy_head
        while head1 is not None and head2 is not None:
            if head1.val <= head2.val:
                self.cur.next = head1
                head1 = head1.next
            else:
                self.cur.next = head2
                head2 = head2.next
            self.cur = self.cur.next
        
        if head1 is None:
            head1 = head2
        
        while head1 is not None:
            self.cur.next = head1
            head1 = head1.next
            self.cur = self.cur.next
        
        return self.dummy_head.next
        
    def sortList(self, head: Optional[ListNode]):
        if head is None or head.next is None:
            return head
        else:
            
            mid = self.find_mid(head)
            # print(head.val, mid.val)
            ll2 = self.sortList(mid.next)
            mid.next = None
            ll1 = self.sortList(head)
            
            return self.merge(ll1, ll2)
        

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

ll0 = make_ll_from_array([1, 2])
ll = make_ll_from_array([1,2,3,4, 5])
ll2 = make_ll_from_array([2,3,4, 5])
# ll3 = make_ll_from_array([-1,5,3,4,0])
ll3 = make_ll_from_array([2, 1, -1])

# ll = Solution().merge(ll, ll2)
# print(Solution().find_mid(ll0).val)
ll = Solution().sortList(ll3)

while ll is not None:
    print(ll.__dict__)
    ll = ll.next
        