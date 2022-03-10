# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        curr = dummy
        carry = 0
        
        while l1 and l2:
            _sum = l1.val+l2.val+carry
            carry = _sum//10
            curr.next = ListNode(_sum%10)
            l1 = l1.next
            l2 = l2.next
            curr = curr.next
            
        while l1:
            _sum = l1.val+carry
            carry = _sum//10
            curr.next = ListNode(_sum%10)
            l1 = l1.next
            curr = curr.next
            
        while l2:
            _sum = l2.val+carry
            carry = _sum//10
            curr.next = ListNode(_sum%10)
            l2 = l2.next
            curr = curr.next
        
        
        if carry != 0:
            curr.next = ListNode(carry)
        
        return dummy.next
        
        
        
        
        
            
            
        
        