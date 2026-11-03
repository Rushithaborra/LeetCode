class Solution(object):
    def minMoves(self, nums):
        maxi = max(nums)
        return sum(maxi - x for x in nums)