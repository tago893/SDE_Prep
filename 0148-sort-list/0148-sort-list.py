# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self,head1: Optional[ListNode],head2: Optional[ListNode]) -> Optional[ListNode]:
            left = head1
            right = head2
            result = ListNode(0)
            curr = result
            while left and right:
                if left.val <right.val:
                    curr.next = left
                    left = left.next
                else:
                    curr.next = right
                    right = right.next
                curr = curr.next
            if left:
                curr.next = left
            if right:
                curr.next = right
            
            return result.next
    
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head
        
         # Use slow/fast to find mid
        prev = None
        slow = head
        fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        # Split the list into two halves
        prev.next = None
        
        left = self.sortList(head)
        right = self.sortList(slow)
        return self.merge(left,right)

