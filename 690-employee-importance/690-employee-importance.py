"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        importance = {}
        subordinates = {}
        
        
        for emp in employees:
            importance[emp.id] = emp.importance
            subordinates[emp.id] = emp.subordinates
        
        
        
        def dfs(_id):

            totalImp = importance[_id]
                    
            for sub in subordinates[_id]:
                totalImp += dfs(sub)
                
            return totalImp
                
        
        return dfs(id)
        