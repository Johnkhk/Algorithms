def pruneTree(root):
    def containsOne(root):
        if not root:
            return False
        
        if root.val==1:
            return True
        
        return containsOne(root.left) or containsOne(root.right)
    
    def dfs(root):
        if not root:
            return None
        if containsOne(root.left):
            dfs(root.left)
        else:
            root.left=None
        if containsOne(root.right):
            dfs(root.right)
        else:
            root.right=None
        
        if not containsOne(root):
            return None
        return root
    
    return dfs(root)

### With Memo
def pruneTree(root):
    memo = {}
    def containsOne(root):
        if root in memo:
            return memo[root]
        if not root:
            return False
        
        if root.val==1:
            return True
        ret = containsOne(root.left) or containsOne(root.right)
        memo[root] = ret
        return ret

    def dfs(root):
        if not root:
            return None
        if containsOne(root.left):
            dfs(root.left)
        else:
            root.left=None
        if containsOne(root.right):
            dfs(root.right)
        else:
            root.right=None
        
        if not containsOne(root):
            return None
        return root

    return dfs(root)
            

### MUCH CLEANER (Do it inside contains_one)
def pruneTree(root):

    def contains_one(node):
        if not node: 
            return False
        
        left_contains_one = contains_one(node.left)
        right_contains_one = contains_one(node.right)
        if not left_contains_one: 
            node.left = None
        if not right_contains_one: 
            node.right = None
        root_contains_one = True if node.val==True else False
        # Return True if the current node or its left or right subtree contains a 1.
        return root_contains_one or left_contains_one or right_contains_one

    # Return the pruned tree if the tree contains a 1, otherwise return None.
    if contains_one(root):
        return root
    else:
        return None