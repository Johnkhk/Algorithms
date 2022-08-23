### Most basic form (Takes care of edge cases when it only has 1 number) ###
def binarySearch(nums,target):
    l,r = 0,len(nums)-1
    while l<=r:
        mid = (l+r)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            l=mid+1
        else:
            r=mid-1
    return -1

### If the element can still be in mid (previous elemnt to mid) ###
def binarySearch(matrix,target):
    l,r = 0,len(matrix)-1
            
    while l<r:
        mid = (l+r)//2
        if matrix[mid][-1]==target:
            return True
        elif matrix[mid][-1]<target:
            l=mid+1
        else:
            r=mid
    return l
### Finding Pivot IDX in rotated sorted arr ###
# Actually there's only 2 cases: (find pivot (smallest element))
## USING RIGHT
# case1: [4,5,6,7,0*,1,2] mid>r: that means pivot>mid (search right: l=mid+1)
# case2: [7,0*,1,2,3,4,5] mid<=r: that means pivot<=mid, equals for when middle is 0
#Alternatively
## USING LEFT
# case1: [4,5,6,7,0*,1,2] l<=mid: that means pivot>mid (search right: l=mid+1)
# case1.5: if nums[l]<nums[r]:break (1,2,3,4,5)
# case2: [7,0*,1,2,3,4,5] l>mid: that means pivot>mid (search left: r=mid) equals for when middle is 0
def findPivot(nums):
    """
    using left
    """
    l,r = 0, len(nums)-1
    while l<r:
        mid = (l+r)//2
        if nums[l]<=nums[mid]:
            if nums[l]<nums[r]:
                break
            l=mid+1 # case1
        elif nums[l]>nums[mid]: # case2
            r=mid
    pivot=l
    return pivot
def findPivot(nums):
    """
    using right
    """
    l,r = 0, len(nums)-1
    while l<r:
        mid = (l+r)//2
        if nums[r]<nums[mid]:
            l=mid+1 # case1
        elif nums[r]>=nums[mid]: # case2
            r=mid
    pivot=l
    return pivot

### peak in mountain ###
def findPeak(arr):
    lo = 0
    hi = len(arr)-1

    while(lo<hi):
        # mid = lo + (hi-lo +1)/2
        mid = (lo + hi)/2
        if(arr[mid]<arr[mid+1]):
            lo=mid+1
        else:
            hi=mid
    return lo

### get first smaller or equal elem ###
def getLeq(nums,target):
    l,r = 0, len(nums)-1
    while l<=r:
        mid = (l+r)//2
        if nums[mid]<=target: # if nums[mid]<target: (FIRST ELEM STRICTLY SMALLER)
            l=mid+1
        else:
            r=mid-1
    # not found
    if r==-1:
        return -1
    return nums[r]
nums=[1,3,5,11]
print(getLeq(nums,1.1))

def getGeq(nums,target):
    l,r = 0, len(nums)-1
    while l<=r:
        mid = (l+r)//2
        # GEQ
        if nums[mid]<target: # if nums[mid]<=target: (FIRST ELEM STRICTLY GREATER)
            l=mid+1
        else:
            r=mid-1
    # not found
    if l==len(nums):
        return -1
    return nums[l]
# nums=[1,3,5,11]
# print(getGeq(nums,5))
# TODO:
"""
https://leetcode.com/problems/find-in-mountain-array/
https://leetcode.com/problems/longest-mountain-in-array/
"""


##### More advanced notes #####
"""
if we are not returning something in the array, usually we do while l<r:
    watch below for explanation
    https://www.youtube.com/watch?v=3JU0v2kuYGg&ab_channel=CrackingFAANG

To, fit a condition, use while l<r:
222. Count Complete Tree Nodes
while l<=r:
    # mid = (l+r)//2
    mid = l+(r-l)//2

    if exists(root,d,mid):
        l=mid+1
    else:
        r=mid-1
return l
First Bad Version
while l<=r:
    mid = (l+r)//2
    if not isBadVersion(mid):
        l=mid+1
    else:
        r=mid-1
return l
"""