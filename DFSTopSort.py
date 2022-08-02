numCourses = 4
# prerequisites = [[1,0],[2,0],[3,1],[3,2],[0,1]] #Cycle
prerequisites = [[1,0],[2,0],[3,1],[3,2]] #No Cycle

def dfs(node):
    visited.add(node)
    dfsvisited.add(node)
    for child in adj[node]:
        if child in visited and child in dfsvisited:
            return True #cycle
        elif child not in visited:
            if dfs(child):
                return True
    dfsvisited.remove(node)
    stack.append(node)
    return False
visited = set()
dfsvisited = set()
stack=[]


adj={i:[] for i in range(numCourses)}
for totake, prereq in prerequisites:
    adj[prereq].append(totake)
for i in range(numCourses):
    if i not in visited and dfs(i):
        print([])
        #  return []
print(stack)
# return anstacks
