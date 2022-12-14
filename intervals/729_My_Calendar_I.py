# using line sweep
# O(NlogN), O(N)
class MyCalendar:
    
    def __init__(self):
        self.change=defaultdict(int)
        

    def book(self, start: int, end: int) -> bool:
        self.change[start]+=1
        self.change[end]-=1
        cur=0
        for key in sorted(self.change.keys()):
            cur +=self.change[key]
            if cur>1:
                self.change[start]-=1
                self.change[end]+=1
                return False
        return True


from sortedcontainers import SortedList
class MyCalendar:

    def __init__(self):
        # a=[[1,2],[3,4],[7,8],[9,10],[11,12]]
        a=[]
        # a=[[0,0],[float("inf"),float("inf")]]
        
        self.bookings=SortedList(a)

    def book(self, start: int, end: int) -> bool:
        if not self.bookings:
            self.bookings.add([start,end])
            return True
        # start,end = 5,6
        bs=self.bookings
        # print(bs)
        l,r = 0,len(bs)
        while l < r:
            mid = (r+l)//2
            if bs[mid][0]>start:
                r = mid
            else:
                l = mid + 1
        last_idx = l
        # if last_idx==0:
            # last_idx = 1
        idx = last_idx
        self.calendar = bs
        # idx = bs.bisect_right([start, end])
        # print(bs)
        # print("inserting",start,end)
        # print(last_idx,idx)
        
        if (idx > 0 and self.calendar[idx-1][1] > start) or (idx < len(self.calendar) and self.calendar[idx][0] < end):
            return False
        self.calendar.add([start, end])
        return True
        
        # if last_idx==0:
        #     if start>=bs[last_idx][1]:
        #         self.bookings.add([start,end])
        #         return True
        #     if end <= bs[last_idx][0]:
        #         self.bookings.add([start,end])
        #         return True
        #     return False
        # elif last_idx==len(bs)-1:
        #     if bs[last_idx][0] >=end and bs[last_idx-1][1]<=start:
        #         self.bookings.add([start,end])
        #         return True
        #     if bs[last_idx][1]<=start: 
        #         self.bookings.add([start,end])
        #         return True
        #     return False
                
        if bs[last_idx-1][1]>start:
            return False
        self.bookings.add([start,end])
        return True
