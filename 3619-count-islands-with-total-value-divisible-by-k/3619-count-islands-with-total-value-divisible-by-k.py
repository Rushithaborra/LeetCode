
class Solution:
    def countIslands(self, grid, k):
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]

        def dfs(r, c):
            if (r < 0 or r >= m or c < 0 or c >= n
                    or visited[r][c] or grid[r][c] == 0):
                return 0

            visited[r][c] = True
            total = grid[r][c]

            total += dfs(r + 1, c)
            total += dfs(r - 1, c)
            total += dfs(r, c + 1)
            total += dfs(r, c - 1)

            return total

        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0 and not visited[i][j]:
                    total = dfs(i, j)

                    if total % k == 0:
                        count += 1

        return count
