class Solution(object):
    def getAllElements(self, root1, root2):
        def inorder(root, arr):
            if not root:
                return
            inorder(root.left, arr)
            arr.append(root.val)
            inorder(root.right, arr)

        a = []
        b = []
        inorder(root1, a)
        inorder(root2, b)

        i = j = 0
        ans = []

        while i < len(a) and j < len(b):
            if a[i] <= b[j]:
                ans.append(a[i])
                i += 1
            else:
                ans.append(b[j])
                j += 1

        ans.extend(a[i:])
        ans.extend(b[j:])

        return ans