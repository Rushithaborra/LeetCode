class Solution(object):
    def reverseBits(self, n):
        rev = 0
        
        for _ in range(32):
            bit = n & 1
            rev = (rev << 1) | bit
            n >>= 1
            
        return rev