class Solution:
    def jump(self, nums: List[int]) -> int:
        
        queue = deque([(0,0)])
        visited = set()
        
        while queue:
            # print(queue)
            n = len(queue)
            for i in range(n):
                cur,jump = queue.popleft()
                if cur >= len(nums)-1:
                    return jump
                maxjump = nums[cur]
                while maxjump > 0:
                    if cur+maxjump not in visited:
                        visited.add(cur+maxjump)
                        queue.append((cur+maxjump,jump+1))
                        maxjump -= 1
                    else:
                        break
            
            