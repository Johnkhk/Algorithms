### 108. Convert Sorted Array to Binary Search Tree ###
def sortedArrayToBST(nums):
    def dfs(nums):
        if not nums:
            return None
        
        N = len(nums)
        
        BST = TreeNode(nums[N//2])
        
        if N==1:
            return BST
        
        BST.left = dfs(nums[:N//2])
        BST.right = dfs(nums[N//2+1:])
        
        return BST

    return dfs(nums)

### 109. Convert Sorted List to Binary Search Tree ###
# Very good problem
"""
Algorithm:
    - have a helper function that find the middle element using slow & fast ptr technique
    - this helper function also disconnects the mid from the left portion
    - Then recursively build your answer.
        Key steps:
        - mid = helper(head)
        - BST(mid.val)
        - bst.left = dfs(head)
        - bst.right = dfs(mid.next)
"""


def sortedListToBST(head):
    def getMiddle(root):
        """
        gets the middle element, and disconnect the left of mid
        """
        prev=None
        slow=fast=root
        
        while fast and fast.next:
            prev=slow
            slow=slow.next
            fast=fast.next.next
        # disconnect
        if prev:
            prev.next=None
        return slow
    
    def dfs(root):
        if not root:
            return None
        
        # get middle LL node
        mid = getMiddle(root)
        # create treeNode
        BST = TreeNode(mid.val)
        
        # base case
        if root==mid:
            return BST
        
        # root is disconnected at this point (to its mid)
        BST.left = dfs(root)
        # start from the node after mid
        BST.right = dfs(mid.next)
        return BST

    return dfs(head)