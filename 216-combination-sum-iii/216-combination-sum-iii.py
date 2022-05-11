class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        res = []
        
        def backtrack(cur,pos,target):
            if target == 0 and len(cur) == k:
                res.append(cur.copy())
            if target <= 0 or len(cur) >= k:
                return 
            
            prev = -1
            
            for i in range(pos,10):
                if i == prev:
                    continue
                
                cur.append(i)
                backtrack(cur,i+1,target-i)
                cur.pop()
                prev = i
                
        
        backtrack([],1,n)
        return res
        
        