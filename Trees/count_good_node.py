
"""
pass the max down
"""
count=0
def dfs(root,mx):
    nonlocal count
    if not root:
        return
    # print(root.val,mx)
    if mx<=root.val:
        count+=1
    dfs(root.left,max(mx,root.val))
    dfs(root.right,max(mx,root.val))
dfs(root,float("-inf"))
return count