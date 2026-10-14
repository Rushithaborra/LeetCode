class Solution(object):
    def maxSumOfSquares(self, num, sum):
        if sum > 9 * num:
            return ""

        if sum == 0:
            return "0" if num == 1 else ""

        q, r = divmod(sum, 9)
        digits = [9] * q

        if r > 0:
            digits.append(r)

        digits.extend([0] * (num - len(digits)))

        return ''.join(map(str, digits))