class Solution(object):
    def findMode(self, root):
        from collections import defaultdict
        
        freq = defaultdict(int)
        
        # Step 1: Traverse tree
        def dfs(node):
            if not node:
                return
            freq[node.val] += 1
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        
        max_freq = max(freq.values())
        
        result = []
        for key in freq:
            if freq[key] == max_freq:
                result.append(key)
        
        return result