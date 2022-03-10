# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
       
        nonduplicate = ListNode()
        nd = nonduplicate
        
        if not head:
            return 
        
        prev = head 
        curr = head.next 
        
        duplicate = -101
        
        
        while curr and prev:
            if prev.val != curr.val :
                if prev.val != duplicate:
                    nd.next = ListNode(prev.val)
                    nd = nd.next
            else:
                duplicate = prev.val
            
            prev = curr
            curr = curr.next
            
        if prev and  prev.val != duplicate:
            nd.next = ListNode(prev.val)
            
        return nonduplicate.next
                
                