# Input: nums = [2,4,0,9,6]
# Output: [9,6,6,-1,-1]
"""
As a quick refresher, that algorithm goes right-to-left maintaining a mono-stack, 
and binary-searches the monostack to find the next greater element.

1st pass get the nums[i] is nge of [elem1, elem2]
e.g: [2,4,0,9,6]
     [[],[2],[],[0,4],[]] ->indices-> [[],[0],[],[0,1],[]]

     u have a monodec of the indexes of nums
"""
import bisect
def myfind(ms,j,nums):
    # tmp = [nums[ms[a]] for a in reversed(range(len(ms)))]
    # a = bisect.bisect_right(tmp, nums[j])
    # if a==len(tmp):
    #     return -1
    # return ms[a]

    # tmp = ms[::-1]
    # a = bisect.bisect_right(tmp, nums[j])
    # print("a",a)
    # return a

    # tmp = ms[::-1]
    # l,r = 0, len(tmp)-1
    # while l<=r:
    #     mid = (l+r)//2
    #     # GEQ
    #     # if nums[mid]<target: # if nums[mid]<=target: (FIRST ELEM STRICTLY GREATER)
    #     if nums[ms[mid]]>=nums[j]: # if nums[mid]<=target: (FIRST ELEM STRICTLY GREATER)
    #         l=mid+1
    #     else:
    #         r=mid-1
    # # not found
    # if l==len(nums):
    #     return -1
    # if not ms:
    #     return -1
    # return ms[l-1]

    tmp = ms[::-1]
    l,r = 0, len(tmp)-1
    target = nums[j]
    while l<r:
        mid = (l+r)//2
        if target<nums[tmp[mid]]:
            r=mid
        else:
            l=mid+1
    if not ms:
        return -1
    if l==len(tmp):
        return -1
    return ms[l-1]


    # l,r = 0,len(ms)-1
    # while l<r:
    #     mid = (l+r)//2
    #     if nums[j]>nums[ms[mid]]:
    #         r=mid
    #     else:
    #         l=mid+1
    # print("l",l, len(ms))
    # if l == len(ms):
    #     return -1
    # return ms[l]


    # for i in reversed(range(len(ms))):
    #     if nums[j]<nums[ms[i]]:
    #         return ms[i]
    # return -1
def secondGreaterElement(nums):

    def ge(nums, prev):
        n = len(nums)
        ms = []
        pprev = [[] for _ in range(n)]
        for i in range(n-1,-1,-1):
            # if not prev:
            #     print("HERE1")
            #     for j in [i]:
            #         print("j",j)
            #         tmp = [nums[a] for a in ms][::-1]
            #         # a = bisect.bisect_right(tmp, nums[j])
            #         a = myfind(ms,j,nums)
            #         # if a != len(ms):
            #         if a != -1:
            #             print("it",a)
            #             pprev[a].append(j)
            # else:
            #     print("HERE2")
            #     for j in prev[i]:
            #         # a = bisect.bisect_right(ms, j)
            #         a = myfind(ms,j,nums)
            #         if a != len(ms):
            #             pprev[a].append(j)

                    
            cont = prev[i] if prev else [i]
            for j in cont:
                a = myfind(ms,j,nums)
                if a != -1:
                    pprev[a].append(j)

            while ms and nums[ms[-1]]<nums[i]:
                ms.pop()
            ms.append(i)
            # print(ms)
        return pprev
    k=2
    n=len(nums)
    res = [-1]*n
    prev = []
    while k>0:
        prev = ge(nums, prev)
        # print("prev", prev)
        # break
        k-=1
    for i in range(n-1,-1,-1):
        for j in prev[i]:
            res[j] = nums[i]
    return res

           
            

a = secondGreaterElement([2,4,0,9,6])
print(a)

# b=[1,2,3,4,5,6]
# # c = bisect.bisect_left(b,3) # 2
# c = bisect.bisect_right(b,3) # 3
# print("C",c)

        
#nge3
