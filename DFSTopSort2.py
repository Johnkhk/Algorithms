#2115. Find All Possible Recipes from Given Supplies

def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
    def dfs(r):
        if r not in can_make:
            can_make[r] = False
            if r in graph:
                can_make[r] = all([dfs(i) for i in graph[r]])
        return can_make[r]
    
    can_make = {s: True for s in supplies}
    graph = {r : ing for r, ing in zip(recipes, ingredients)}
    return [r for r in recipes if dfs(r)]