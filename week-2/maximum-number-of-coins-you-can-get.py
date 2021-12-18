def maxCoins(piles):
        piles.sort()
        alice = 0
        me = 0
        bob = 0
        i = 0
        j = len(piles) -1 
        while i < j:
            alice += piles[j]
            me += piles[j-1]
            bob += piles[i]
            i += 1
            j -= 2
        
        return me

example = maxCoins([2,4,1,2,7,8])
print(example)

        
            