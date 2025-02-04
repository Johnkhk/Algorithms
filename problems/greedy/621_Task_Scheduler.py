def leastInterval(tasks, n):
    # Greedily do the largestcount tasks first.
    """
    real idea:
    use a heap of frequencies. 

    We always pop and add it to the queue if the heap isn't empty.
    But we only add it back to the heap(with decreased freq) if the time is up for the top element in queue

    Note, we don't even need the key because we know we will be greedy. 
    e.g if we have AAABB. we pop A, then its AABB, but we still know 
    we will pop B because of cooldown, by ignoring key, we assume B 
    will be popped/

    Then, we use a queue to store the frequency and the time. 
    if time is up we add it back to the heap decreased by 1 frequency. 
    this is only if frequency isnt zero..
    """
    c = Counter(tasks)
    h=[]
    for k,v in c.items():
        heapq.heappush(h,(-v,k))

    res = 0
    q = deque()
    time = 0
    while h or q:
        if q and q[0][1] == time:
            f_,t_ = q.popleft()
            if f_<0:
                heapq.heappush(h,(f_,key))
        if h:
            freq,key = heapq.heappop(h)
            if freq+1==0:
                time+=1
                continue
            q.append((freq+1,time+n+1))
        time+=1
    return time