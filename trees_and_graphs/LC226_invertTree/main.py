class Solution:
    def invertTree(self, root):
        if not root:
            return root

        right = self.invertTree(root.left)

        left = self.invertTree(root.right)

        root.right, root.left = right, left

        return root
