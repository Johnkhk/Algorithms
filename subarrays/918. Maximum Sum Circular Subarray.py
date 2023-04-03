"""
idea is to use kadane and special and take the max of the both
special is a wrap around. and we get its max
We make a array called right_max which stores the max subarr sum starting and including an index i
then while we do kadane, we can find special kadane too by getting the prefix + right_max[i+1] (prefix includes current i)
we do special = max(special, prefix + right_max[i+1])
we dont worry about maxing prefix because the special max thing takes care of that since right_max[i] >= right_max[i+1] so if we dont do anything it (left side of max), it means prefix was badly taken
"""

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        right_max = [0]*n
        right_max[n - 1] = nums[n - 1];
        
        suffix_sum = nums[n-1]
        
        
        for i in reversed(range(n-1)):
            suffix_sum+=nums[i]
            right_max[i] = max(right_max[i+1], suffix_sum)
        # print(right_max)
        
        # kadane
        cur = 0
        mx = float("-inf")
        pref = 0
        special = float("-inf")
        for i in range(n):
            if cur+nums[i]<nums[i]:
                cur = nums[i]
            else:
                cur += nums[i]
            #kadane
            mx = max(cur,mx)
            pref+=nums[i]
            if i+1<n:
                special = max(special, pref+right_max[i+1])
        print(right_max)
        return max(mx,special)
    
            
        
