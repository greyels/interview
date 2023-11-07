def depth_first_search(graph, start_node):
    def dfs(graph, node, visited):
        print(f"we are at {node}")
        if node not in visited:
            print(node)  # Process the node (you can modify this part)
            visited.add(node)  # Mark the node as visited
            for neighbor in graph[node]:
                dfs(graph, neighbor, visited)
    return dfs(graph, start_node, set())


# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

depth_first_search(graph, 'A')
