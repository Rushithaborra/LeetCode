class Solution:
    def checkSubarraySum(self, nums, k):
        prefix = 0
        seen = {0: -1}

        for i in range(len(nums)):
            prefix += nums[i]
            rem = prefix % k

            if rem in seen:
                if i - seen[rem] >= 2:
                    return True
            else:
                seen[rem] = i

        return False