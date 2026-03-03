# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def printTree(self, root):
        
        def getHeight(node):
            if not node:
                return -1
            return 1 + max(getHeight(node.left), getHeight(node.right))
        
        height = getHeight(root)
        rows = height + 1
        cols = 2**(height + 1) - 1
        
        res = [["" for _ in range(cols)] for _ in range(rows)]
        
        def fill(node, r, c):
            if not node:
                return
            
            res[r][c] = str(node.val)
            
            offset = 2 ** (height - r - 1)
            
            if node.left:
                fill(node.left, r + 1, c - offset)
            
            if node.right:
                fill(node.right, r + 1, c + offset)
        
        fill(root, 0, (cols - 1) // 2)
        
        return res
        