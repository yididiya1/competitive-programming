class Solution:
    def kIncreasing(self, arr: List[int], k: int) -> int:
        
        def getIncresing(nums):
            f = []
            for i in range(len(nums)):
                if not f or nums[i] >= f[-1]:
                    f.append(nums[i])
                else:
                    pos = bisect.bisect_right(f, nums[i])
                    f[pos] = nums[i]
            return len(f)
        
        arrays = []
        curr = []
        for i in range(0,k):
            for j in range(i,len(arr),k):
                # print(i,j)
                curr.append(arr[j])
            arrays.append(curr)
            curr = []
        total = 0
        for a in arrays:
            x = getIncresing(a)
            # print(x)
            total += len(a) - x
            
        return total
            
        