# Q3
class Allocator:
    """
    goal: to have an allocator where we can allocate blocks with size and mID. Free(mID) should free all those blocks
    idea: to use 2 arrays. 
            arr will signify what index in memory taken. 
            res will signify for a mID, what indices in arr they correspond to
    """
    def __init__(self, n: int):
        self.arr=[0]*n # 1 id index x is taken, 0 otherwise
        self.res=[[] for _ in range(1001)] # a list of all indices with ID equal to x (mID<=1000)

    def allocate(self, size: int, mID: int) -> int:
        streak=0
        n = len(self.arr)
        for i in range(n):
            if self.arr[i]==1:
                streak=0
            else:
                streak+=1
                if streak==size:
                    l=i-size+1
                    for j in range(streak):
                        self.arr[j+l]=1
                        self.res[mID].append(j+l)
                    return l
        return -1
                    

    def free(self, mID: int) -> int:
        freed=0
        # print(self.res[mID])
        for i in range(len(self.res[mID])):
            idx = self.res[mID][i]
            print(idx)
            self.arr[idx]=0
            freed+=1
        self.res[mID] = []
        return freed

# Q4

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m = len(grid)
        n = len(grid[0])
        heap = [(grid[0][0], 0, 0)]
        v = {(0, 0)}
        order = []
        while len(heap) > 0:
            curr, i, j = heapq.heappop(heap)
            order.append(curr)
            for x, y in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
                if 0 <= x < m and 0 <= y < n and (x, y) not in v:
                    v.add((x, y))
                    heapq.heappush(heap, (grid[x][y], x, y))
        print(order)
        maxYet = -1
        for i in range(len(order)):
            maxYet = max(maxYet, order[i])
            order[i] = maxYet
        print(order)
        
        res = []
        for q in queries:
            res.append(bisect.bisect_left(order, q))
        return res