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
    


######## 1712 ways to split 3 array ##########
### binary search and prefixsum

def waysToSplit(self, nums: List[int]) -> int:
    
    N = len(nums)
    
    prefix=[0]
    for i in range(N):
        prefix.append(prefix[-1]+nums[i])
    total=prefix[N]
    ans=0
    for i in range(1,N-1):
        lsum = prefix[i]
        
        l,r=i+1,N+1
        while l<r:
            mid = (l+r)//2
            # msum = prefix[mid] - lsum
            # if msum>=lsum:
            if prefix[mid]>=lsum*2:
                r=mid
            else:
                l=mid+1
        L = l
        l,r=i+1,N+1
        while l<r:
            mid = (l+r)//2
            # msum = prefix[mid] - prefix[i]
            # rsum = total - prefix[mid]
            # if not (rsum>=msum):
            if not (total-prefix[mid]>=prefix[mid]-lsum):
            
                r=mid
            else:
                l=mid+1
        R=l
        
        # print(L,R)
        # ans+= max(0,(R-L)-1)
        # ans+= (R-L-1)
        
        # ans += max(0, min(len(nums), R) - max(i+1, L))
        if L<i+1:
            L=i+1
        if R>=len(nums):
            R=len(nums)
        if L>R:
            continue
        ans+=R-L

        
    return ans%((10**9)+7)


############################ prefix_sum of matrix ############################
mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]]
"""
prefix[i][j] = sum(matrix[0...i][0...j]) not including i and j
"""
m,n=len(mat),len(mat[0])
prefixSum = [[0]*(n+1) for i in range(m+1)]
for i in range(1,m+1):
    for j in range(1,n+1):
        prefixSum[i][j] = prefixSum[i-1][j] + prefixSum[i][j-1] - prefixSum[i-1][j-1] + mat[i-1][j-1]
print(prefixSum)

### Sum any region ###
def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
    row1+=1
    col1+=1
    row2+=1
    col2+=1
    sm=0
    whole = self.prefixSum[row2][col2]
    left = self.prefixSum[row2][col1-1]
    top = self.prefixSum[row1-1][col2]
    topleft = self.prefixSum[row1-1][col1-1]
    return whole - left - top + topleft

### ###
def maxSideLength(mat, threshold):
        
    m,n=len(mat),len(mat[0])
    prefixSum = [[0]*(n+1) for i in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            prefixSum[i][j] = prefixSum[i-1][j] + prefixSum[i][j-1] - prefixSum[i-1][j-1] + mat[i-1][j-1]
    
    def sumRegion(row1: int, col1: int, row2: int, col2: int) -> int:
        if row2>=len(prefixSum) or col2>=len(prefixSum[0]):
            return float("inf")
        whole = prefixSum[row2][col2]
        left = prefixSum[row2][col1-1]
        top = prefixSum[row1-1][col2]
        topleft = prefixSum[row1-1][col1-1]
        return whole - left - top + topleft
    
    # i=2
    # j=1
    # sqr_len=1
    # print(sumRegion(i,j,i+sqr_len,j+sqr_len))
    
    mx = 0
    for i in range(1,len(mat)+1):
        for j in range(1,len(mat[0])+1):
            # sqr_len=0
            sqr_len=mx
            while sumRegion(i,j,i+sqr_len,j+sqr_len)<=threshold:
                sqr_len+=1
                mx = max(sqr_len,mx)
    return mx