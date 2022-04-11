class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        requires = {recipe:[] for recipe in recipes}
        indegree =  [0 for i in range(len(recipes))]
        
        for i in range(len(ingredients)):
            for j in range(len(ingredients[i])):
                if  ingredients[i][j] not in supplies  :
                    if ingredients[i][j] in requires:
                        requires[ingredients[i][j]].append(i)
                    indegree[i] += 1
                    # requires[ingredients[i][j]].append(i)     
                
        
        
        
        queue = deque()            
        output = []
        
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:
            recipe = queue.popleft()
            output.append(recipes[recipe])
            
            for i in requires[recipes[recipe]]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)
                    
        return output
                
            
             