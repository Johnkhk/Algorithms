### 572. Subtree of Another Tree ###
"""
Given 2 trees: root and subRoot, return true if there is a subtree of root==subRoot
Idea: use isSameTree() function in the preorder traversal
"""

# TC: O(n*m) where n and m are nodes in root and subRoot
# SC:  O(n+m)
def isSubtree(root, subRoot):
    def isSame(node,subroot):
        if not node and not subroot:
            return True
        if not node or not subroot:
            return False
        if node.val!=subroot.val:
            return False
        l = isSame(node.left,subroot.left)
        r = isSame(node.right,subroot.right)
        return l and r
    def dfs(root,subroot):
        if not root:
            return False
        if isSame(root,subroot):
            return True
        a=dfs(root.left,subroot)
        b=dfs(root.right,subroot)
        
        return a or b
    return dfs(root,subRoot)

### Advanced Approach (Merkle Hashing) ###
def isSubtree(s, t):
    from hashlib import sha256
    def hash_(x):
        S = sha256()
        S.update(x)
        return S.hexdigest()
        
    def merkle(node):
        if not node:
            return '#'
        m_left = merkle(node.left)
        m_right = merkle(node.right)
        node.merkle = hash_(m_left + str(node.val) + m_right)
        return node.merkle
        
    merkle(s)
    merkle(t)
    def dfs(node):
        if not node:
            return False
        return (node.merkle == t.merkle or 
                dfs(node.left) or dfs(node.right))
                    
    return dfs(s)