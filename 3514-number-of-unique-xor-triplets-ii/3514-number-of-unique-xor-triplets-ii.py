class Solution(object):
    def uniqueXorTriplets(self, nums):
        n = len(nums)
        if n == 1:
            return 1

        pair = [False] * 2048

        for i in range(n):
            for j in range(i + 1, n):
                pair[nums[i] ^ nums[j]] = True

        ans = [False] * 2048

        for x in range(2048):
            if pair[x]:
                for v in nums:
                    ans[x ^ v] = True

        return sum(ans)