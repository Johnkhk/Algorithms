### q1
def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
    
    def gett(time):
        h,m=time.split(':')
        h=int(h)
        m=int(m)
        return h*60 + m
        
    s1 = gett(event1[0])
    e1 = gett(event1[1])        
    s2 = gett(event2[0])
    e2 = gett(event2[1])   
    
    change=defaultdict(int)

    change[s1]+=1
    change[e1+1]-=1
    change[s2]+=1
    change[e2+1]-=1
    
    
    # print(change)
    cur=0
    mx = 0
    for key in sorted(change.keys()):
        cur +=change[key]
        if cur==2:
            return True
        mx = max(mx, cur)
    return False
### q2
# greatest common factor
# O(log(min(a, b))
def gcd(a, b):
    while b: 
        a, b = b, a % b
    return a
# gcd
def subarrayGCD(self, nums: List[int], k: int) -> int:
    def hcf(a, b):
        if(b == 0):
            return a
        else:
            return hcf(b, a % b)
    n = len(nums)
    count=0
    for i in range(n):
        num = nums[i]
        if nums[i]==k:
            count+=1
        for j in range(i+1,n):
            num = hcf(num,nums[j])
            if num==k:
                count+=1
    return count
    
### Q3
class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        
        def getcost(target):
            res=0
            for i in range(len(nums)):
                res+=abs(target-nums[i])*cost[i]
            return res
        
        n = len(nums)
        l,r=1,10**6
        
        while l<r:
            mid = (l+r)//2
            a = getcost(mid-1)
            b = getcost(mid)
            ans = min(a,b)
            if mid-1>=1 and  a< b:
                r=mid
            else:
                l=mid+1
                
        return ans
        
