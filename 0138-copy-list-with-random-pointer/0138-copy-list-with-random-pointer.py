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

        # Dummy node
        x = Node(0)
        temp2 = x
        temp = head
        i = 0

        # hash_map: index -> original.random node
        # new_list_map: index -> new node
        hash_map = {}
        new_list_map = {}

        # \U0001fa79 First pass: copy nodes & next pointers
        while temp:
            new_node = Node(temp.val)
            temp2.next = new_node
            hash_map[i] = temp.random     # store random target (original reference)
            new_list_map[i] = new_node    # store new node
            temp2 = temp2.next
            temp = temp.next
            i += 1

        # \U0001f9ed Second pass: assign random pointers
        # We'll find which index each original node corresponds to.
        # To do this, map old node -> index
        old_to_index = {}
        temp = head
        j = 0
        while temp:
            old_to_index[temp] = j
            temp = temp.next
            j += 1

        # Now go through each index and assign randoms in the new list
        for idx in range(i):
            original_random = hash_map[idx]  # old random node
            if original_random is not None:
                random_idx = old_to_index[original_random]
                new_list_map[idx].random = new_list_map[random_idx]

        return x.next
