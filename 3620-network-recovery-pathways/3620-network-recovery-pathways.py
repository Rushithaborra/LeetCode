from collections import deque

class Solution(object):
    def findMaxPathScore(self, edges, online, k):
        n = len(online)
        graph = [[] for _ in range(n)]
        indegree = [0] * n
        maxCost = 0

        for u, v, c in edges:
            graph[u].append((v, c))
            indegree[v] += 1
            maxCost = max(maxCost, c)

        q = deque()
        topo = []
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)

        while q:
            u = q.popleft()
            topo.append(u)
            for v, _ in graph[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)

        INF = float("inf")

        def check(limit):
            dp = [INF] * n
            dp[0] = 0

            for u in topo:
                if dp[u] == INF:
                    continue
                if u != 0 and u != n - 1 and not online[u]:
                    continue
                for v, c in graph[u]:
                    if c < limit:
                        continue
                    if v != n - 1 and not online[v]:
                        continue
                    if dp[u] + c < dp[v]:
                        dp[v] = dp[u] + c

            return dp[n - 1] <= k

        lo, hi = 0, maxCost
        ans = -1

        while lo <= hi:
            mid = (lo + hi) // 2
            if check(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1

        return ans