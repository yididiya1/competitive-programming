class Solution(object):
    def fizzBuzz(self, n):
        list = []
        list2 = []
        counter = n
        for x in range(1,n+1):
            if(n%3 == 0 and n%5 == 0):
                list.append("FizzBuzz")
                n = n - 1
            elif(n%3 == 0):
                list.append("Fizz")
                n = n -1
            elif(n%5 == 0):
                list.append("Buzz")
                n = n -1            
            else:
                list.append(str(n))
                n = n -1
        
        
        
        
        return list[::-1]
        
