from collections import defaultdict, deque

class Solution(object):
    def countCompleteComponents(self, n, edges):
        g = defaultdict(list)

        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        vis = [False] * n
        ans = 0

        for i in range(n):
            if vis[i]:
                continue

            q = deque([i])
            vis[i] = True

            nodes = 0
            degree_sum = 0

            while q:
                u = q.popleft()
                nodes += 1
                degree_sum += len(g[u])

                for v in g[u]:
                    if not vis[v]:
                        vis[v] = True
                        q.append(v)

            edges_in_component = degree_sum // 2

            if edges_in_component == nodes * (nodes - 1) // 2:
                ans += 1

        return ans