import heapq
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


def merge(*iterables):
    """Merge multiple sorted inputs into a single sorted output.

    Similar to sorted(itertools.chain(*iterables)) but returns a generator,
    does not pull the data into memory all at once, and assumes that each of
    the input streams is already sorted (smallest to largest).

    list(merge([1,3,5,7], [0,2,4,8], [5,10,15,20], [], [25]))
    [0, 1, 2, 3, 4, 5, 5, 7, 8, 10, 15, 20, 25]
    """
    _heappop, _heapreplace, _StopIteration = heapq.heappop, heapq.heapreplace, StopIteration

    h = []
    h_append = h.append
    for itnum, it in enumerate(map(iter, iterables)):
        try:
            next = it.next
            h_append([next(), itnum, next])
        except _StopIteration:
            pass
    heapq.heapify(h)

    while 1:
        try:
            while 1:
                v, itnum, next = s = h[0]   # raises IndexError when h is empty
                yield v
                s[0] = next()               # raises StopIteration when exhausted
                _heapreplace(h, s)          # restore heap condition
        except _StopIteration:
            _heappop(h)                     # remove empty iterator
        except IndexError:
            return


def merge(*subsequences):
    # prepare a priority queue whose items are pairs of the form
    # (current-value, iterator), one each per (non-empty) subsequence
    heap = [  ]
    for subseq in subsequences:
        iterator = iter(subseq)
        for current_value in iterator:
            # subseq is not empty, therefore add this subseq's pair
            # (current-value, iterator) to the list
            heap.append((current_value, iterator))
            break
    # make the priority queue into a heap
    heapq.heapify(heap)
    while heap:
        # get and yield lowest current value (and corresponding iterator)
        current_value, iterator = heap[0]
        yield current_value
        for current_value in iterator:
            # subseq is not finished, therefore add this subseq's pair
            # (current-value, iterator) back into the priority queue
            heapq.heapreplace(heap, (current_value, iterator))
            break
        else:
            # subseq has been exhausted, therefore remove it from the queue
            heapq.heappop(heap)
