### Get prefix sum quick for nums ###
nums=[1,2,3,4,5,6,7]
prefix=[0]
for i in range(len(nums)):
    prefix.append(prefix[-1]+nums[i])
# print(prefix)

### get +1 quick given range(start and end) ###
nums = [1,2,3,4,5,6,7,8,9]
# add 1 for range [0,2], add 1 for range [5,7] 
# # (inclusive)-> expect [2,3,4,4,5,7,8,9,9], (noninclusive)-> expect [2,3,3,4,5,7,8,8,9]
ranges=[[0,2],[5,7]]

# create adder
tmp = [0]*(len(nums)+1)
for start, end in ranges:
    tmp[start]+=1
    # tmp[end+1]-=1 # inclusive
    tmp[end]-=1 # noninclusive
cur=0
res=[]
for i in range(len(nums)):
    cur+=tmp[i]
    res.append(cur+nums[i])
print(res)
    



