class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def getIntersectionNode(headA: ListNode, headB: ListNode) -> ListNode:
    nodes_set = set()
    # Traverse the first linked list and store all its nodes in the set
    while headA:
        nodes_set.add(headA)
        headA = headA.next
    # Traverse the second linked list and check if each node is already in the set
    while headB:
        if headB in nodes_set:
            return headB
        headB = headB.next
    # No intersection node found
    return None

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNodeMy(self, headA: ListNode, headB:ListNode) -> ListNode:
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        ll_a_set = set()
        next_node = headA

        while(next_node):
            ll_a_set.add(next_node)
            next_node = next_node.next

        next_node = headB
        while(next_node):
            if next_node in ll_a_set:
                return next_node
            next_node = next_node.next

        return None

def createLinkedList(vals):
    if not vals:
        return None
    # Create the first node
    head = ListNode(vals[0])
    current = head
    # Create the remaining nodes and link them together
    for val in vals[1:]:
        current.next = ListNode(val)
        current = current.next
    return head
