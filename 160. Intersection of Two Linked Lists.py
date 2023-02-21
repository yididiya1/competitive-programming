# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        lenA = 0
        lenB = 0
        currA = headA
        currB = headB
        
        while currA:
            currA = currA.next
            lenA += 1

        while currB:
            currB = currB.next
            lenB += 1

        if lenA < lenB:
            headA,headB = headB,headA
            lenA,lenB = lenB,lenA

        newCurrA = headA
        newCurrB = headB
        while lenA > lenB and newCurrA:
            newCurrA = newCurrA.next
            lenA -= 1

        
        while newCurrA != newCurrB and newCurrA is not None and newCurrB is not None:
            newCurrA = newCurrA.next
            newCurrB = newCurrB.next

        return newCurrA
