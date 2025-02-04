import heapq

### 703. Kth Largest Element in a Stream ###
class KthLargest:
    """
    Use a minheap of size K. 
    That way the smallest element is always the Kth largest!
    """
    def __init__(self, k: int, nums: List[int]):
        self.k=k
        # self.h=heapq.heapify([-i for i in nums])
        self.h=nums
        heapq.heapify(self.h)
        while len(self.h) >k:
            heapq.heappop(self.h)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.h,val)
        if len(self.h)>self.k:
            heapq.heappop(self.h)
        return self.h[0]

### 973. K Closest Points to Origin ###
def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    """
    idea: use a max heap of size k.
    hold (dist_to_orig, [pointx,pointy])
    return the heap
    """
    
    h = []
    for x,y in points:
        heapq.heappush(h,(-(x**2+y**2),[x,y]))
    
    while len(h) > k:
        heapq.heappop(h)
    
    return [i[1] for i in h]