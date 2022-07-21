class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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


def hasCycle(head: ListNode):
    one_jump = head
    two_jump = head
    counter = 1
    
    while True:
        if one_jump == None or two_jump == None or two_jump.next is None:
            return False
        
        if one_jump is two_jump:
            counter -= 1
            if counter < 0:
                return True
        
        one_jump = one_jump.next
        two_jump = two_jump.next.next




ll = make_ll_from_array([1,2,3,2,1])

node = ll
while node.next is not None:
    # print(ll.__dict__)
    node = node.next

# node.next = ll

# counter = 100
# while ll is not None:
#     print(ll.__dict__)
#     ll = ll.next
    
#     counter -= 1
#     if counter < 0:
#         break

    
print(hasCycle(ll))