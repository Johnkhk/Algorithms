"""
very good question
width is defined as the length between 2 end nodes, where if in between are Null are still counter
algorith:
    do a level order traversal with index of node
    at a new level, record the index of first popped
    and at other nodes in same level maximize the window size
"""

### Level Order Traversal ###
def widthOfBinaryTree(root):
    q = deque([(root,1)])
    mx=float("-inf")
    while q:
        start=float("inf")
        for i in range(len(q)):
            node,idx_pop = q.popleft()
            if i==0:
                start = idx_pop
            mx=max(mx,idx_pop-start+1)

            if node.left:
                q.append((node.left,idx_pop*2))
            if node.right:
                q.append((node.right,idx_pop*2+1))
            
    return mx


### DFS + hashmap ###
def widthOfBinaryTree(root):
    # because preorder traversal goes left to right, we c an always gaurantee we see left ones first
    mp={} # map stores the first idx seen
    mx=float("-inf")
    def dfs(root,level,idx):
        nonlocal mx
        if not root:
            return
        if level not in mp:
            mp[level]=idx
        mx = max(mx,idx-mp[level]+1)
        
        dfs(root.left,level+1,idx*2)
        dfs(root.right,level+1,idx*2+1)

    dfs(root,1,1)
    return mx
                