
### Recursive level order ###
levels=[]
def dfs(root,level):
    if len(levels)==level:
        levels.append([])
    levels[level].append(root.val)
    if root.left:
        dfs(root.left,level+1)
    if root.right:
        dfs(root.right,level+1)
dfs(root,0)

### Iterative ###
q = deque([root])
res=[]
while q:
    tmp=[]
    for i in range(len(q)):
        node=q.popleft()
        tmp.append(node.val)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    res.append(tmp)
