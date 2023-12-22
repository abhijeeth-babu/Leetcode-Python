class Solution():
    def isSubtree(self, s, t):
        if not s:
            return False
        
        if not t:
            return False
        
        if self.isSameTree(s, t):
            return True
        
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
    
    
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        
        if not p or not q:
            return False
        
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)