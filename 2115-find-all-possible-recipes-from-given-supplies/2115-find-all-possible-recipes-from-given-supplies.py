class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        requires = {recipe:[] for recipe in recipes}
        indegree = [0] * len(recipes)
        supplies = set(supplies)
        
        for i in range(len(ingredients)):
            for j in range(len(ingredients[i])):
                if ingredients[i][j] not in supplies:
                    if ingredients[i][j] in requires:
                        requires[ingredients[i][j]].append(i)
                    indegree[i] += 1
            
        
        queue = deque()
        
        
        
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
         
        # print(queue)
        answer = []
        while queue:
            rec = queue.popleft()
            answer.append(recipes[rec])
            
            for i in requires[recipes[rec]]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)
                    
        return answer
            
        