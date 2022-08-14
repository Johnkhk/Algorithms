"""
Summary:
To come up with this solution myself.
Think of the max area a paticular height will have.
if a height is in a rectangle, no smaller heights are in that rectabgle, only bigger ones can have smaller rectangle cutoff below them. 
Then the issue is to find the left and right boundary where the bars are shorter than x
According to the code, when a bar is popped out from the stack, we know it must be higher than the bar at position i, 
so bar[i] must be the right boundary (exclusive) of the rectangle, and the previous bar in the stack is the first one that is shorter than the popped one so it must be the left boundary (also exclusive). Then we find the rectangle.
SO ABOUT TO ENTER IS RIGHT BOUNDARY
POPPED IS THE HEIGHT
LEFT IS THE LEFT BOUNDARY
"""


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


### EVEN MORE ELEGANT SOLUTION ###
height = [5,4,3,2,1]

height.append(0)
stack = [-1]
ans = 0
for i in range(len(height)):
    while height[i] < height[stack[-1]]:
        h = height[stack.pop()]
        w = i - stack[-1] - 1
        ans = max(ans, h * w)
    stack.append(i)
height.pop()
print(ans)

### Most intuituve Solution (Neetcode) ###
maxArea = 0
stack=[]

for i,h in enumerate(heights):
    startidx=i
    while stack and stack[-1][1] > h:
        idx,hpop = stack.pop()
        maxArea = max(maxArea, (i-idx)*hpop)
        startidx=idx # push back the start index
    stack.append([startidx,h])

while stack:
    idx,hpop = stack.pop()
    maxArea = max(maxArea, (len(heights)-idx)*hpop)
    
return  maxArea