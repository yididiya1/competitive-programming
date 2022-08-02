class Solution:
    def isHappy(self, n: int) -> bool:
        
        checked = set()
        
        def rec(num):
            
            temp = num
            
            if num in checked:
                return False
            
            num = str(num)
            num = list(num)
            _sum = 0
            
            for i in num:
                _sum += int(i) ** 2
            # print(_sum)
            if _sum == 1:
                return True
            else:
                checked.add(temp)
                return rec(_sum)
            
        
        return rec(n)
        