from queue import PriorityQueue
from typing import List


class ListNode:
    """Definition for Singly-Linked List"""
    def __init__(self, x: int):
        self.val = x
        self.next = None

    def __eq__(self, other):
        return self.val == other.val

    def __lt__(self, other):
        return self.val < other.val

    def __gt__(self, other):
        return self.val > other.val


def merge_k_lists(lists: List[ListNode]) -> ListNode:
    """Compare every k nodes (head of every linked list) and get the node with
    the smallest value. Optimize the comparison process by priority queue"""
    head = point = ListNode(0)
    q = PriorityQueue()

    for l in lists:
        if l:
            q.put((l.val, l))

    while not q.empty():
        val, node = q.get()
        point.next = ListNode(val)
        point = point.next
        node = node.next
        if node:
            q.put((node.val, node))

    return head.next


def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    """Merge with Divide And Conquer
    Time complexity : O(N\log k)O(Nlogk) where k is the number of Linked Lists.
    We can merge two sorted linked list in O(n) time where n is the total number of nodes in two lists.
    Sum up the merge process and we can get: O(Nlog k)O(∑i=1log2kN)=O(Nlogk)
    Space complexity : O(1)
    We can merge two sorted linked lists in O(1) space.
    """
    K = len(lists)
    interval = 1

    while interval < K:
        for i in range(0, K - interval, interval * 2):
            lists[i] = self.merge2Lists(lists[i], lists[i + interval])
        interval *= 2

    return lists[0] if K > 0 else lists


def merge2Lists(l1: ListNode, l2: ListNode) -> ListNode:
    head = point = ListNode(0)

    while l1 and l2:
        if l1.val <= l2.val:
            point.next = l1
            l1 = l1.next
        else:
            point.next = l2
            l2 = l1
            l1 = point.next.next
        point = point.next

    if not l1:
        point.next=l2
    else:
        point.next=l1

    return head.next
