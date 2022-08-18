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