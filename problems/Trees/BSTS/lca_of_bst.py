
def dfs(root):
    if q.val<root.val and p.val<root.val:
        return dfs(root.left)
    elif p.val>root.val and q.val>root.val:
        return dfs(root.right)
    else:
        return root
