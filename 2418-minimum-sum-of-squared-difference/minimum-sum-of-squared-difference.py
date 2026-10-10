
class Solution(object):
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        diffs = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if sum(diffs) <= k:
            return 0

        low, high = 0, max(diffs)

        while low < high:
            mid = (low + high) // 2
            operations = sum(max(0, d - mid) for d in diffs)

            if operations <= k:
                high = mid
            else:
                low = mid + 1

        x = low
        operations = sum(max(0, d - x) for d in diffs)
        remaining = k - operations

        ans = sum(min(d, x) ** 2 for d in diffs)
        ans -= remaining * (2 * x - 1)

        return ans