class Solution:
    def kthSmallest(self, root, k):
        res = self.inorder(root)

        return res[k-1]
    
    def inorder(self, node):
        if not node:
            return []
        
        left = self.inorder(node.left)
        right = self.inorder(node.right)

        return left + [node.val] + right
    
