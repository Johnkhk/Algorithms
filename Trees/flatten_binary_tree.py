def dfs(root):
    # base case
    if not root:
        return None
    # leaf case, we need this or else the leaf will return None 
    # (due to us returning right child)
    if not root.left and not root.right:
        return root
    
    l=dfs(root.left) # flattened left side-> and return me the tail
    r=dfs(root.right) # flattened right side-> and return me the tail
    if l:
        l.right=root.right
        root.right=root.left
        root.left=None
    
    # return right tail of node-> the leaf gets None,None
    # the leaf's parent gets None None
    return r if r else l
dfs(root)