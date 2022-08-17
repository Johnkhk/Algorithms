### recursive ###
def diameterOfBinaryTree(root):
    """
    goal: 
        return the diameter of the tree, (length of longest path b/n 2 nodes)
        Also the # of edges
    Idea: 
        the diameter should be the height of leftsubtree + height of rightsubtree
        Where height is the max number of nodes from root to a leaf
        Use recursion to get height
        Keep a running global max of the diameter
        SC: O(n)
        TC: O(n)
    """ 
    mxdiameter=0
    def dfs(root):
        nonlocal mxdiameter
        if not root:
            return 0
        lheight=dfs(root.left)
        rheight=dfs(root.right)
        mxdiameter = max(mxdiameter,lheight+rheight)
        return max(lheight,rheight)+1
        
    dfs(root)
    return mxdiameter
