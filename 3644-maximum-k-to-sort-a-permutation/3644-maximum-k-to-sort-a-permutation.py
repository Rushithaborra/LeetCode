class Solution(object):
    def sortPermutation(self, nums):
        ans = -1

        for i, num in enumerate(nums):
            if num != i:
                ans &= num & i

        return max(ans, 0)