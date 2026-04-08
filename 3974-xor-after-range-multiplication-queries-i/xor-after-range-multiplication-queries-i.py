class Solution(object):
    def xorAfterQueries(self, nums, queries):
        MOD = 10**9 + 7
        n = len(nums)
        
        mul = [1] * n
        
        for l, r, k, val in queries:
            i = l
            while i <= r:
                mul[i] = (mul[i] * val) % MOD
                i += k

        res = 0
        for i in range(n):
            nums[i] = (nums[i] * mul[i]) % MOD
            res ^= nums[i]
        
        return res