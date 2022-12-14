def lengthOfLongestSubstring(self, s: str) -> int:
    # d= {}
    #O(2n)
    
    
    d=defaultdict(int)
    n=len(s)
    l,r = 0,0
    mx=0
    for r in range(n):
        d[s[r]]+=1
        
        while d[s[r]]>1:
            d[s[l]]-=1
            l+=1
        mx = max(mx,r-l+1)
        
        
    return mx
    