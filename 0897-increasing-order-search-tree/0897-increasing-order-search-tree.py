class Solution(object):
    def increasingBST(self, root):
        dummy = TreeNode(0)   # temporary node
        self.curr = dummy
        
        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            
            # process node
            node.left = None
            self.curr.right = node
            self.curr = node
            
            inorder(node.right)
        
        inorder(root)
        return dummy.right