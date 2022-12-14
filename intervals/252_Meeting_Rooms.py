### Sorting, uses a stack (my sol) ###
def canAttendMeetings(intervals):
    if not intervals:
        return True
    intervals.sort()
    stack=[intervals[0][1]]
    for inter in intervals[1:]:
        if inter[0]<stack[-1]:
            return False
        stack.append(inter[1])
    return True

### Sorting, No Stack ###
def canAttendMeetings(intervals):
    if not intervals:
        return True
    intervals.sort()
    for i in range(1,len(intervals)):
        if intervals[i][0]<intervals[i-1][1]:
            return False
    return True