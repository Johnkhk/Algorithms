# Inorder Iterative DFS
def closestValue(root, target):
    stack=[]
    prev=float("-inf")

    while root:
        stack.append(root)
        root=root.left
    root = stack.pop()
    if target>prev and target<root.val:
        return min(prev,root.val,key=lambda x: abs(x-target))
    prev = root.val
    root=root.right
    return prev

### Recursive Inorder DFS ###
def closestValue(root, target):
    res,diff=root.val,float("inf")
    Flag=False
    # prev=float("inf")
    prev=float("-inf")
    def inorder(root):
        nonlocal res,diff,prev,Flag
        if root==None:
            return
        inorder(root.left)
        if target>=prev and target<=root.val:
            Flag=True
            res= min(prev,root.val, key=lambda x : abs(target-x))
        # print(prev,root.val)
        prev = root.val
        inorder(root.right)  

    inorder(root)
    if Flag:
        return res
    else: 
        return prev

### Clean Binary Search (most optimal) ###
# SC: O(h)
# SC: O(1)
def closestValue(self, root, target):
    r = root.val
    while root:
        if abs(root.val - target) < abs(r - target):
            r = root.val
        root = root.left if target < root.val else root.right
    return r

### EVEN CLEANER ###
# HOWEVER THIS IS O(N)
def closestValue(self, root, target):
    def inorder(r):
        """
        returns the list in sorted order
        """
        return inorder(r.left) + [r.val] + inorder(r.right) if r else []
        
    return min(inorder(root), key = lambda x: abs(target - x))