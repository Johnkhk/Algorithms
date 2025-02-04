import collections
import itertools
def ff(n):
    return n*(n-1)/2
def solution(numbers):
    # d = collections.defaultdict(list)
    # for num in numbers:
    #     cur = str(num)
    #     d[len(cur)].append(cur)
    
    # 151,241,351,121
    # 151: _51, 1_1, 15_
    # ans=0
    # for k,v in d.items():
    #     n = len(v)
    #     for i in range(n):
    #         for j in range(i+1,n):
    #             diff=0
    #             for c in range(k):
    #                 if v[i][c]!=v[j][c]:
    #                     diff+=1
    #                 if diff>1:
    #                     break
    #             if diff==1:
    #                 ans+=1
    # return ans
    d = collections.defaultdict(collections.Counter)
    for num in numbers:
        cur = list(str(num))
        tmp = cur.copy()
        for i in range(len(cur)):
            old = tmp[i]
            tmp[i]='_'
            tmp2 = "".join(tmp)
            d[tmp2][str(num)]+=1
            tmp[i] = old
    print(d)  
    ans=0
    for k,v in d.items():
        cur=0
        for c,d in v.items():
            ans-=ff(d)
            cur+=d
        ans+=ff(cur)
        # if n<2:
        #     continue
        # # ans+= (n-1)*n/2

        # prod=1
        # for c,d in v.items():
        #     prod*=d
        # ans+=prod
    return ans

def solution2(nums):
    ct,res=collections.Counter(),0
    for num in map(str,nums):   
        for i in range(len(num)):
            l = num[:i]+'*'+num[i+1:]
            r = ct[num]
            print(l,":",ct[l]," - ",num,":",r, "   sum = ",ct[l]-r)
            res += ct[l]-r
            ct[l]+=1
            # res+=ct[num[:i]+'*'+num[i+1:]]-ct[num]
            # ct[num[:i]+'*'+num[i+1:]]+=1
            
        ct[num]+=1
    # print(ct)
    return res
# nums1=[221,221,211,321]
nums1=[1,1,1,9,9,4,4] # 3*4 + 2*2
# nums1= [1, 9, 33, 402, 420, 502, 1] # [1,1,9,33,402,420,502]
"""
_ {
    1:2
    9:1
}
"""
n=7
# def ff(n):
#     return n*(n-1)/2
# print("AAA", n*(n-1)/2)
# print(ff(7)-ff(3)-ff(2)-ff(2))
# nums1=[1,1,1,9,9,4,4]+[221,221,211,321]


# nums1=[1,2,3,4]
# print("hey",set(itertools.combinations(nums1, 2)))
b = solution2(nums1)
c = solution(nums1)

print(b,c)
# a = solution([1,9,1,151,351])
# a = solution([1, 9, 33, 402, 420, 502, 1])
# print(a)