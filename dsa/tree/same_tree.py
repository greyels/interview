# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def isSame(node1, node2):
            if (not node1 and node2) or (node1 and not node2):
                return False
            elif not node1 and not node2:
                return True
            else:
                if node1.val != node2.val:
                    return False
            return isSame(node1.left, node2.left) and isSame(node1.right, node2.right)

        return isSame(p, q)

    def isSameTreeStack(self, p, q):
        stack = [(p, q)]
        while len(stack):
            first, second = stack.pop()
            if not first and not second:
                pass
            elif not first or not second:
                return False
            else:
                if first.val != second.val: return False
                stack.append((first.left, second.left))
                stack.append((first.right, second.right))
        return True
