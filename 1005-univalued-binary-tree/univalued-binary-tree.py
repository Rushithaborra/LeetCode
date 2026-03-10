class Solution(object):
    def isUnivalTree(self, root):
        
        val = root.val
        
        def dfs(node):
            if not node:
                return True
            
            if node.val != val:
                return False
            
            return dfs(node.left) and dfs(node.right)
        
        return dfs(root)