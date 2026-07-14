class Solution:
    def subsequencePairCount(self, nums):
        MOD = 10**9 + 7
        n = len(nums)

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        memo = {}

        def dp(i, g1, g2):
            if (i, g1, g2) in memo:
                return memo[(i, g1, g2)]

            if i == n:
                return 1 if g1 == g2 and g1 != 0 else 0

            # Skip current element
            ans = dp(i + 1, g1, g2)

            # Put current element in first subsequence
            ng1 = nums[i] if g1 == 0 else gcd(g1, nums[i])
            ans += dp(i + 1, ng1, g2)

            # Put current element in second subsequence
            ng2 = nums[i] if g2 == 0 else gcd(g2, nums[i])
            ans += dp(i + 1, g1, ng2)

            ans %= MOD
            memo[(i, g1, g2)] = ans
            return ans

        return dp(0, 0, 0)