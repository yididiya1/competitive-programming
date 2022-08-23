class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        count = 0
        while maxDoubles > 0 and target > 1:
            if target%2 != 0:
                target -= 1
                count += 1
            else:
                target //= 2
                count += 1
                maxDoubles -= 1
 
        if target > 1:
            return count + target - 1
        return count