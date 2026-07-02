"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        
        old_to_new = {}
        old_to_new[None] = None

        # pass 1 - create all copied nodes
        curr = head
        while curr:
            copy = Node(curr.val)
            old_to_new[curr] =  copy
            curr = curr.next
        
        # Pass 2 - Connect next and random pointers
        curr = head
        while curr:
            copy = old_to_new[curr]
            copy.next = old_to_new[curr.next]
            copy.random = old_to_new[curr.random]
            curr = curr.next
        
        # Return the head of copied lists
        return old_to_new[head]