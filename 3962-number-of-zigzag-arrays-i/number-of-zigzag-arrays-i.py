class Solution(object):
    def zigZagArrays(self, n, l, r):
        MOD = 10**9 + 7
        m = r - l + 1

        up = [0] * m
        down = [0] * m

        for y in range(m):
            up[y] = y
            down[y] = m - 1 - y

        if n == 2:
            return (sum(up) + sum(down)) % MOD

        for _ in range(3, n + 1):
            newUp = [0] * m
            newDown = [0] * m

            pref = 0
            for i in range(m):
                newUp[i] = pref
                pref = (pref + down[i]) % MOD

            suff = 0
            for i in range(m - 1, -1, -1):
                newDown[i] = suff
                suff = (suff + up[i]) % MOD

            up = newUp
            down = newDown

        return (sum(up) + sum(down)) % MOD