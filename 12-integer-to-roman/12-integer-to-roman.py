class Solution:
    def intToRoman(self, num: int) -> str:
        
        digits = {1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M'}
        
        def change_number(number,power):
            if number == 0:
                return "" 
            
            if number == 4 or number == 9:
                # print(power,number)
                high = digits[(number + 1) * (10**power)]
                low = digits[(10**power)]
                return low+high
            elif number < 4:
                return digits[10**power]*number
            else:
                high = digits[(5) * (10**power)]
                low = digits[(10**power)] * (number - 5)
                return high+low
                
        
        number = str(num)
        length = len(number)
        result = []
        
        for i in range(len(number)):
            result.append(change_number(int(number[i]),length-i-1))
        
        return "".join(result)
            
            
            
                
                
            
            
            
                    
                    
        