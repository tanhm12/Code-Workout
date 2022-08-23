class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def isPalindrome(head: ListNode):
    def find_mid(head: ListNode = head):
        one_jump = head
        two_jump = head
        
        while True:
            if two_jump.next is None:
                return one_jump.next
            if two_jump.next.next is None:
                return one_jump.next
            one_jump = one_jump.next
            two_jump = two_jump.next.next
            
    def reverse_next(node1, node2):
        old_head = node2.next
        new_head = node2
        new_head.next = node1
        
        return new_head, old_head
        
        
    old_head = find_mid(head)
    new_head = None
    while old_head is not None:
        new_head, old_head = reverse_next(new_head, old_head)
    
    # while new_head is not None:
    #     print(new_head.__dict__)
    #     new_head = new_head.next
    
    while new_head is not None:
        if  new_head.val != head.val:
            return False
        
        new_head = new_head.next
        head = head.next
    
    return True


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

ll = make_ll_from_array([1,2,3,2,1])

# while ll is not None:
#     # print(ll.__dict__)
#     ll = ll.next
    
print(isPalindrome(ll))