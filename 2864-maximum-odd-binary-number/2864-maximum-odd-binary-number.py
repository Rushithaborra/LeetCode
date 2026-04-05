class Solution(object):
    def maximumOddBinaryNumber(self, s):
        ones = s.count('1')
        zeros = s.count('0')
        
        return '1' * (ones - 1) + '0' * zeros + '1'