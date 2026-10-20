
class Solution(object):
    def sortableIntegers(self, nums):
        n = len(nums)
        ans = 0

        for k in range(1, n + 1):
            if n % k != 0:
                continue

            prev_max = float('-inf')
            valid = True

            for start in range(0, n, k):
                block = nums[start:start + k]
                m = len(block)

                descents = 0
                for i in range(m):
                    if block[i] > block[(i + 1) % m]:
                        descents += 1

                if descents > 1:
                    valid = False
                    break

                if min(block) < prev_max:
                    valid = False
                    break

                prev_max = max(block)

            if valid:
                ans += k

        return ans
