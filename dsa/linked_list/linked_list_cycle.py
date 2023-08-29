# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node = head
        visited = set()
        while node:
            if node in visited:
                return True
            visited.add(node)
            node = node.next
        return False
