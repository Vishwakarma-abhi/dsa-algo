# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        ans_node = ListNode(-1)
        sum_node = ans_node
        carry = 0
        while l1 or l2:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0

            total = num1+ num2 + carry

            carry = total // 10
            digit = total % 10

            sum_node.next = ListNode(digit)

            sum_node = sum_node.next
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry != 0:
            sum_node.next = ListNode(carry)
        
        return ans_node.next
