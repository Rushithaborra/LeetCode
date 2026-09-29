class Solution:
    def hasValidPath(self, grid):
        m = len(grid)
        n = len(grid[0])

        # Total number of cells in the path must be even
        if (m + n - 1) % 2 != 0:
            return False

        # Start must be '(' and end must be ')'
        if grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False

        memo = {}

        def dfs(r, c, balance):
            # Invalid if we have more ')' than '('
            if balance < 0:
                return False

            # If this is the last cell
            if r == m - 1 and c == n - 1:
                return balance == 0

            state = (r, c, balance)

            if state in memo:
                return memo[state]

            # Move down
            if r + 1 < m:
                new_balance = balance + (1 if grid[r + 1][c] == '(' else -1)

                if dfs(r + 1, c, new_balance):
                    memo[state] = True
                    return True

            # Move right
            if c + 1 < n:
                new_balance = balance + (1 if grid[r][c + 1] == '(' else -1)

                if dfs(r, c + 1, new_balance):
                    memo[state] = True
                    return True

            memo[state] = False
            return False

        return dfs(0, 0, 1)