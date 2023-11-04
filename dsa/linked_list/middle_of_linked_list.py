from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head
        ll_track = {}
        index = 0
        next = head
        while next:
            index += 1
            ll_track[index] = next
            next = next.next
        return ll_track[index // 2 + 1]

    def middleNodeTwoPointers(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow
