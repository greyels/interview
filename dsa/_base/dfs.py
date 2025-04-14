def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = set()
    visited.add(node)
    print(node, end=" ")  # Process node

    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)


def dfs_iterative(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=" ")  # Process node
            visited.add(node)
            stack.extend(reversed(graph.get(node, [])))  # Push neighbors


graph = {
    1: [2, 3, 4],
    2: [5, 6],
    3: [7],
    4: [],
    5: [],
    6: [7],
    7: []
}
dfs_recursive(graph, 1)
print()
dfs_iterative(graph, 1)
print()


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# Recursive DFS (Preorder)
def dfs_tree(node):
    if node is None:
        return
    print(node.val, end=" ")  # Process node
    dfs_tree(node.left)
    dfs_tree(node.right)


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
