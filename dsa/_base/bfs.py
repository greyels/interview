from collections import deque


def bfs(graph, start):
    visited = set()  # To keep track of visited nodes
    queue = deque([start])  # Initialize queue with start node

    while queue:
        node = queue.popleft()  # Dequeue a node
        if node not in visited:
            print(node, end=" ")  # Process the node
            visited.add(node)  # Mark as visited

            # Add unvisited neighbors to queue
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)


# Example graph as adjacency list
#        1
#       / \
#      2   3
#     / \
#    4   5
graph = {
    1: [2, 3, 4],
    2: [5, 6],
    3: [7],
    4: [],
    5: [],
    6: [7],
    7: []
}
bfs(graph, 1)
print()


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def bfs_tree(root):
    if not root:
        return
    queue = deque([root])

    while queue:
        node = queue.popleft()
        print(node.val, end=" ")

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


# Example Binary Tree:
#        1
#       / \
#      2   3
#     / \
#    4   5
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
bfs_tree(root)
