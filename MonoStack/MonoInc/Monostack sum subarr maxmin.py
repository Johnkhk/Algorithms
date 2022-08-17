### 2104. Sum of Subarray Ranges ###

# idea: 
# sum{ Max(subarray) - Min(subarray) } over all possible subarray == sum{Max(subarray)} - sum{Min(subarray)} over all possible subarray

# use a monoinc stack for calculating sum(MinSubarr).
# use a monodec stack for calculating sum(MaxSubarr).

# For Max:
# we know for a value
# [1,2,3,4] 2, if 2 is to be put into stack:
# we look at 4 and we can see that it is at index 3
# the amount of subarrays at which 4 is the minimum will be:
# x amount to its left (where x+1 will be smaller), 
# and y amount to its right, (where y+1 will be smaller)
# i.e we look for previous less element PLE and next less element NLE 
# we see 4 will give us (3-2)*(4-3) subarrays where 4 is at idx 3
#
# For Min:
# [4,3,2,1] 2, if 2 is to be put into stack:
# We pop 1 and see left and right
# For left, the Previous Greater Element (PGE) is 1 index away, the NGE is also 1 index away
# So we know, 1 is the min for only itself, we multiply 1* the value of 1

### Solution1: 2 loop solution ###
nums = [1,4,2,1,9,2,4]
stack=[]
sum_min=0
## GET SUM(ALL MIN SUBARRAYS) ##
# DO IN 2 LOOPS
for i,n in enumerate(nums):
    while stack and stack[-1][1] > n:
        popi,popn = stack.pop()
        prevstackidx = stack[-1][0] if stack else -1
        sum_min+= (i-popi)*(popi-prevstackidx)*popn
    stack.append((i,n))

# this second loop takes care of items still in stack
i=len(nums)
while stack:
    popi,popn = stack.pop()
    prevstackidx = stack[-1][0] if stack else -1
    sum_min+= (i-popi)*(popi-prevstackidx)*popn

### GET SUM(ALL MAX SUBARRAYS) ###
stack=[]
sum_max=0
# DO IN 2 LOOPS
for i,n in enumerate(nums):
    while stack and stack[-1][1] < n:
        popi,popn = stack.pop()
        prevstackidx = stack[-1][0] if stack else -1
        sum_max+= (i-popi)*(popi-prevstackidx)*popn
    stack.append((i,n))
i=len(nums)
while stack:
    popi,popn = stack.pop()
    prevstackidx = stack[-1][0] if stack else -1
    sum_max+= (i-popi)*(popi-prevstackidx)*popn
print(sum_max-sum_min)
### Solution2: 1 loop solution ###
# we add 1 more iteration to take care of items still in stack
#calculate min (monoincreasing)
stack=[]
sum_min=0
for i in range(len(nums)+1):
    while stack and (i==len(nums) or nums[stack[-1]] > nums[i]):
        popi = stack.pop()
        prevstack = stack[-1] if stack else -1
        sum_min+= (i-popi)*(popi-prevstack)*nums[popi]
    stack.append(i)
#calcluate max (monodecreasing)
stack=[]
sum_max=0
for i in range(len(nums)+1):
    while stack and (i==len(nums) or nums[stack[-1]] < nums[i]):
        popi = stack.pop()
        prevstack = stack[-1] if stack else -1
        sum_max+= (i-popi)*(popi-prevstack)*nums[popi]
    stack.append(i)
print(sum_max-sum_min)
### Solution3: Use a function to be clean withit ###

def fn(op): 
    """Return min sum (if given gt) or max sum (if given lt)."""
    ans = 0 
    stack = []
    for i in range(len(nums) + 1): 
        while stack and (i == len(nums) or op(nums[stack[-1]], nums[i])): 
            mid = stack.pop()
            ii = stack[-1] if stack else -1 
            ans += nums[mid] * (i - mid) * (mid - ii)
        stack.append(i)
    return ans 
def lt(a,b):
    return a<b
def gt(a,b):
    return a>b
print(fn(lt) - fn(gt))

