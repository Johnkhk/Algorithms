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
        print(nums[mid])
        # if nums[r]<nums[mid]:
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
        # if nums[l]<nums[mid] and nums[r<nums[mid]:
        if nums[r]<nums[mid]:
            l=mid+1 # case1
        # elif nums[l]>nums[mid] and nums[r]>nums[mid]: # case2
        elif nums[r]>=nums[mid]: # case2
            r=mid
    pivot=l
    return pivot