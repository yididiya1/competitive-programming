# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head
        second_half = []
        _max = float('-inf')
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        if fast:
            slow = slow.next
            
        while slow:
            second_half.append(slow.val)
            slow= slow.next
            
        curr = head
        while second_half:
            pair1 = second_half.pop()
            _max = max(_max,pair1+curr.val)
            curr = curr.next
            
        return _max
        