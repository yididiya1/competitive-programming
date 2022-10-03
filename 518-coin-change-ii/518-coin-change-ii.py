class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        @cache
        def numberofCombination(_sum,index):
            if _sum == amount:
                    return 1
            if _sum > amount or index >= len(coins):	
                    return 0
            take_again = numberofCombination(_sum+coins[index],index)
            skip = numberofCombination(_sum,index+1)
                
            return skip + take_again
        
        return numberofCombination(0,0)