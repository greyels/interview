from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        queue = [node]
        mapping = {node: Node(node.val, [])}
        while queue:
            cur = queue.pop(0)
            for neighbor in cur.neighbors:
                if neighbor not in mapping:
                    mapping[neighbor] = Node(neighbor.val, [])
                    queue.append(neighbor)
                mapping[cur].neighbors.append(mapping[neighbor])
        return mapping[node]
