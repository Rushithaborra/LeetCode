class Solution(object):
    def findTilt(self, root):
        
        self.tilt = 0
        
        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            self.tilt += abs(left - right)
            
            return left + right + node.val
        
        dfs(root)
        
        return self.tilt