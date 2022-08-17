from collections import deque
### Recursive ###
def isSameTree(p,q):
    """
    goal:
        given 2 roots, p & q, check if they are same
    idea:
        preorder traverse both trees together, and check if theeir values are same
    """

    def dfs(p,q):
        if not p and not q:
            return True
        if not p and q:
            return False
        if p and not q:
            return False
        if p.val!=q.val:
            return False
        l = dfs(p.left,q.left)
        r = dfs(p.right,q.right)
        return l and r
    return dfs(p,q)

### Iterative ###
def isSameTree(p,q):
    """
    goal:
        given 2 roots, p & q, check if they are same
    idea:
        Iteratively:
        traverse preorder together with stack, check if they are same
    """
    if p and q:
        stack=deque([(p,q)])
    elif p or q:
        return False
    else:
        return True

    while stack:
        p,q = stack.pop()
        if p.val!=q.val:
            return False
        if p.left and q.left:
            stack.append((p.left,q.left))
        elif p.left or q.left:
            return False
        if p.right and q.right:
            stack.append((p.right,q.right))
        elif p.right or q.right:
            return False
    return True
### cleaner Iterative ###
def isSameTree(p, q):
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool
    """    
    def check(p, q):
        # if both are None
        if not p and not q:
            return True
        # one of p and q is None
        if not q or not p:
            return False
        if p.val != q.val:
            return False
        return True
    
    deq = deque([(p, q),])
    while deq:
        p, q = deq.popleft()
        if not check(p, q):
            return False
        
        if p:
            deq.append((p.left, q.left))
            deq.append((p.right, q.right))
                
    return True