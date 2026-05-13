class Solution(object):
    def minMoves(self, nums, limit):
        n = len(nums)
        diff = [0] * (2 * limit + 2)
        
        for i in range(n // 2):
            a = nums[i]
            b = nums[n - 1 - i]
            
            diff[2] += 2
            diff[2 * limit + 1] -= 2
            
            lower = min(a, b) + 1
            upper = max(a, b) + limit
            
            diff[lower] -= 1
            diff[upper + 1] += 1
            
            sum_val = a + b
            diff[sum_val] -= 1
            diff[sum_val + 1] += 1
            
        ans = n
        current_moves = 0
        for i in range(2, 2 * limit + 1):
            current_moves += diff[i]
            if current_moves < ans:
                ans = current_moves
            
        return ans