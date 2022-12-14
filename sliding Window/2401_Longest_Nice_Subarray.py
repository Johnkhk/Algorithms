def longestNiceSubarray(self, nums: List[int]) -> int:
        
    l=0
    cur=0
    res=0
    N=len(nums)
    for r in range(N):
        while (cur & nums[r]) != 0:
            cur ^= nums[l]
            l+=1
            
        cur|= nums[r]         
        res = max(res,r-l+1)
    return res
    