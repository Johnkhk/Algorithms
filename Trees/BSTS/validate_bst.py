def isValidBST(root):
    mx,mi=float("inf"),float("-inf")
    def dfs(root,mx,mi):
        if not root:
            return True
        print(root.val,mi,mx)
        if root.val>=mx or root.val<=mi:
            return False
        return dfs(root.left,root.val,mi) and dfs(root.right,mx,root.val)
    return dfs(root,mx,mi)