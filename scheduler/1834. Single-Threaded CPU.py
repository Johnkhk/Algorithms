class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        for i in range(len(tasks)):
            tasks[i].append(i)
        tasks.sort(key=lambda x:x[0])
        
        ans,h=[],[]
        i,time = 0, tasks[0][0]
        
        while i<len(tasks) or h:
            while i<len(tasks) and tasks[i][0]<=time: 
                heapq.heappush(h,(tasks[i][1],tasks[i][2])) #process time and idx
                i+=1
            
            if h:
                # started the task and finished it
                proc_time, idx = heapq.heappop(h)
                time+=proc_time
                ans.append(idx)
            else: # cpu is idle
                time = tasks[i][0]
        return ans
                
                