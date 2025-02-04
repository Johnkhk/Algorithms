"""
path is defined as no forking, or no returning
"""

def maxpathsum(root):

    def dfs(root):
        """
        returns the max path length without splitting
        """
        nonlocal mx
        if not root:
            return 0
        
        l = max(0,dfs(root.left))
        r = max(0,dfs(root.right))
        # compute max with split
        mx = max(mx,l+r+root.val)
        return root.val + max(l,r)
    
    mx = float("-inf")
    dfs(root)
    return mx