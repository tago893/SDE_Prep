# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pos = -1
        isCycle = False
        slow = head
        fast = head
        second = None
        first = head
        index = 0
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                second = slow
                break
        while second:
            if first == second:
                return second
            first = first.next
            second = second.next
        return second