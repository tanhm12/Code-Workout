class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseBetween(head: ListNode, left: int, right: int):
    head_ = head
            
    def reverse_next(node1, node2):
        old_head = node2.next
        new_head = node2
        new_head.next = node1
        
        return new_head, old_head
    
    start = None
    for i in range(left-1):
        start = head
        head = head.next
    
    old_head = head
    new_head = None
    for j in range(right-left+1):
        new_head, old_head = reverse_next(new_head, old_head)
    
    if start is not None:
        start.next = new_head
    else:
        head_ = new_head
    head.next =  old_head
    
    return head_


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


# ll = make_ll_from_array([1,2,3,4,5])
# res = reverseBetween(ll, left = 2, right = 4)

# ll = make_ll_from_array([5])
# res = reverseBetween(ll, left = 1, right = 1)


ll = make_ll_from_array([1,2,3,4,5])
res = reverseBetween(ll, left = 1, right = 5)

while res is not None:
    print(res.val)
    res = res.next

