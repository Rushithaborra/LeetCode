class Solution(object):
    def balanceBST(self, root):
        
        def inorder(node, arr):
            if not node:
                return
            inorder(node.left, arr)
            arr.append(node.val)
            inorder(node.right, arr)
        
        arr = []
        inorder(root, arr)
        
        def build(left, right):
            if left > right:
                return None
            
            mid = (left + right) // 2
            
            node = TreeNode(arr[mid])
            node.left = build(left, mid - 1)
            node.right = build(mid + 1, right)
            
            return node
        
        return build(0, len(arr) - 1)