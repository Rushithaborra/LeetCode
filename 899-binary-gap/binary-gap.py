class Solution(object):
    def binaryGap(self, n):
        b = bin(n)[2:] 
        prev = -1
        max_gap = 0

        for i in range(len(b)):
            if b[i] == '1':
                if prev != -1:
                    max_gap = max(max_gap, i - prev)
                prev = i

        return max_gap