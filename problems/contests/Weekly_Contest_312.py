
# P3
class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        
        # [2, 1, 1, 1, 3, 4, 1]
        # [1, 2, 3, 4, 1, 1, 2] # Noninc aka either same or decreasing STORES streaks including self
        # [1, 5, 4, 3, 2, 1, 1] # Nondec aka either same or increasing
        #.       *. *. *. *
        #        
        N=len(nums)
        def calc(nums):
            
            res=[1]*N
            streak=1
            for i in range(1,N):
                if nums[i]<=nums[i-1]: # nonincreasing aka same or decreasing
                    streak+=1
                else:
                    streak=1
                res[i]=streak
            return res
        noninc = calc(nums)
        nondec = calc(nums[::-1])[::-1]
        
        """
        so we have the streaks for nondec and noninc in the array
        Now, given index i
        ---(nondec)--- i ---(noninc)---
        we need k guys on the left and kguys on the right that are nondec and noninc
        
        For Nondec we need nondec[i] - nondec[i-k] == k
        
        """
        # print(noninc,nondec)
        res=[]
        for i in range(k,N-k):
            if noninc[i-1]>=k and nondec[i+1]>=k:
                res.append(i)
        return res