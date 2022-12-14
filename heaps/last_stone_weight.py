#1046. Last Stone Weight
def lastStoneWeight(self, stones: List[int]) -> int:
    h = [-i for i in stones]
    heapq.heapify(h)
    
    while len(h)>1:
        y = heapq.heappop(h)
        x = heapq.heappop(h)
        
        if x==y:
            continue
        else:
            heapq.heappush(h,-((-y)-(-x)))
    if not h:
        return 0
    return -h[0]