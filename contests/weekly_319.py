# https://www.youtube.com/watch?v=ZYuitS5_XuA
# Joshua Chen a GOD
# Please watch his video
# https://www.youtube.com/watch?v=fbCPh9pD44o

# Q2 ### Number of Subarrays With LCM Equal to K ###
"""
key is to know that:
the lcm of 2 numbers is their product divided by their gcd
"""
import math
# a = math.gcd(3,6)
# print(a)
# nums = [3,4,7,12,8] # 168
"""
euclidean gcd algorithm:
    e.g: 1701,3768
    a,b = 366, 1701
    a,b = 237, 366
    a,b = 129, 237
    a,b = 108, 129
    a,b = 21, 108
    a,b = 3, 21
    a,b = 0, 3
"""
def gcd(a,b):
    while a:
        a, b = b % a, a
    return b

nums = [3,4,12] # 12
cur = nums[0]
for num in nums:
    # cur = cur*num // math.gcd(cur,num)
    cur = cur*num // gcd(cur,num)

print(cur)

# Q3 2471. Minimum Number of Operations to Sort a Binary Tree by Level
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        """
        we need to know at each level:
            how many swaps does it take to sort the list!
            e.g: [6,3,4,5] -> [3,4,5,6]
            [1,2,3] -> [2,3,1]
            graph: (1,2),(2,3),(3,1). if have m components, takes m-1 swaps
                   we have m=3, so takes 2 swaps
            
            [1,2,3] -> [2,1,3]
            graph: (1,2),(2,1) -> m=2 takes 1 swap
                   (3,3) -> m=1 takes 0 swap
            so takes 1 swap
        
        """
        edges = defaultdict(list)
        
        # lev = [root]
        lev = deque([root])
        
        seen = set()
        def dfs(node):
            """
            dfs function to count how many elems in a component
            """
            tot=1
            seen.add(node)
            if node in edges:
                for nei in edges[node]:
                    if nei not in seen:
                        tot+=dfs(nei)
            return tot
                
                
                
        ans=0
        while lev:
            a1=[]
            for i in range(len(lev)):
                node = lev.popleft()
                a1.append(node.val)
                if node.left:
                    lev.append(node.left)
                if node.right:
                    lev.append(node.right)
            a2 = sorted(a1)    
            
            # a1 = [i.val for i in lev]
            # a2 = sorted(a1)
            for i,j in zip(a1,a2):
                edges[i].append(j)
                edges[j].append(i)
            swaps=0
            for i in a1:
                swaps+=dfs(i)-1
            ans+=swaps
            
            
            
#             nxt=[]
#             for i in lev:
#                 if i.left:
#                     nxt.append(i.left)
#                 if i.right:
#                     nxt.append(i.right)
#             lev=nxt[:]
        return ans


## Q4 palindrome DP and Max pali DP
class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        
        """
        create a matrix p, where p[x][y]: is the subarr from x:y palindromic?
        loop: e.g n=4
        i,j:
        (3,3)
        (2,2),(2,3)
        (1,1),(1,2),(1,3)
        (0,0),(0,1),(0,2),(0,3)
        """
        n = len(s)
        # n = 4
        
        p = [[False]*n for _ in range(n)]
        # print(n)
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                # print(i,j)
                if i==j:
                    p[i][j] = True # size 1
                elif i+1==j and s[i]==s[j]: # size 2 and same
                    p[i][j] = True
                else:
                    p[i][j] = s[i]==s[j] and p[i+1][j-1]
        memo = {}
        
        """
        abacc
        last c: 0
        2nd last c: 
        
        
        """
        # def dfs(i):
        #     if i in memo:
        #         return memo[i]
        #     if i>=n:
        #         return 0
        #     cur = dfs(i+1)
        #     for j in range(i+k-1,n):
        #         # if j<n:
        #         if p[i][j]:
        #             cur = max(cur,dfs(j+1)+1)
        #     memo[i] = cur
        #     return cur
        # a = dfs(0)
        # # print(memo)
        # return a
        
        # dp[i] is the max # of substr if we start at i
        dp = [0]*(n+1)            
        for i in range(n-1,-1,-1):
            dp[i]=dp[i+1]
            for j in range(i+k-1,n): # i:i+k-1 ... e.g if k=3: 0:2 (0,1,2) (3 letters)
                if p[i][j]:
                    dp[i] = max(dp[i],dp[j+1]+1) # dp[j+1] will be the remaining part of the substr, then we add 1 cuz we i:j is a substr
        return dp[0]
    
    
    
        # abac
#         [[True, False, True, False], 
#         [False, True, False, False], 
#         [False, False, True, False], 
#         [False, False, False, True]]
        # (3,3) cc : True
        # (2,2),(2,3) aa, ac : True False
        # (1,1),(1,2),(1,3) bb, ba, bc True False False
        # (0,0),(0,1),(0,2),(0,3) aa, ab, aa, ac True, False, True, False
        
        # abda
#         [[True, False, False, False], 
#          [False, True, False, False], 
#          [False, False, True, False], 
#          [False, False, False, True]]
        
        # (3,3) aa : True
        # (2,2),(2,3) dd, da : True False
        # (1,1),(1,2),(1,3) bb, bd, ba True False False
        # (0,0),(0,1),(0,2),(0,3) aa, ab, ad, aa True, False, False, False-(1,2) had to be true(bd)
        