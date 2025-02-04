class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def serialize(root):
    """Encodes a tree to a single string.
    
    :type root: TreeNode
    :rtype: str
    """
    s=[]
    def dfs(node):
        if not node:
            s.append("N")
            return
        s.append(str(node.val))
        dfs(node.left)
        dfs(node.right)
    dfs(root)
    return ",".join(s)
def deserialize(data):
    """Decodes your encoded data to tree.
    
    :type data: str
    :rtype: TreeNode
    """
    data=data.split(",")
    i=0
    def dfs():
        nonlocal i
        if data[i]=="N":
            i+=1
            return None
        node = TreeNode(int(data[i]))
        i+=1
        node.left = dfs()
        node.right= dfs()
        return node
    root = dfs()
    return root