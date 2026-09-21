class Solution(object):
    def resultArray(self, nums, k):
        result = [0] * k
        dp = [0] * k

        for num in nums:
            r = num % k
            new_dp = [0] * k

            new_dp[r] += 1

            for p in range(k):
                if dp[p]:
                    new_dp[(p * r) % k] += dp[p]

            for x in range(k):
                result[x] += new_dp[x]

            dp = new_dp

        return result