class Solution:
    def constructFromPrePost(self, preorder, postorder):
        postMap = {}

        for i in range(len(postorder)):
            postMap[postorder[i]] = i

        self.preIndex = 0

        def build(left, right):
            if left > right:
                return None

            root = TreeNode(preorder[self.preIndex])
            self.preIndex += 1

            if left == right:
                return root

            nextValue = preorder[self.preIndex]

            index = postMap[nextValue]

            root.left = build(left, index)
            root.right = build(index + 1, right - 1)

            return root

        return build(0, len(postorder) - 1)