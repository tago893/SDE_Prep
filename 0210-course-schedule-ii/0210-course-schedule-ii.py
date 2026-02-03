class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[ ]for _ in range(numCourses)]
        indegree = [0]*(numCourses)
        for a, b in prerequisites:
            adj[b].append(a)   # b → a
            indegree[a] += 1
                
        q = deque()
        for i in range(0,numCourses):
            if indegree[i] == 0:
                q.append(i)
        finish = []
        while q:
            node = q.popleft()
            finish.append(node)
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        if len(finish) == numCourses:
            return finish
        else:
            return [] 