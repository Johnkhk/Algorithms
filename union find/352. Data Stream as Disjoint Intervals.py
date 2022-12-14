# class SummaryRanges:
    
#     def __init__(self):
#         self.parents = {}
#         self.intervals = {}

#     def find(self, x):
#         if x not in self.parents:
#             return None
#         if x != self.parents[x]:
#             self.parents[x] = self.find(self.parents[x])
#         return self.parents[x]
    
#     def union(self, x, y):
#         px, py = self.find(x), self.find(y)
#         if px == None or py == None:
#             return
#         self.parents[px] = py # just pick one of them # make py the important one # so we get rid of px's intervals
#         mirange = min(self.intervals[px][0],self.intervals[py][0])
#         mxrange = max(self.intervals[px][1],self.intervals[py][1])
#         self.intervals[py] = [mirange,mxrange]
#         del self.intervals[px]
        

#     def addNum(self, val):
#         if val in self.parents:
#             return
#         self.parents[val] = val
#         self.intervals[val] = [val,val]
#         self.union(val, val-1)
#         self.union(val, val+1)

#     def getIntervals(self):
#          return sorted(self.intervals.values())

### sorted container solution
from sortedcontainers import SortedList
class SummaryRanges:
    def __init__(self):
        self.sl = SortedList()

    def addNum(self, val):
        self.sl.add((val,val))
        
        

    def getIntervals(self):
        r = list(self.sl)
        self.sl = SortedList()
        stack = [] # we want a monotonic increasing stack

        # e.g
        # [1,1],[2,2] -> [1,2]
        # [1,3],[3,3],[4,5] -> [1,5]
        # [1,2],[4,5],[6,6] -> [1,2],[4,6]
        for s,e in r:
            if stack and stack[-1][1]+1>=s: # if the stack's end greater than start we need to merge
                ts,te = stack.pop()
                stack.append((min(s,ts),max(e,te)))
            else:
                stack.append((s,e))
        
        for s,e in stack:
            self.sl.add((s,e))

        return stack

sr = SummaryRanges()
sr.addNum(1)
sr.addNum(3)
sr.addNum(5)
# sr.addNum(2)
sr.addNum(6)
# sr.addNum(7)
sr.addNum(4)



print(sr.getIntervals())

# print(sr.parents)
# print(sr.intervals)


