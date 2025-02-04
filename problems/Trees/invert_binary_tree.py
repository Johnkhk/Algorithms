from collections import deque
### Recursive Solution ###
def invertTree(root):
    # goal: invert binary tree
    # idea: 
    """
    When we are at None, return None
    recursively call invert on the subtree, when we are at a leaf, nothing happens
    
    """
    if not root:
        return None
    
    # have to do it on the same line because:
    """
    root.right = self.invertTree(root.left) 
    root.left = self.invertTree(root.right)
    root.right already reassigned
    """
    root.right,root.left = invertTree(root.left),invertTree(root.right)
    return root

### Iterative Solution ###
def invertTree(root):
    # goal: invert binary tree
    # idea: 
    """
    Use Level order BFS to reassign nodes
    """
    q=deque([root])
    while q:
        node=q.pop()
        if node and (node.left or node.right):
            node.left,node.right=node.right,node.left
            q.append(node.left)
            q.append(node.right)
    return root
                    
