class Solution:
    def nextGreaterElement(self, n: int) -> int:
        n = list(str(n))
        n = [int(i) for i in n]
        
        index = None
        
        # print(n)
        
        for i in range(len(n)-1,-1,-1):
            if n[i] > n[i-1]:
                index = i-1
                break
        
        # print(index)     
        if index is not None and index >= 0:
            best = float('inf')
            idx = None
            for i in range(index+1,len(n)):
                if n[i] > n[index]:
                    if n[i] < best:
                        best = n[i]
                        idx = i
            
            if idx:
                # print(idx,"After")
                n[index],n[idx] = n[idx],n[index]

            l =index+1
            r = len(n) - 1
            
            while l <= r and n[l] > n[r]:
                n[l],n[r] = n[r],n[l]
                l += 1
                r -= 1

            n = [str(k) for k in n]
            n = "".join(n)
            if int(n) > 2**31 - 1:
                return -1
            
            return int(n)
        
            
        else:
            return -1
        