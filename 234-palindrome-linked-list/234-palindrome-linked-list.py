# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast,slow = head,head
        
        half = []
        
        while fast!=None and fast.next!=None:
            
            fast = fast.next.next
            half.append(slow.val)     
            slow = slow.next
          
        if fast:
            half.append(slow.val)
          
        #print(half)
        counter = -1
        
        while slow!= None:
            if slow.val != half[counter]:
                return False
            slow = slow.next
            counter -= 1
        return True    
        
        