from collections import deque


class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        
        q = deque([root])
        res = []
        while q:
            curr_level = []
            for _ in range(len(q)):
                node = q.popleft()
                curr_level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res.append(curr_level)
        
        return res
