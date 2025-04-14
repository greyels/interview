class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# Recursive DFS (Preorder)
def dfs_tree(root):
    if root is None:
        return
    print(root.val, end=" ")  # Process node
    dfs_tree(root.left)
    dfs_tree(root.right)


# Example Binary Tree:
#        1
#       / \
#      2   3
#     / \
#    4   5
#   / \
#  6   7
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.left.left = TreeNode(6)
root.left.left.right = TreeNode(7)

dfs_tree(root)
