graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}


# The Algorithm
# Pick any node, visit the adjacent unvisited vertex, mark it as visited, display it,
# and insert it in a queue.
# If there are no remaining adjacent vertices left, remove the first vertex from the queue.
# Repeat step 1 and step 2 until the queue is empty or the desired node is found.
def bfs(graph, node):
    visited = []  # List to keep track of visited nodes.
    queue = []  # Initialize a queue
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s, end=" ")
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


bfs(graph, 'A')
