class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        comp = [0] * n
        curr = 0

        for i in range(1, n):
            if nums[i] - nums[i - 1] > maxDiff:
                curr += 1
            comp[i] = curr

        ans = []
        for u, v in queries:
            ans.append(comp[u] == comp[v])

        return ans