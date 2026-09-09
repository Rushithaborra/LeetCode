class Solution(object):
    def lastRemaining(self, n):
        first = 1
        gap = 1
        remaining = n
        left = True

        while remaining > 1:
            if left or remaining % 2 == 1:
                first += gap

            remaining //= 2
            gap *= 2
            left = not left

        return first