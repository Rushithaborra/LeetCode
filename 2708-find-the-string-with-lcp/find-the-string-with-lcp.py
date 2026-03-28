class Solution:
    def findTheString(self, lcp):
        n = len(lcp)

        for i in range(n):
            if lcp[i][i] != n - i:
                return ""

        parent = list(range(n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[px] = py

        for i in range(n):
            for j in range(n):
                if lcp[i][j] > 0:
                    union(i, j)

        group_char = {}
        res = [''] * n
        curr_char = 'a'

        for i in range(n):
            root = find(i)
            if root not in group_char:
                if curr_char > 'z':
                    return ""
                group_char[root] = curr_char
                curr_char = chr(ord(curr_char) + 1)
            res[i] = group_char[root]

        word = "".join(res)

        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if word[i] == word[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = 0

                if dp[i][j] != lcp[i][j]:
                    return ""

        return word