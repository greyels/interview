import heapq
from typing import List


class Solution:
    # MaxHeap usage -> O(nlog(k)), because heapq.pop and heapq.push give O(log(k))
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            # Because we need a MaxHeap (multiply on -1)
            dist = -(x * x + y * y)
            if len(heap) == k:
                heapq.heappushpop(heap, (dist, x, y))
            else:
                heapq.heappush(heap, (dist, x, y))
        return [[x, y] for (dist, x, y) in heap]

    # Sorting -> O(nlog(n))
    def kClosestSorted(self, points: List[List[int]], k: int) -> List[List[int]]:
        return sorted(points, key=lambda x: (x[0] ** 2 + x[1] ** 2))[:k]
