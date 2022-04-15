# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        size = 0
        curr = head
           
        while curr:
            size += 1
            curr = curr.next
            
        temp = head
        count = 1
        
        k = min(k,size-k+1)
        
        swap = None
        
        
        while temp:
            if count == k:
                swap = temp
            if count == size-k+1:
                swap.val,temp.val = temp.val,swap.val
                break
            temp = temp.next
            count += 1
        
        return head
        
        
        
        