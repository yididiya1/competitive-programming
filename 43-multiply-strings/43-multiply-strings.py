class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        carry  = 0
        curr = None
        prev = None
        ans = ""
        
        if len(num1) < len(num2):
            num1 , num2 = num2 , num1
        
        def adder(n1,n2):
            ans = []
            carry = 0
            
            
            i1 = len(n1) - 1
            i2 = len(n2) - 1
            
            while i1 >= 0 and i2 >= 0 :
                no = int(n1[i1]) + int(n2[i2]) + carry
                carry =  no // 10
                prod = no % 10
                ans.append(str(prod))
                i1 -= 1
                i2 -= 1 
            
            while i1 >= 0:
                no = int(n1[i1]) + carry
                carry =  no // 10
                prod = no % 10
                ans.append(str(prod))
                i1 -= 1
            
            while i2 >= 0:
                no = int(n2[i2]) + carry
                carry =  no // 10
                prod = no % 10
                ans.append(str(prod))
                i2 -= 1
            
            if carry > 0:
                ans.append(str(carry))
                
            ans.reverse()
            return "".join(ans)
            
                  
                
            
        
        def multiplier(n1,n2):
            carry = 0
            ans = []
            for i in range(len(n1)-1,-1,-1):
                no = (int(n1[i]) * int(n2)) + carry
                carry =  no // 10
                prod = no % 10
                ans.append(str(prod))
            if carry > 0:
                ans.append(str(carry))
            ans.reverse()  
            return "".join(ans)
         
        tracker = 1
        
        for i in range(len(num2)-1,-1,-1):
            # print(num1,num2[i],curr,prev)
            # if num2[i] != '0':
                curr = multiplier(num1 ,num2[i])
                # print("Multiper " ,curr)
                if prev:
                    temp = prev[-tracker:]
                    # print("temp ",temp)
                    prev = adder(prev[:-tracker],curr)
                    prev = prev + temp
                    tracker += 1
                else:
                    prev = curr
                
        if not prev:
            return "0"
        prev = prev.lstrip("0")
        if prev == "":
            return "0"
        return prev
            
           