# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        """
        Idea is to calculate the excess coins you have
        because this is the amount of moves you need to make.
        0 coins: means you need 1 coin (-1) (make 1 move)
        4 coins: means you have excess of 3 coin (+3) (make 3 moves)
        
        
        Below is the basic intuition behind this problem:

        Root asks the left subtree, how much do you need or you've got extra? I'll give that/take it away to/from you via our direct edge, and pass it to right child, and if something remains, I'll take it.
        Same question is asked to the right child.
        Answer will be the sum of values(absolute) returned after the asked questions from the left(Left) and right(Right).
        But what should the root return to its parent? It will return that how much does "his tree" need/has extra. That will be the signed sum of its Left+Right (question's answer) + same question asked to current root node.
        """
        
        ans=0
        def dfs(root):
            """
            excess amount of coins in the subtree at or below this node
            which is the # of coins in subtree - # of nodes in subtree
            So for example1: this will be 3:0, 0:-1, 0:-1
            """
            nonlocal ans
            if not root:
                return 0
            l=dfs(root.left)
            r=dfs(root.right)
            ans+= (abs(l)+abs(r))
            
            print(root.val-1+l+r)
            return root.val-1+l+r # how many coins excess for a node
        dfs(root)




"""        
Below is the basic intuition behind this problem:

Root asks the left subtree, how much do you need or you've got extra? 
I'll give that/take it away to/from you via our direct edge, 
and pass it to right child, and if something remains, I'll take it.
Same question is asked to the right child.
Answer will be the sum of values(absolute) returned after the asked 
questions from the left(Left) and right(Right).
But what should the root return to its parent? 
It will return that how much does "his tree" need/has extra. 
That will be the signed sum of its Left+Right (question's answer) + same question asked to current root node.
"""
moves=0
def dfs(root):
    nonlocal moves
    if not root:
        return 0
    l=dfs(root.left)
    r=dfs(root.right)          
    
    # because we have exactly n coins and n nodes,
    # if left needs 1 and right needs 1, at this node we make 2 moves
    # we do += because the children may have needed to make moves for this root
    moves += abs(l)+abs(r)
    
    return l+r+root.val-1 # how much my left needs, how much my right needs and how much i need (excess i have)
dfs(root)
return moves