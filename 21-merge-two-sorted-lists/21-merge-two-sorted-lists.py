# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        answer = ListNode()
        curr = answer
        
        while list1 and list2:
            first = list1.val
            second = list2.val           
            if first <= second:
                curr.next = list1
                curr = curr.next
                list1 = list1.next
            else:
                curr.next = list2
                curr = curr.next
                list2 = list2.next
            
        while list1:
            curr.next = list1
            curr = curr.next
            list1 = list1.next
            
        while list2:
            curr.next = list2
            curr = curr.next
            list2 = list2.next
            
        return answer.next
            
            
                
                
        
        
        