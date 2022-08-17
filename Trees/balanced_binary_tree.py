### 110. Balanced Binary Tree ###
### recursive ###
"""
goal:
    return whether binary tree is balanced
    balanced means left & right subtrees differ in height by no more than 1
idea:
    recursion
    calculate the height of all nodes
    at the parent, check if nodes differ by 1
"""        
BalancedFlag=True
def dfs(root):
    nonlocal BalancedFlag
    if not root:
        return 0
    
    lh=dfs(root.left)
    rh=dfs(root.right)
    if abs(lh-rh)>1:
        BalancedFlag=False
        return 0
    return max(lh,rh)+1
dfs(root)
return BalancedFlag