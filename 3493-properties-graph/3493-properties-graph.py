class Solution(object):
    def numberOfComponents(self, properties, k):
        n = len(properties)

        parent = list(range(n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[py] = px

        sets = [set(p) for p in properties]

        for i in range(n):
            for j in range(i + 1, n):
                if len(sets[i] & sets[j]) >= k:
                    union(i, j)

        return len(set(find(i) for i in range(n)))