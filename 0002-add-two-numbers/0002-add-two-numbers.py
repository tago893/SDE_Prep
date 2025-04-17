# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, l1: Optional[ListNode]) -> Optional[ListNode]:
        temp = l1
        prev = None

        while temp!=None:
            next_node = temp.next
            temp.next = prev
            prev = temp
            temp = next_node
        return prev

    def addNodes(self,l1: Optional[ListNode]) -> int:
        temp = self.reverse(l1)
        number = 0
        while temp!= None:
            number = number * 10 + temp.val
            temp = temp.next
        return number
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        number1 = self.addNodes(l1)
        number2 = self.addNodes(l2)
        number3 = number1+number2
        # Create a new linked list for the result
        head = None
        current = None
        if number3 == 0:
            return ListNode(0)
        # Create the linked list from the digits of the sum
        while number3 > 0:
            digit = number3 % 10
            new_node = ListNode(digit)
            
            if head is None:
                head = new_node
                current = head
            else:
                current.next = new_node
                current = new_node
                
            number3 //= 10
        
        return head
        