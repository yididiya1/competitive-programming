# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        #iterative
        
        prev , cur = None , head
        
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            
        return prev
        
        
        
#         #recursive
#         def reverse(node):
#             if not node:
#                 return None
            
#             newhead = node
#             if node.next:
#                 newhead = reverse(node.next)
#                 node.next.next = node
            
#             node.next = None
#             return newhead
        
#         return reverse(head)
        