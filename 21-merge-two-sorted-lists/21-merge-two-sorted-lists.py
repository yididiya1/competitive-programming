# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        output = []
        while list1 != None or list2 != None:
            if(list1!=None and list2!=None):
                output.append(list1.val)
                output.append(list2.val)
                list1 = list1.next
                list2 = list2.next
            elif(list1!= None):
                output.append(list1.val)
                list1 = list1.next
            else:
                output.append(list2.val)
                list2 = list2.next
                
        output.sort()
        # print(output)
        
        def createLL(n):
            if n == len(output) - 1:
                return ListNode(output[n])
            return ListNode(output[n],createLL(n+1))
        
        
        
        if not output:
            if list1 == None:
                return list1
            else:
                return list2
        
        result = createLL(0)
        return result
        
#         result = createLL(0)
        
#         return result
        
        
        