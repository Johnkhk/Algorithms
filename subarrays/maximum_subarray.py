from typing import *
nums = [-2,1,-3,4,-1,2,1,-5,4]

def maxSubArray(self, nums: List[int]) -> int:
    n = len(nums)
    cursum = nums[0]

    if len(nums) == 1:
        return nums[0]
    maxsum = float("-inf")
    maxsum = max(maxsum, cursum)

    for i in range(1,n):

        if nums[i] > cursum + nums[i]:
            cursum = nums[i]
        else:
            cursum += nums[i]
        maxsum = max(maxsum, cursum)
    return maxsum

# returning subarray
def maxsubarr(nums):
    n = len(nums)
    cursum = nums[0]

    if len(nums) == 1:
        return nums[0]
    maxsum = float("-inf")
    maxsum = max(maxsum, cursum)
    
    for i in range(1,n):

        if nums[i] > cursum + nums[i]:
            cursum = nums[i]
            startindex=i
        else:
            cursum += nums[i]
        if cursum>maxsum:
            maxsum = cursum
            endindex=i
    return nums[startindex:endindex+1]
a = maxsubarr([-2,1,-3,4,-1,2,1,-5,4])
print(a)