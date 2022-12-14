### 1st one ###
def maxProfit(prices):
    min_so_far=float("inf")
    ret=0
    for p in prices:
        min_so_far=min(min_so_far,p)
        cost = p-min_so_far
        ret = max(ret,cost)
    return ret
