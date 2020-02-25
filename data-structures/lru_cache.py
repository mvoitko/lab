from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Node:
    """Doubly Linked List (DLL) Node class to store value to be cached"""
    key: int = None
    val: int = None
    prev: Node = None
    next_: Node = None


class LRUCache:
    """LRU Cache implemented with Doubly Linked List with sentinels and Hash Map"""
    def __init__(self, capacity: int) -> None:
        """Create DLL with sentinels technique"""
        self.router = dict()
        self.capacity = capacity
        self.head = LRUCache.Node()
        self.head.next_ = self.head
        self.tail = self.head.next_
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        """Get item from LRU cache by O(1) time"""
        node = self.router.get(key, None)
        if node:
            self._remove(node)
            self._add(node)
            return node.val
        return -1


    def put(self, key: int, value: int) -> None:
        """Put item in LRU cache with O(1) by time"""
        # Check if such value is already in cache
        node = self.router.get(key, None)
        if node:
            self._remove(node)
            node.val = value
            self._add(node)
            return

        if self._reach_capacity():
            last_node = self.tail.prev
            self._remove(last_node)
            self.router.pop(last_node.key)

        new_node = LRUCache.Node(key, value)
        self._add(new_node)
        self.router[key] = new_node

    def _reach_capacity(self) -> bool:
        return len(self.router) == self.capacity

    def _remove(self, node: Node) -> None:
        """Remove node from DLL"""
        prev = node.prev
        next_ = node.next_
        prev.next_ = next_
        next_.prev = prev

    def _add(self, node: Node) -> None:
        """Add Node to DLL"""
        cur = self.head.next_
        self.head.next_ = node
        node.prev = self.head
        node.next_ = cur
        cur.prev = node
