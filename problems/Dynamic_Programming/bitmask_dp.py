def subsets(self, nums: List[int]) -> List[List[int]]:
    # WITH BITMASK
    
    res=[]
    N = len(nums)
    for bitmask in range(1<<N):
        cur=[]
        for j in range(N):
            if (1<<j)&bitmask:
                cur.append(nums[j])
        res.append(cur)
    return res