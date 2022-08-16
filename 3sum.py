nums.sort()
res=[]
for i in range(len(nums)):
    l,r=i+1,len(nums)-1
    if i>0 and nums[i]==nums[i-1]:
        continue
    while l<r:
        sam = nums[i]+nums[l]+nums[r]
        if sam==0:
            res.append([nums[i],nums[l],nums[r]])
            l+=1
            r-=1
            while l<r and nums[l]==nums[l-1]:
                l+=1
        elif sam<0:
            l+=1
        else:
            r-=1
        
return res