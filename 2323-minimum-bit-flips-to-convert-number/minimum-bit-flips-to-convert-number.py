class Solution(object):
    def minBitFlips(self, start, goal):
        x = start ^ goal
        count = 0
        
        while x:
            x &= (x - 1)  
            count += 1
        
        return count