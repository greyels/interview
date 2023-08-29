def dfs(graph, node, visited):
    if node not in visited:
        print(node)  # Process the node (you can modify this part)
        visited.add(node)  # Mark the node as visited
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

start_node = 'A'
visited_nodes = set()
print("Depth-First Traversal:")
dfs(graph, start_node, visited_nodes)
