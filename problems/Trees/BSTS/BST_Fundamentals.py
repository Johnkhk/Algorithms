"""
inorder traversal of BST is not unique
"""
"""
iterative inorder generally faster than recursive if westopping.
"""
### binary search closest value ###
# SC: O(h)
# SC: O(1)
def closestValue(self, root, target):
    r = root.val
    while root:
        if abs(root.val - target) < abs(r - target):
            r = root.val
        root = root.left if target < root.val else root.right
    return r

### inorder traversal of a BST returns sorted order of the values ###
def inorder(r):
    """
    returns the list in sorted order
    """
    return inorder(r.left) + [r.val] + inorder(r.right) if r else []

### get successor of a node iteratively ###
def successor(root):
    root = root.right
    while root.left:
        root = root.left
    return root

### get predecessor of a node iteratively ###
def predecessor(root):
    root = root.left
    while root.right:
        root = root.right
    return root

### Delete Node from BST (Uses successor and predecessor)###
def delete(root,key):
    """
    if none return none, nothing to delete
    recurse until we have same value
        - leaf node, just return None
        - has left child
    """
    if not root:
        return None
    if key<root.val:
        root.left=delete(root.left,key)
    elif key>root.val:
        root.right=delete(root.right,key)
    else:
        if not root.left and not root.right:
            root=None
        elif root.left:
            root.val = predecessor(root).val
            root.left=delete(root.left,root.val)
        elif root.right:
            root.val = successor(root).val
            root.right=delete(root.right,root.val,)
    return root
### Can also just use infunction (different method) ###
def delete(root,key):
    """
    1.) if not left return right
    2.) if not right return left
    3.) the top 2 cases covers if both are None return None
    4.) if has left and right replace with successor, then delete successor (call for right subtree)
    """
    if not root:
        return None
    if key<root.val:
        root.left=delete(root.left,key)
    elif key>root.val:
        root.right=delete(root.right,key)
    else:
        if not root.right: return root.left
        if not root.left: return root.right
        if root.left and root.right:
            temp = root.right
            while temp.left: temp = temp.left
            root.val = temp.val
            root.right = delete(root.right, root.val)
    return root