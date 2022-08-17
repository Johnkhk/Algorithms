def maxScore(cardPoints, k):
    # goal: fing maximum score obtained from picking k cards from start and end of deck
    """
    idea: 
    Use a sliding window approach
    Sum the last k elements (we using all the cards at the end)
    have a window from 0 to len(List)-k (not including len(List)-k)
    shift the window K times using iterator i:
        when we shift we must add the element at i to cursum
        then we must minus the element at len(nums)-k+i
        then we keep a running max
    TC:O(k)
    SC:O(k)
    """
    mx=0
    cursum=0
    n = len(cardPoints)
    for i in range(k):
        cursum+= cardPoints[n-1-i]
    mx = max(mx,cursum)

    l,r = 0,n-k
    for i in range(k):
        cursum+=cardPoints[l]
        cursum-=cardPoints[r]
        l+=1
        r+=1
        mx = max(mx,cursum)
    return mx
cardPoints=[9,7,7,9,7,7,9]
k=7
print(maxScore(cardPoints,k))