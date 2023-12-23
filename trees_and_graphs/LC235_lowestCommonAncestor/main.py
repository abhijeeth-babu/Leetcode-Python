class Solution:
    def lowestCommonAncestor(self, root, p, q):
        curr = root
        while curr:
            if curr.val > p.val and curr.val > q.val:
                curr = curr.left
            elif curr.val < p.val and curr.val < q.val:
                curr = curr.right
            else:
                return curr
            
    # recursive      
    # def lowestCommonAncestor(self, root, p, q):
    #     if root.val > p.val and root.val > q.val:
    #         return self.lowestCommonAncestor(root.left, p, q)
    #     elif root.val < p.val and root.val < q.val:
    #         return self.lowestCommonAncestor(root.right, p, q)
    #     else:
    #         return root