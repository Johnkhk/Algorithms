# Q2 good way to get all the powers in linear time
class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        # 1010011
        # 1000000
        #   10000
        #      10
        #       1
        # print(bin(0b1010011<<1))
        # print(bin(0b1010011%2))
        
        # e.g: 39-> 0b100111
        # [], 100111
        # [1], 10011
        # [1,10], 1001
        # [1,10,100], 100
        # [1,10,100], 10
        # [1,10,100], 1 shift=5
        # [1,10,100,100000],
        
        MOD = 10**9 + 7
        
        
        twos=[]
        shift=0
        while n>0:
            if n%2==1: 
                twos.append(1<<shift)
            shift+=1
            # n//=2
            n>>=1
        # print(twos)
        # print([bin(a) for a in twos])
        ans=[]
        for s,e in queries:
            prod=1
            for i in range(s,e+1):
                prod*=twos[i]
            ans.append(prod%MOD)
        return ans
            
                
            
        
# Q4
class Solution:
    def componentValue(self, nums: List[int], edges: List[List[int]]) -> int:
        
        """
        The smallest nodes definetly cannot be the value (by themselves)
        
        
        backup idea2:
        we iterate curtarget from sum of all nodes to the biggest node, then we union everything, if it does not work
        6,2,4,4,3,5,3,5, target 8
        if u take 3,3,2 ur screwed
        
        
        actual idea:
            use a dfs function to return the value up to parent, if we have the target, return 0... we need the final return to be 0
            then, we just iterate over possible number of parts we can have. we use the total sum of the nodes and divide that by the number of parts and that is our target, we use that in our dfs function.
        """
        adj=defaultdict(list)
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
            
        def dfs(idx, parent, target):
            # print(idx)
            val = nums[idx]
            visited.add(idx)
            for i in adj[idx]:
                if i in visited:
                    continue
                
                # if i==parent: # because it is non directed, we dont want 0->1,1->0 infinite
                    # continue
                val+=dfs(i,idx,target)
            if val==target:
                return 0
            return val
        
        total = sum(nums)
        p = len(nums)
        res=0
        for parts in range(1,p+1):
            if total%parts!=0:
                continue
            target = total//parts
            visited=set()
            
            if dfs(0,-1,target)!=0:
                continue
            res = max(res, parts-1) # parts-1 is how man splits
        return res
        