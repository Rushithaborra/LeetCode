class Solution(object):
    def checkOnesSegment(self, s):
        seen_zero = False
        
        for c in s:
            if c == '0':
                seen_zero = True
            if c == '1' and seen_zero:
                return False
        
        return True