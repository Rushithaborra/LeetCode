class Solution(object):
    def sumOfLeftLeaves(self, root):
        if not root:
            return 0
        
        def dfs(node):
            if not node:
                return 0
            
            total = 0
            
            if node.left:
                if not node.left.left and not node.left.right:
                    total += node.left.val
                else:
                    total += dfs(node.left)

            total += dfs(node.right)
            
            return total
        
        return dfs(root)