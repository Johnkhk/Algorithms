# a=[36,9,13,27,43,25,44,48,12,40,37,20,26,36,1,20,19,14,28,38,39,42,21,30,29,29,44,14,33,31,48,11,43,6,19,33,43,41,40,22,6,49,16,44,20,15,13,10,2,3,16,31,40,50,5,30,27,41,37,13,46,45,25,32,26,16,10,42,45,1,49,50,7,50,28,15,12,45,34,30,4,36,16,8,30,9,30,43,34,36,39,21,49,29,40,47,33,28,36,29]
# # a = [1,2,3]
# n = len(a)
# for i in range(n):
#     for j in range(i,n):
#         subarr = a[i:j+1]
#         # print(subarr)
#         tmp = sum(subarr)*min(subarr)
#         if tmp == 10374:
#             print("aa",i,j)
#             print(subarr, sum(subarr))



class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        # min in how many subarrays
            # for this we can use a mono inc stack
        # then while we pop we can add if increasing we make it yeyeye
        n = len(nums)
        
        pref = [0]
        tmp = 0
        for i in range(n):
            tmp+=nums[i]
            pref.append(tmp)
        
        
        stack = []
        ans = float("-inf")
        for i in range(n+1):
            ple = -1
            # ple = i-1
            mx = float("-inf")
            while stack and (i==n or nums[stack[-1]] >= nums[i]):
                idx = stack.pop()
                ple = -1
                
                if stack:
                    ple = stack[-1]
                cursum = pref[i] - pref[ple+1]
                ans = max(ans, cursum*nums[idx])
                
            stack.append(i)
            # print(stack)
        mod = (10**9) + 7
        return ans % mod
        
















