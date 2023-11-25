from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue, res = [], []
        if not root:
            return res
        queue.append(root)
        res.append([root.val])
        while queue:
            level = []
            while queue:
                node = queue.pop(0)
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            if level:
                res.append([node.val for node in level])
                queue.extend(level)
        return res
