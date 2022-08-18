class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        def dfs(root,val):
            if not root:
                return BST(val)
            if value<root.value:
                root.left=dfs(root.left,value)
            elif value>=root.value:
                root.right=dfs(root.right,value)
            return root
        dfs(self,value)
        return self

    def contains(self, value):
        def dfs(root,value):
            if not root:
                return False
            if root.value<value:
                return dfs(root.right,value)
            elif root.value>value:
                return dfs(root.left,value)
            else:
                return True
        return dfs(self,value)
        
    def remove(self, value, parent=None):
        curnode=self
        while curnode is not None:
            if curnode.value<value:
                parent = curnode
                curnode=curnode.right
            elif curnode.value>value:
                parent = curnode
                curnode=curnode.left
            else:
                if curnode.left and curnode.right:
                    curnode.value = curnode.right.getmin()
                    curnode.right.remove(curnode.value, curnode)
                elif parent is None:
                    if curnode.left is not None:
                        curnode.value = curnode.left.value
                        curnode.right = curnode.left.right
                        curnode.left = curnode.left.left
                    elif curnode.right is not None:
                        curnode.value = curnode.right.value
                        curnode.left = curnode.right.left
                        curnode.right = curnode.right.right
                    else:
                        print("wut")
                        pass
                elif parent.left == curnode:
                    parent.left = curnode.left if curnode.left else curnode.right
                elif parent.right == curnode:
                    parent.right = curnode.right if curnode.right else curnode.left
                break

        return self
	
    def getmin(self):
        curnode = self
        while curnode.left:
            curnode=curnode.left
        return curnode.value

	
