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
        if not head:
            return None

        dummy = Node(0)
        temp2 = dummy
        temp = head

        # Maps
        old_to_index = {}
        index_to_random = {}
        index_to_newnode = {}

        i = 0
        # \U0001f539 First pass: copy list & record mappings
        while temp:
            new_node = Node(temp.val)
            temp2.next = new_node

            old_to_index[temp] = i
            index_to_random[i] = temp.random
            index_to_newnode[i] = new_node

            temp2 = new_node
            temp = temp.next
            i += 1

        # \U0001f539 Second pass: assign random pointers
        for idx, old_random_node in index_to_random.items():
            if old_random_node:
                random_idx = old_to_index[old_random_node]
                index_to_newnode[idx].random = index_to_newnode[random_idx]

        return dummy.next

