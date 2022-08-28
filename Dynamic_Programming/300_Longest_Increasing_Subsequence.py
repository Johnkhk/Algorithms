# Top down memo

def lengthOfLIS(nums):
    def dfs(i):
        if i in memo:
            return memo[i]
        res=0
        for j in range(i+1,len(nums)):
            if nums[j]>nums[i]:
                res = max(res,1+dfs(j))
        memo[i]=res
        return res
    memo={}
    res =float("-inf")
    for i in range(len(nums)):
        res = max(res,1+dfs(i))
    return res

# Bottom up
# O(N^2)
def lengthOfLIS(nums):
    dp = [1]*len(nums)
    ret = 1
    for i in range(1,len(nums)):
        for j in range(i):
            if nums[j]<nums[i]:
                dp[i] = max(dp[i],dp[j]+1)
                ret = max(ret, dp[i])
    return ret

# weird solution that leads to binary search
def lengthOfLIS(nums):
    sub = [nums[0]]
    for i in range(1,len(nums)):
        if nums[i]>sub[-1]:
            sub.append(nums[i])
        else:
            for j in range(len(sub)):
                if sub[j]>=nums[i]:
                    sub[j]=nums[i]
                    break
    return len(sub)
    
### binary search ###
def lengthOfLIS(nums):
    sub = [nums[0]]
    for i in range(1,len(nums)):
        if nums[i]>sub[-1]:
            sub.append(nums[i])
        else:
            l,r=0,len(sub)-1
            while l<r:
                mid = l+(r-l)//2
                if sub[mid]>=nums[i]:
                    r=mid
                else:
                    l=mid+1
            sub[l]=nums[i]
            # for j in range(len(sub)):
            #     if sub[j]>=nums[i]:
            #         sub[j]=nums[i]
            #         break
    return len(sub)


        