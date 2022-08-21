def distanceK(root,target):
    adj=defaultdict(list)
    
    def dfs(root):
        if not root:
            return
        
        if root.left:
            adj[root].append(root.left)
            adj[root.left].append(root)
            dfs(root.left)
        
        if root.right:
            adj[root].append(root.right)
            adj[root.right].append(root)
            dfs(root.right)
    dfs(root)
    visited = set()
    res=[]
    q=deque([(target,0)])
    while q:
        node,dist = q.popleft()
        if dist==k:
            res.append(node.val)
        visited.add(node)
        for nei in adj[node]:
            if nei not in visited:
                q.append((nei,dist+1))
    return res