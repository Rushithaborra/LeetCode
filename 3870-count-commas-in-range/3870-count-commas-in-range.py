class Solution:
    def countCommas(self, n):
        ans = 0
        
        for i in range(1, n + 1):
            if i >= 1000:
                ans += 1
            if i >= 1000000:
                ans += 1
            if i >= 1000000000:
                ans += 1
        
        return ans