# 1588. Sum of All Odd Length Subarrays
"""
The contribution of arr idx=i
is in (i+1)(n-i) sub arrays
e.g [1,2,3,4,5]
3 is in 3*3 sub arrays
"""


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ans = 0
        n=len(arr)
        for i in range(n):
            k = (i+1)*(n-i)
            ans += (k+1)//2*arr[i]
        return ans