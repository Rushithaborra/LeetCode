class Solution(object):
    def minimumOperations(self, nums):
        operations = 0
        for num in nums:
            remainder = num % 3
            if remainder != 0:
                operations += 1
        return operations