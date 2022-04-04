# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        
        def createLL(l):
            dummy = ListNode()
            curr = dummy
            for num in l:
                curr.next = ListNode(num)
                curr = curr.next
            return dummy.next
        
        arr = []
        curr = head
        
        while curr:
            arr.append(curr.val)
            curr = curr.next
          
        
        index = k - 1
        arr[index],arr[-k] = arr[-k],arr[index]
        
        
        
        return createLL(arr)
        
        
        
        