class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        answer = []
        
        def backtrack(index,_sum,arr):
            # print(index,_sum,arr)
            if _sum == 0:
                answer.append(arr.copy())
                return 
            if _sum < 0:
                return 
            
            prev = -1
            
            for i in range(index,len(candidates)):
                if candidates[i] == prev:
                    continue
                # print("To be added ", arr,candidates[i])  
                arr.append(candidates[i])
                # print("After Adding ",arr)
                backtrack(i,_sum - candidates[i],arr)
                arr.pop()
                prev = candidates[i]
                
        backtrack(0,target,[])
        return answer
                
        