
"""
because we are going left to right,
we use a monotonic increasing queue for maximum area,
this is because if its 6,7,5,
anything to the right of 5 will be limited to 5's height..
To know if monoinc stack or monodec stack, see what we do not need going left to right. 

For a min area, we will use a monodec stack
this is because wehn going left to right, we see something bigger,
everything to the right of that bigger thing will not give an area smaller than the ..
IDK
"""
from itertools import chain


### Cleanest Solution I have ever seen ###
heights = [5,4,3,2,1]

maxArea = 0
stack = [] # list[(column, height)]
for i, height in enumerate(chain([0], heights, [0])): # append zero heights at both ends
    while stack and stack[-1][1] > height:
        rect_right = i
        rect_height = stack.pop()[1]
        rect_left = stack[-1][0]
        area = (rect_right - rect_left - 1) * rect_height
        maxArea = max(area, maxArea)
    stack.append((i, height))
print(maxArea)


