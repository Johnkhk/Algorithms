# TOPSORT STEPS:
# 1. Build the adjacency list and indegree
# tip: indegree is the number of incoming edges to a node
# tip: if you need flour to make bread, flour has an indegree of 0, bread has an indegree of 1
# 2. Add all nodes with indegree 0 to the queue
# 4. Pop node from queue and reduce its neighbors indegree by 1
# 5. If indegree of neighbor is 0, that item can be "made", can add to queue


# Time: O(V+E)
# Space: O(V)

from collections import deque

numCourses = 4
prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2], [0, 1]]

q = []
adj = {i: [] for i in range(numCourses)}
indegree = {i: 0 for i in range(numCourses)}
# in the D-Graph prereq->course
for totake, prereq in prerequisites:
    adj[prereq].append(totake)
    indegree[totake] += 1

# Add indegree 0 keys into queue
q = deque([key for key, val in indegree.items() if val == 0])
ans = []
while q:
    node = q.pop()
    ans.append(node)
    for child in adj[node]:
        indegree[child] -= 1
        if indegree[child] == 0:
            q.append(child)
if len(ans) != numCourses:
    print([])
    # return []
print(ans)
# return ans


### Alien Dictionary Khan's Algorithm ###
def alienOrder(words):
    """
    goal:
        return a string of the unique letters in sorted order
        if no solution return ""
    idea:
        build a adjacenct listof words that differ (the order)
        top sort the adj list with khan's algorithm
        first word -> second word
        indegree[second word]+=1
    Complexity:
        Let N be the total number of strings in the input list.
        Let C be the total length of all the words in the input list, added together.
        Let U be the total number of unique letters in the alien alphabet.
        TC: O(C)
            building the adj list and identifying all relations could take up all C.
            For the BFS, it is O(V+E) where V=U (U vertices cuz unique chars are in indegree), and N-1 edges since we only compare 1:1
            So, BFS is O(U+N)
        SC: O(V+E) = O(U+min(U^2N))
            For fixed alphabet: 26 letters
            U is 26 so technically O(1)
    """
    # indegree = {i:0 for i in mp.keys()}
    # indegree = defaultdict(int)
    indegree = Counter({c: 0 for word in words for c in word})
    mp = defaultdict(set)
    for i in range(len(words) - 1):
        minlen = min(len(words[i]), len(words[i + 1]))

        if (
            len(words[i]) > len(words[i + 1])
            and words[i][:minlen] == words[i + 1][:minlen]
        ):
            return ""

        for j in range(minlen):
            if words[i][j] != words[i + 1][j]:
                if words[i + 1][j] not in mp[words[i][j]]:
                    mp[words[i][j]].add(words[i + 1][j])
                    indegree[words[i + 1][j]] += 1
                break
    x = 0
    q = deque()
    for k, v in indegree.items():
        # if k in mp or k in mp[k]:
        if v == 0:
            q.append(k)
        # if v==0:
        #     q.append(k)
    ans = []
    while q:
        node = q.popleft()
        x += 1
        ans.append(node)
        for child in mp[node]:
            indegree[child] -= 1
            if indegree[child] == 0:
                q.append(child)
    if x != len(indegree):
        return ""
    return "".join(ans)


### Alien Dictionary DFS (WHITE,GREY,BLACK) (Reverse ADJ List) ###
def alienOrder(words):
    mp = {char: set() for word in words for char in word}
    for i in range(len(words) - 1):
        minlen = min(len(words[i]), len(words[i + 1]))
        if (
            len(words[i]) > len(words[i + 1])
            and words[i][:minlen] == words[i + 1][:minlen]
        ):
            return ""
        for j in range(minlen):
            if words[i][j] != words[i + 1][j]:
                mp[words[i + 1][j]].add(words[i][j])
                break
    visited = defaultdict(bool)  # True: black, False: grey
    res = []

    def dfs(node):
        if node in visited:
            return visited[node]
        visited[node] = False
        for child in mp[node]:
            status = dfs(child)
            if status == False:
                return False
        visited[node] = True
        # post order we add
        res.append(node)
        return True

    for key, val in mp.items():
        if not dfs(key):
            return ""
    return "".join(res)


### Alien Dictionary DFS (WHITE,GREY,BLACK) (Forward ADJ List, Reverse Result) ###
def alienOrder(words):
    mp = {char: set() for word in words for char in word}
    for i in range(len(words) - 1):
        minlen = min(len(words[i]), len(words[i + 1]))
        if (
            len(words[i]) > len(words[i + 1])
            and words[i][:minlen] == words[i + 1][:minlen]
        ):
            return ""
        for j in range(minlen):
            if words[i][j] != words[i + 1][j]:
                mp[words[i][j]].add(words[i + 1][j])
                break

    visited = defaultdict(bool)  # True: black, False: grey
    res = []

    def dfs(node):
        """
        Very good DFS to mark white,grey,black
        """
        if node in visited:
            return visited[node]
        visited[node] = False
        for child in mp[node]:
            status = dfs(child)
            if status == False:
                return False
        visited[node] = True
        # post order we add
        res.append(node)
        return True

    for key, val in mp.items():
        if not dfs(key):
            return ""
    return "".join(res[::-1])
