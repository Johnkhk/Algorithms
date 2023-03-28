class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        summ = 0 
        n = len(nums)
        mp={0:-1}
        for i in range(n):
            summ += nums[i]
            if k!=0:
                summ%=k
            if summ in mp and mp[summ]:
                
            