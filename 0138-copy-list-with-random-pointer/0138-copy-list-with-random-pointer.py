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
        if head == None:
            return None
        old_to_new  = {}
        c = head
        while c:
            old_to_new[c] = Node(c.val)
            c = c.next
        
        c = head
        while c:
            old_to_new[c].next = old_to_new.get(c.next)
            old_to_new[c].random = old_to_new.get(c.random)
            c = c.next
        
        return old_to_new[head]