"""
idea is simple:
we have 3 states:
covered: the node is covered by a camera
notcovered: the node is not covered by a camera
camera: the node is a camera

We also want to be greedy. So when we hit a leaf node we want it to be not covered.
This is so the leaf's our parent can be a camera.
For the base case (NULL Node), we put it as "covered" instead of "notcovered" to avoid putting a camera on the leaf
Then we just return what our state should be given we know the state of our children. 

Final edge case: the root node needs to be covered, or a camera, so we check if it is "notcovered".
if it is we add 1 more camera to our final result.
"""

def minCameraCover(root) -> int:
    numcameras=0
    def dfs(root):
        nonlocal numcameras
        if not root:
            return "covered"
        
        l=dfs(root.left)
        r=dfs(root.right)
        
        if l=="notcovered" or r=="notcovered":
            numcameras+=1
            return "camera"
        elif l=="camera" or r=="camera":
            return "covered"
        
        return "notcovered"

    if dfs(root)=="notcovered":
        return 1+numcameras
    return numcameras