### Most basic form (Takes care of edge cases when it only has 1 number) ###
def binarySearch(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1


### If the element can still be in mid (previous elemnt to mid) ###
def binarySearch(matrix, target):
    l, r = 0, len(matrix) - 1

    while l < r:
        mid = (l + r) // 2
        if matrix[mid][-1] == target:
            return True
        elif matrix[mid][-1] < target:
            l = mid + 1
        else:
            r = mid
    return l


### Finding Pivot IDX in rotated sorted arr ###
# Actually there's only 2 cases: (find pivot (smallest element))
## USING RIGHT
# case1: [4,5,6,7,0*,1,2] mid>r: that means pivot>mid (search right: l=mid+1)
# case2: [7,0*,1,2,3,4,5] mid<=r: that means pivot<=mid, equals for when middle is 0
# Alternatively
## USING LEFT
# case1: [4,5,6,7,0*,1,2] l<=mid: that means pivot>mid (search right: l=mid+1)
# case1.5: if nums[l]<nums[r]:break (1,2,3,4,5)
# case2: [7,0*,1,2,3,4,5] l>mid: that means pivot>mid (search left: r=mid) equals for when middle is 0
def findPivot(nums):
    """
    using left
    """
    l, r = 0, len(nums) - 1
    while l < r:
        mid = (l + r) // 2
        if nums[l] <= nums[mid]:
            if nums[l] < nums[r]:
                break
            l = mid + 1  # case1
        elif nums[l] > nums[mid]:  # case2
            r = mid
    pivot = l
    return pivot


def findPivot(nums):
    """
    using right
    """
    l, r = 0, len(nums) - 1
    while l < r:
        mid = (l + r) // 2
        if nums[r] < nums[mid]:
            l = mid + 1  # case1
        elif nums[r] >= nums[mid]:  # case2
            r = mid
    pivot = l
    return pivot


### peak in mountain ###
def findPeak(arr):
    lo = 0
    hi = len(arr) - 1

    while lo < hi:
        # mid = lo + (hi-lo +1)/2
        mid = (lo + hi) / 2
        if arr[mid] < arr[mid + 1]:
            lo = mid + 1
        else:
            hi = mid
    return lo


### get first smaller or equal elem ###
def getLeq(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] <= target:  # if nums[mid]<target: (FIRST ELEM STRICTLY SMALLER)
            l = mid + 1
        else:
            r = mid - 1
    # not found
    if r == -1:
        return -1
    return r


# nums=[1,3,5,11]
# print(getLeq(nums,1.1))
# nums=[1,3,5,8,8,8,8,8,8,8,8,8,8,8,11]
# print(getLeq(nums,8))
# return nums[r]
# nums=[1,3,5,11]
# print(getLeq(nums,1.1))


### get first bigger or equal to elem ###
def getGeq(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        # GEQ
        if nums[mid] < target:  # if nums[mid]<=target: (FIRST ELEM STRICTLY GREATER)
            l = mid + 1
        else:
            r = mid - 1
    # not found
    if l == len(nums):
        return -1
    return l


# nums=[1,3,5,11]
# print(getGeq(nums,5))
# nums=[1,3,5,8,8,8,8,8,8,8,8,8,8,8,11]
# print(getGeq(nums,8))

# nums=[1,3,5,11]
# print(getGeq(nums,5))
# TODO:
"""
https://leetcode.com/problems/find-in-mountain-array/
https://leetcode.com/problems/longest-mountain-in-array/
"""


def find_first_pos(arr, target):
    left = 0
    right = len(arr) - 1

    first_position = -1  # keep track of the latest valid mid position
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            first_position = mid
            right = mid - 1  # continue searching to the left
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return first_position


##### More advanced notes #####
"""
if we are not returning something in the array, usually we do while l<r:
    watch below for explanation
    https://www.youtube.com/watch?v=4lK5pdSXhCk&t=802s&ab_channel=CrackingFAANG
"""

"""
Binary search with bisect
idea is if we insert a 7, which index should it be inserted at?
can return lo or hi
"""
################################# Binary Search Template #################################
"""
Minimize k , s.t. condition(k) is True (from the right)
# first 1 to evaluate ths true from right 

def binary_search(array) -> int:
    def condition(value) -> bool:
        pass

    left, right = min(search_space), max(search_space) # could be [0, n], [1, n] etc. Depends on problem
    while left < right:
        mid = left + (right - left) // 2
        if condition(mid): # # keep evaluating this condition true until the first
            right = mid
        else:
            left = mid + 1
    return left

we only need to modify three parts after copy-pasting this template, and never need to worry about corner cases and bugs in code any more:

Correctly initialize the boundary variables left and right to specify search space. Only one rule: set up the boundary to include all possible elements;
Decide return value. Is it return left or return left - 1? Remember this: after exiting the while loop, left is the minimal k​ satisfying the condition function;
Design the condition function. This is the most difficult and most beautiful part. Needs lots of practice.
"""
############################ E.G using template ############################

### sqrt(x) ###
"""
goal: return integer sqrt x
algo: 
        use template, condition is first number stuch that the sqrt is strictly greater, then we return that -1. 
        We need to increase r by 1 for edge cases. 
"""


def sqrt(x):
    l, r = 0, x + 1
    while l < r:
        m = (l + r) // 2

        if m * m > x:
            r = m
        else:
            l = m + 1
    return l - 1


### 34.Find First and Last Position of Element in Sorted Array ###


def searchRange(nums, target):
    l, r = 0, len(nums) - 1
    while l < r:
        mid = (l + r) // 2
        if nums[mid] >= target:  # minimize this condition while true
            r = mid
        else:
            l = mid + 1
    start = l

    l, r = 0, len(nums) - 1
    while l < r:
        mid = (l + r) // 2
        if nums[mid] > target:  # minimize this condition while true
            r = mid
        else:
            l = mid + 1
    end = l - 1

    if start == -1:
        return [-1, -1]

    return [start, end]


### 852. Peak Index in a Mountain Array ### (Holy Crap this method is good)
def peakIndexInMountainArray(arr):
    l, r = 0, len(arr) - 1
    while l < r:
        mid = (l + r) // 2
        if (
            mid + 1 < len(arr) and arr[mid] > arr[mid + 1]
        ):  # first condition for this to be true
            r = mid
        else:
            l = mid + 1
    return l


### 162. Find Peak Element ### (Use method again, but this one is WEIRD, why is this the condition)
def findPeakElement(nums):
    l, r = 0, len(nums) - 1
    while l < r:
        mid = (l + r) // 2
        if nums[mid] > nums[mid + 1]:
            r = mid
        else:
            l = mid + 1
    return l


### 1095. Find in Mountain Array ### (EZ, apply same template, wow 1 try)
def findInMountainArray(target, mountain_arr):
    l, r = 0, mountain_arr.length() - 1
    while l < r:
        mid = (l + r) // 2
        if mid + 1 < mountain_arr.length() and mountain_arr.get(mid) > mountain_arr.get(
            mid + 1
        ):
            r = mid
        else:
            l = mid + 1
    peak = l

    print(peak)

    l, r = 0, peak
    while l < r:
        mid = (l + r) // 2
        if mountain_arr.get(mid) >= target:
            r = mid
        else:
            l = mid + 1
    leftans = l
    l, r = peak + 1, mountain_arr.length() - 1
    while l < r:
        mid = (l + r) // 2
        if mountain_arr.get(mid) <= target:
            r = mid
        else:
            l = mid + 1
    rightans = l
    if mountain_arr.get(leftans) == target:
        return leftans
    if mountain_arr.get(rightans) == target:
        return rightans
    return -1


### 1231. Divide Chocolate ### (template still works)
def maximizeSweetness(sweetness, k):
    """
    Idea & algo:
    using the same binary search template...
    1. min and max are min(sweetness), max(sweetness)+1 (+1 for edge case)
    2. condition:
        -   If we have more chunks than amount of people,
            we should increase our limit.
        -   If we less chunks than amount of people,
            then we should decrease our limit. (chunks<people)
    3. return l or r
    """

    def cond(limit):
        cursweet = 0
        chunks = 0
        for j in sweetness:
            cursweet += j
            if cursweet >= limit:
                cursweet = 0
                chunks += 1
        # higher sweetness to lower sweetness, this is true, we find the first
        return chunks < num_people

    l, r = min(sweetness), sum(sweetness) + 1
    num_people = k + 1
    while l < r:
        mid = l + (r - l) // 2
        if cond(mid):
            r = mid
        else:
            l = mid + 1
    return l - 1


# b=[1,2,3,4,5,6]
# # c = bisect.bisect_left(b,3) # 2
# c = bisect.bisect_right(b,3) # 3
# print("C",c)
