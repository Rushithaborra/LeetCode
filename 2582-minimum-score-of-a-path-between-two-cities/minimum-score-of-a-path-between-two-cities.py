from collections import defaultdict, deque

class Solution(object):
    def minScore(self, n, roads):
        graph = defaultdict(list)

        for u, v, d in roads:
            graph[u].append((v, d))
            graph[v].append((u, d))

        visited = set()
        q = deque([1])
        visited.add(1)

        ans = float('inf')

        while q:
            node = q.popleft()

            for nei, dist in graph[node]:
                ans = min(ans, dist)

                if nei not in visited:
                    visited.add(nei)
                    q.append(nei)

        return ans