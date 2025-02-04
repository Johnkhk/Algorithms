class MedianFinder:

    def __init__(self):
        self.minh=[] # holds bigger + 1. we return self.minh[0] if odd
        self.maxh=[] # holds smaller 
        # max[2,1], min[3,4]
    def addNum(self, num: int) -> None:
       
        # add to the minheap
        heapq.heappush(self.minh,num)
        # pop from the minheap (gets the smallest) and add to max heap
        heapq.heappush(self.maxh,-heapq.heappop(self.minh))

        if len(self.minh) < len(self.maxh): # this makes sure maxheap is never 1 more than minheap. if they are equal this is skipped
            # rather, maxheap 
            heapq.heappush(self.minh,-heapq.heappop(self.maxh))
        
    def findMedian(self) -> float:
        if len(self.minh)==len(self.maxh):
            return (self.minh[0]+-self.maxh[0])/2
        elif len(self.minh)>len(self.maxh):
            return self.minh[0]
        