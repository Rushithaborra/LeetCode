
class Solution(object):
    def flatten(self, root):
        if not root:
            return

        stack = [root]
        prev = None

        while stack:
            curr = stack.pop()

            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)

            if prev:
                prev.left = None
                prev.right = curr

            prev = curr
