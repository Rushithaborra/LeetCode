class Solution(object):
    def minOperations(self, s):
        start0 = sum(int(s[i]) != i % 2 for i in range(len(s)))
        return min(start0, len(s) - start0)