from BuildTree import *
from collections import deque
############### Inorder ###############
# (of a BST it becomes sorted)
arr="4,2,1,N,N,3,N,N,5,N,N" # Preorder Representation
root = deserialize(arr)
stack=[]
while stack or root:
    while root:
        stack.append(root)
        root=root.left
    root = stack.pop()
    print(root.val)
    root=root.right
    
############### Post Order ###############
print("post order")
arr="3,9,N,N,20,15,N,N,7,N,N"
root = deserialize(arr)
stack=[]
while root or stack:
    if root:
        stack.append(root)
        root=root.left
    else:
        tmp = stack[-1].right
        if tmp:
            root = tmp
        else:
            tmp = stack.pop()
            print(tmp.val)
            while stack and tmp==stack[-1].right:
                tmp=stack.pop()
                print(tmp.val)

############### Level Order ###############
print("level order")
# arr="4,2,1,N,N,3,N,N,5,N,N"
arr="3,9,N,N,20,15,N,N,7,N,N"
root = deserialize(arr)
q=deque([root])
while q:
    print([a.val for a in list(q)])
    for i in range(len(q)):
        node = q.popleft()
        # print(node.val)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
