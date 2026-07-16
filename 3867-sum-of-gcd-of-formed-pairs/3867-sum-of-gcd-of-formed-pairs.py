class Solution(object):
    def gcdSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)

        prefixGcd = [0] * n
        mx = 0

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        for i in range(n):
            if nums[i] > mx:
                mx = nums[i]
            prefixGcd[i] = gcd(nums[i], mx)

        prefixGcd.sort()

        ans = 0
        left, right = 0, n - 1

        while left < right:
            ans += gcd(prefixGcd[left], prefixGcd[right])
            left += 1
            right -= 1

        return ans