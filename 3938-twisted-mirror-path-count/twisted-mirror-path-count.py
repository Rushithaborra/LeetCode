        
class Solution(object):
    def uniquePaths(self, grid):
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        # reflect_right[r][c]:
        # Final non-mirror cell reached after entering mirror (r,c)
        # while moving RIGHT.
        #
        # reflect_down[r][c]:
        # Final non-mirror cell reached after entering mirror (r,c)
        # while moving DOWN.
        reflect_right = [[-1] * n for _ in range(m)]
        reflect_down = [[-1] * n for _ in range(m)]

        # Compute mirror exits from bottom-right to top-left.
        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if grid[r][c] == 0:
                    continue

                # Enter mirror while moving RIGHT -> reflected DOWN
                nr, nc = r + 1, c
                if nr < m:
                    if grid[nr][nc] == 0:
                        reflect_right[r][c] = nr * n + nc
                    else:
                        reflect_right[r][c] = reflect_down[nr][nc]

                # Enter mirror while moving DOWN -> reflected RIGHT
                nr, nc = r, c + 1
                if nc < n:
                    if grid[nr][nc] == 0:
                        reflect_down[r][c] = nr * n + nc
                    else:
                        reflect_down[r][c] = reflect_right[nr][nc]

        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        for r in range(m):
            for c in range(n):
                if dp[r][c] == 0 or grid[r][c] == 1:
                    continue

                ways = dp[r][c]

                # Try moving RIGHT
                if c + 1 < n:
                    if grid[r][c + 1] == 0:
                        dp[r][c + 1] = (dp[r][c + 1] + ways) % MOD
                    else:
                        dest = reflect_right[r][c + 1]
                        if dest != -1:
                            nr, nc = divmod(dest, n)
                            dp[nr][nc] = (dp[nr][nc] + ways) % MOD

                # Try moving DOWN
                if r + 1 < m:
                    if grid[r + 1][c] == 0:
                        dp[r + 1][c] = (dp[r + 1][c] + ways) % MOD
                    else:
                        dest = reflect_down[r + 1][c]
                        if dest != -1:
                            nr, nc = divmod(dest, n)
                            dp[nr][nc] = (dp[nr][nc] + ways) % MOD

        return dp[m - 1][n - 1]