# Non-overlapping intervals
import heapq
### Heap Solution (didn't get) ###
"""
Explanation: we sort the interval, add endtimes to a heap and see if the meeting has ended. 
if it has, we pop it off and add the new room, (reuse same room)
oterhwise, we need a new meeting room, so we just add it to the heap.
"""
def minMeetingRooms(intervals):
    intervals.sort()
    h = [intervals[0][1]]
    for i in range(1,len(intervals)):
        if h[0]<=intervals[i][0]: # meeting has ended
            top = heapq.heappop(h)
            heapq.heappush(h,intervals[i][1])
        else: # Meeting hasn't ended
            heapq.heappush(h,intervals[i][1])
            
            
    return len(h)

### separate start times and end times ###
def minMeetingRooms(intervals):
    starts = sorted(a[0] for a in intervals)
    ends = sorted(a[1] for a in intervals)
    end_ptr=0
    res=0
    for s in starts:
        if s<ends[end_ptr]:
            res+=1
        else:
            end_ptr+=1
    return res

### Line Sweep Method ###
# Line Sweep Method
def minMeetingRooms(intervals):
    change=defaultdict(int)
    for start, end in intervals:
        change[start]+=1
        change[end]-=1
    # print(change)
    cur=0
    mx = 0
    for key in sorted(change.keys()):
        cur +=change[key]
        mx = max(mx, cur)
    return mx
                