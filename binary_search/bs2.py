# tmp = [0,18,20]
# l,r = 0, len(tmp)
# target = 18
# while l<r:
#     mid = (l+r)//2
#     if target<=tmp[mid]:
#         r=mid
#     else:
#         l=mid+1
# if l == len(tmp):
#     print(-1)
# else:
#     print(tmp[l])

## REVERSE

tmp = [9,0]
l,r = 0, len(tmp)
target = 4
while l<r:
    mid = (l+r)//2
    if target>tmp[mid]:
        r=mid
    else:
        l=mid+1

if l-1<0:
    print(-1)
else:
    print(tmp[l-1])