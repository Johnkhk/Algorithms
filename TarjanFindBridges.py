from collections import defaultdict

n=4
connections=[[0,1],[2,3]]

 # Tarjan's algorithm for finding bridges
disc=[-1]*n
low=[-1]*n
time=0
adj = defaultdict(list)
for k,v in connections:
    adj[k].append(v)
    adj[v].append(k)
bridges=[]
def dfs(node,parent):
    global time
    disc[node]=low[node]=time # initally they are same (almost like adding to visited)
    time+=1
    for child in adj[node]:
        if disc[child]==-1: # not discovered
            dfs(child,node)
            low[node]=min(low[node],low[child]) # postorder changes
            
            if low[child] > disc[node]:
                bridges.append([child,node])
        elif parent !=child:
            low[node] = min(low[node],disc[child])
disc[0]=0
low[0]=0
dfs(0,None)
print(bridges)