"""
idea 
"""

import heapq
from collections import defaultdict
### Heap Method ###
def minGroups(intervals):
    intervals.sort()
    h = [intervals[0][1]]
    for i in range(1,len(intervals)):
        if h and h[0]<intervals[i][0]: # meeting has ended
            top = heapq.heappop(h)
            heapq.heappush(h,intervals[i][1])
        else:
            heapq.heappush(h,intervals[i][1])
    return len(h)

### Line Sweep Method ###
"""
idea is to find return the max overlap
"""
def minGroups(intervals):
    change=defaultdict(int)
    for start, end in intervals:
        change[start]+=1
        change[end+1]-=1
    print(change)
    cur=0
    mx = 0
    for key in sorted(change.keys()):
        cur +=change[key]
        mx = max(mx, cur)
    return mx

### Separate start and end times ###
def minGroups(intervals):
    starts = sorted(a[0] for a in intervals)
    ends = sorted(a[1] for a in intervals)
    end_ptr=0
    res=0
    for s in starts:
        if s<=ends[end_ptr]:
            res+=1
        else:
            end_ptr+=1
    return res
    
        
