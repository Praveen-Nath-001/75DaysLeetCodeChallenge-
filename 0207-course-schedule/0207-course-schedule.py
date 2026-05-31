class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]

        for a, b in prerequisites:
            adj[b].append(a)

        from collections import deque
        q = deque()
        indegree = [0]*numCourses
        ans = []
        
        for i in range(numCourses):
            for nbr in adj[i]:
                indegree[nbr] += 1

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        while q:
            node = q.popleft()
            ans.append(node)
            for nbr in adj[node]:
                indegree[nbr] -= 1
                if indegree[nbr] == 0:
                    q.append(nbr)

        return len(ans) == numCourses

        