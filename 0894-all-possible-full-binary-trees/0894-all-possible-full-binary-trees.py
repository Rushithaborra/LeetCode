class Solution(object):
    def allPossibleFBT(self, n):
        memo = {}
        
        def dfs(n):
            if n in memo:
                return memo[n]
            
            res = []
            
            if n == 1:
                return [TreeNode(0)]
            
            if n % 2 == 0:
                return []
            
            for left_nodes in range(1, n, 2):
                right_nodes = n - 1 - left_nodes
                
                left_trees = dfs(left_nodes)
                right_trees = dfs(right_nodes)
                
                for l in left_trees:
                    for r in right_trees:
                        root = TreeNode(0)
                        root.left = l
                        root.right = r
                        res.append(root)
            
            memo[n] = res
            return res
        
        return dfs(n)