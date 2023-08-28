# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root


root = TreeNode(6)
p = TreeNode(2)
q = TreeNode(8)
root.left = p
root.right = q

s = TreeNode(10)
t = TreeNode(1)
q.right = s
p.left = t

assert Solution().lowestCommonAncestor(root, p, q) == root
assert Solution().lowestCommonAncestor(root, s, q) == q
assert Solution().lowestCommonAncestor(root, p, t) == p
print("OK")
