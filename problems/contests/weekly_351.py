# q2
class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        """
        num1 - k*num2 - (2^i1 + 2^i2 + ... 2^ik) = 0
        let target = (2^i1 + 2^i2 + ... 2^ik)
        num1 - k*num2 - target = 0
        target = num1 - k*num2
        
        by nature of the problem, target.bitcount() <= k 
        because you can always use more k by separating 2^1 to 2^0 + 2^0
        
        the upper limit of k is target because you can just 2^0 for everything
        
        Therefore we have this ineq:
        target.bit_count() <= k <= target
        
        target>=0 because we need valid (2^i1 + 2^i2 + ... 2^ik)
        """
        
        
        def count_set_bits(number):
            count = 0
            while number:
                count += number & 1
                number >>= 1
            return count
        for k in range(61):
            target = num1 - k*num2
            if target>=0 and count_set_bits(target) <= k <= target:
                return k
            
        return -1

# q3
class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        
        n = len(nums)
        idx = 0
        for i in range(n):
            if nums[i]==1:
                idx = i+1
                break
        if idx == 0:
            return 0
        ans = 1
        numzeros = 0
        while idx<n:
            if nums[idx]==0:
                numzeros+=1
            else:
                ans*=(numzeros+1)
                numzeros=0
            idx+=1
        return ans % (10**9 + 7)
        
        # return 9
        # [0,1,0,0,1,0,0,1]
        
#         3
#         [0,1],[0,0,1],[0,0,1]
#         [0,1,0],[0,1],[0,0,1]        
#         [0,1,0,0],[1],[0,0,1]
        
#         3
#         [...],[0,0,1],[0,0,1]
#         [...],[0,0,1,0],[0,1]
#         [...],[0,0,1,0,0],[1]
        
     # 230630552

# q4
class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        idxs = [i for i in range(n)]
        a = list(zip(positions, healths, directions, idxs))
        a.sort(key=lambda x: x[0])
        # print(a)
        stack = [[a[0][1], a[0][2], a[0][3]]]
        for i in range(1,n):
            pos, health, d, idx = a[i][0], a[i][1], a[i][2], a[i][3]
            
            # if stack and d!=stack[-1][1]:
            while stack and stack[-1][1]=="R" and d=="L" and health>stack[-1][0]:
                stack.pop()
                health-=1

                
            if stack and stack[-1][1]=="R" and d=="L" and stack[-1][0] > health:
                    stack[-1][0]-=1
                    continue
            if stack and stack[-1][1]=="R" and d=="L" and stack[-1][0] == health:
                stack.pop()
                continue
            stack.append([health,d,idx])
        
        stack.sort(key=lambda x:x[-1])
        return [a for a,b,c in stack]
        
        