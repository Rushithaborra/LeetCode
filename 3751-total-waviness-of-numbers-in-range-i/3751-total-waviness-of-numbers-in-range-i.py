class Solution(object):
    def totalWaviness(self, num1, num2):

        def solve(n):
            if n < 0:
                return 0

            s = str(n)
            memo = {}

            def dp(pos, tight, started, last2, last1, length):
                key = (pos, tight, started, last2, last1, length)

                if key in memo:
                    return memo[key]

                if pos == len(s):
                    return (1, 0)  # (count_numbers, total_waviness)

                limit = int(s[pos]) if tight else 9

                total_count = 0
                total_wavy = 0

                for d in xrange(limit + 1):
                    ntight = tight and (d == limit)

                    if not started and d == 0:
                        cnt, wav = dp(
                            pos + 1,
                            ntight,
                            False,
                            -1,
                            -1,
                            0
                        )
                        total_count += cnt
                        total_wavy += wav

                    elif not started:
                        cnt, wav = dp(
                            pos + 1,
                            ntight,
                            True,
                            -1,
                            d,
                            1
                        )
                        total_count += cnt
                        total_wavy += wav

                    else:
                        extra = 0

                        if length >= 2:
                            a = last2
                            b = last1
                            c = d

                            if (b > a and b > c) or (b < a and b < c):
                                extra = 1

                        nlast2 = last1

                        cnt, wav = dp(
                            pos + 1,
                            ntight,
                            True,
                            nlast2,
                            d,
                            length + 1
                        )

                        total_count += cnt
                        total_wavy += wav + cnt * extra

                memo[key] = (total_count, total_wavy)
                return memo[key]

            return dp(0, True, False, -1, -1, 0)[1]

        return solve(num2) - solve(num1 - 1)