from collections import defaultdict, deque

class Solution(object):
    def remainingMethods(self, n, k, invocations):
        graph = defaultdict(list)
        for u, v in invocations:
            graph[u].append(v)

        suspicious = [False] * n
        q = deque([k])
        suspicious[k] = True

        while q:
            u = q.popleft()
            for v in graph[u]:
                if not suspicious[v]:
                    suspicious[v] = True
                    q.append(v)

        for u, v in invocations:
            if not suspicious[u] and suspicious[v]:
                return list(range(n))

        return [i for i in range(n) if not suspicious[i]]