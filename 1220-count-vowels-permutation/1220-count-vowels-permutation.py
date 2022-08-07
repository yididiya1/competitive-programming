class Solution:
    def countVowelPermutation(self, n: int) -> int:
        
        mapp = {'a':['e'],'e':['a','i'],'i':['a','e','o','u'],'u':['a'],'o':['i','u']}
        total = 0
        
        @cache
        def dp(letter,length):
            if length == n:
                return 1
            
            myTotal = 0
            for neighbour in mapp[letter]:
                myTotal += dp(neighbour,length+1)
                
            return myTotal
        
        
        for key in mapp:
            total += dp(key,1)
            
        return total%(10**9 + 7)
                
        