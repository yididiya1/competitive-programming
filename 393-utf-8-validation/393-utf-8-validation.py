class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        
        data = [bin(d)[2:] for d in data]
        
        def checkPossible(bit):
            count = 0
            
            for i,c in enumerate(bit):
                if c == '0':
                    return i
                else:
                    count += 1
            
            return len(bit)
        
        for i,d in enumerate(data):
            if len(d) < 8:
                x = '0' * (8 - len(d))
                data[i] = x+d
                
        # print(data)
        
        l = 0 
        
        while l < len(data):
            x = checkPossible(data[l]) 
            # print(x,l)
            if x == 0:
                l += 1
            elif x > 4 or x == 1:
                return False
            else:
                if l+(x) > len(data):
                    # print("We Out")
                    return False
                else:
                    temp = l
                    l += 1
                    while l <= temp+(x-1):
                        if data[l].startswith('10'):
                            l += 1
                        else:
                            return False

                    # l += 1
                    # print("End At",l)
        
        return True
                    
            
            