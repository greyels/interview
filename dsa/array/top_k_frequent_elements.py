import heapq
from collections import defaultdict
from typing import List


class Solution:

    # O=nlog(k) with heapq/heapify
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        heap = [(-freq, num) for num, freq in count.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for i in range(k)]

     # O=nlog(k) with heapq (better when k << n)
    def topKFrequent1(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        heap = []
        for num in count.keys():
            heapq.heappush(heap, (count[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        return [item[1] for item in heap]

    # O=nlog(n) with sorting
    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        return sorted(count, key=count.get, reverse=True)[:k]

    # O=nlog(k) with heapq (better when k << n)
    def topKFrequent3(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        return heapq.nlargest(k, count, count.get)
