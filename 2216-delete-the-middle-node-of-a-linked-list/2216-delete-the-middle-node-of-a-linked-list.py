# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        middle_index = 1
        size = 1
        while temp.next:
            size += 1
            temp = temp.next
        if size == 1:
            head = None
        else:    
            
            middle_node = head
            temp = head
            while middle_index <= size//2:
                middle_node = middle_node.next
                middle_index += 1
            print([middle_node.val,middle_index])
            if middle_node.next != None:
                middle_node.val = middle_node.next.val
                middle_node.next = middle_node.next.next
            else:
                head.next = None 


        return head