"""
make a prev and next which store prev smaller and next smaller
then for each just check
"""

class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        stack = []
        n = len(nums)
        nextS = [-1]*n
        prevS = [-1]*n
        for i in range(n):
            while stack and nums[stack[-1]] > nums[i]:
                idx = stack.pop()
                nextS[idx] = i
            stack.append(i)
        
        stack.clear()
        for i in reversed(range(n)):
            while stack and nums[stack[-1]] > nums[i]:
                idx = stack.pop()
                prevS[idx] = i
            stack.append(i)
        # print(nextS,prevS)
        
        for i in range(n):
            l, r = prevS[i], nextS[i]
            if r == -1:
                r = n
            # if l == -1:
                # l = -1
            length = r-l-1
            if (threshold/length) < nums[i]:
                return length
            
        return -1
            