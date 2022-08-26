from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int):
        all_nodes = [head]
        while head is not None:
            head = head.next
            all_nodes.append(head)
        
        if n + 1 == len(all_nodes):
            return all_nodes[1]
        else:
            n = len(all_nodes) - 1 - n
            all_nodes[n-1].next = all_nodes[n+1]
            
            return all_nodes[0]
            
        