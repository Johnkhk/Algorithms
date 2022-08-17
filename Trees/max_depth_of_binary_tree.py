### recursive ###
"""
Goal: get the maximum depth of binary tree, (Longest path from root to leaf)
Idea: recurse, and return the max height up to the caller
TC: O(n)
SC: O(logn)
"""
def dfs(root):
    if not root:
        return 0
    l = dfs(root.left)
    r = dfs(root.right)
    return max(l,r)+1

### iterative ###
"""
Goal: get the maximum depth of binary tree, (Longest path from root to leaf)
Idea: do level order traversal of the tree
TC: O(n)
SC: O(logn)
"""
if not root:
    return 0
q = deque([(root,1)])
mx = 1
while q:
    node,level = q.popleft()
    mx = max(mx,level)
    if node.left:
        q.append((node.left,level+1))
    if node.right:
        q.append((node.right,level+1))
return mx