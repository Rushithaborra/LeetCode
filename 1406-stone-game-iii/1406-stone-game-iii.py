class Solution(object):
    def stoneGameIII(self, stoneValue):
        n = len(stoneValue)
        dp = [0, 0, 0, 0]

        for i in range(n - 1, -1, -1):
            best = float("-inf")
            s = 0
            for j in range(3):
                if i + j < n:
                    s += stoneValue[i + j]
                    best = max(best, s - dp[(i + j + 1) % 4])
            dp[i % 4] = best

        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        return "Tie"