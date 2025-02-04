"""
Reading the leetcode official monostack solution helps alot
Key idea:
we use the contribution of each element.
For each element, we find the PLE and NLE, then the number of subarrs where elem is smallest is (idx-PLE)*(NLE-idx)

if there is still elems in the stack, we enforce i=n and pop the rest

edge case:
we need to use >= for duped elements to not overlap ranges
"""

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        # [3,1,2,4]
        # idx i has (i+1)(n-i) subarrays
        # e.g idx 0 is in (0+1)(n-0) subarrays
        # e.g idx 1 is in (1+1)*(n-1) = 8 subarrays
        MOD = 10 ** 9 + 7
        stack = []
        n = len(arr)
        
        ans = 0
        for i in range(n):
            while stack and (arr[stack[-1]]>=arr[i]):
                idx = stack.pop()
                prevsmall_idx = -1
                if stack:
                    prevsmall_idx = stack[-1]
                nextsmall_idx = i
                ans += arr[idx] * (idx-(prevsmall_idx)) * (nextsmall_idx-idx)
            stack.append(i)
        
        i=n
        while stack:
            idx = stack.pop()
            prevsmall_idx = -1
            if stack:
                prevsmall_idx = stack[-1]
            nextsmall_idx = i
            ans += arr[idx] * (idx-(prevsmall_idx)) * (nextsmall_idx-idx)
            
            
        return ans % MOD
                
                