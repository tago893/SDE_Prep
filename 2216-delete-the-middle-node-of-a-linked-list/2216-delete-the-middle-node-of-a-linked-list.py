# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = ListNode(0)
        prev.next = head
        fast = head
        slow = prev
        if head == None:
            return None
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        slow.next = slow.next.next


        return prev.next