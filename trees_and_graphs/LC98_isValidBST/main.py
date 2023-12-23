class Solution:
    def isValidBST(self, root):
        return self.helper(root, float('-inf'), float('inf'))
    
    def helper(self, node, min_val, max_val):
        if not node:
            return True
        
        if not (min_val < node.val < max_val):
            return False
        
        return self.helper(node.left, min_val, node.val) and self.helper(node.right, node.val, max_val)