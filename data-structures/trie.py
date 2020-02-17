from typing import Union


class TrieNode():
    def __init__(self):
        """Initialize TrieNode for building Trie"""
        self._children = [None] * 26
        self.is_end = False

    def __contains__(self, char):
        return self._children[self._char_idx(char)] is not None

    @staticmethod
    def _char_idx(char):
        return ord(char) - ord('a')

    def put(self, char, node):
        self._children[self._char_idx(char)] = node

    def get(self, char):
        return self._children[self._char_idx(char)]


class Trie:
    def __init__(self):
        """Initialize Trie data structure here."""
        self._root = TrieNode()

    @staticmethod
    def _char_idx(char: str) -> int:
        """Returns char index"""
        return ord(char) - ord('a')

    def insert(self, word: str) -> None:
        """Inserts a word into the trie."""
        node = self._root
        for char in word:
            if char not in node:
                node.put(char, TrieNode())
            node = node.get(char)
        node.is_end = True

    def search(self, word: str) -> bool:
        """Returns if the word is in the trie."""
        node = self.search_prefix(word)
        return node is not None and node.is_end

    def search_prefix(self, word) -> Union[None, TrieNode]:
        node = self._root
        for char in word:
            if char in node:
                node = node.get(char)
            else:
                return None
        return node

    def starts_with(self, prefix: str) -> bool:
        """Returns if there is any word in the trie that starts with the given prefix."""
        node = self.search_prefix(prefix)
        return node is not None


# Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
