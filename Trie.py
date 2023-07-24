class Node():
    def __init__(self):
        self.children = [False for i in range(26)]
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        self.root = self.getNode()
    
    def getNode(self) -> Node:
        return Node()

    def _charToIdx(self, c: str) -> int:
        """
        Returns the index of the character in the English alphabet (0-indexed).

        Args:
            c (str): The input character (lowercase or uppercase).

        Raises:
            ValueError: If the input is not a single letter.

        Returns:
            int: The index of the character in the English alphabet (0 for 'a' - 25 for 'z').
        """
        if len(c) != 1 or not c.isalpha():
            raise ValueError(f"Got{c}, input must be a single letter")

        return ord(c.lower()) - ord('a')
    
    def _index_to_char(self, index: int) -> str:
        """
        Returns the character corresponding to the given index in the English alphabet (0-indexed).

        Args:
            index (int): The index of the character (0 for 'a' - 25 for 'z').

        Returns:
            str: The character in the English alphabet corresponding to the given index.
            
        Raises:
            ValueError: If the input index is out of range (not between 0 and 25).
        """
        if not 0 <= index <= 25:
            raise ValueError("Index must be between 0 and 25")

        return chr(ord('a') + index)
    
    def findNearestWords(self, word: str) -> list:
        """
        Returns the nearest four words in the dictionary from a given word
        (two words before and two words after the given word in lexicographic order).
        if the given word exists in the dictionary, the function returns a list contains only that word.

        Args:
            word (str): The word for which to find the nearest words.

        Raises:
            IndexError: Raised if the index of the character is out of range.

        Returns:
            list: A list containing the nearest four words in lexicographic order.
        """
        current_node = self.root
        for char in word:
            c_idx = self._charToIdx(char)
            if c_idx > 25 or c_idx < 0:
                raise IndexError(f'list index out of range, c_idx={c_idx}')
            if not current_node.children[c_idx]:
                return self._findNearestWordsFromNode(current_node, word)
            
            current_node = current_node.children[c_idx]
        if current_node.isEndOfWord:
            return [word]
        else:
            return self._findNearestWordsFromNode(current_node, word)

    def _findNearestUpcomingWords(self, node: Node, word: str, word_list: list = []) -> list:
        """
        Recursively finds the nearest upcoming words in the Trie from a specific node.

        Args:
            node (Node): The current Trie node from which to search for upcoming words.
            word (str): The current word formed up to the given node in the Trie.
            word_list (list, optional): A list to store the nearest upcoming words. Defaults to [].

        Returns:
            list: A list containing the nearest upcoming words in lexicographic order.
        """
        if len(word_list) >= 2:
            return word_list

        if node.isEndOfWord:
            word_list.append(word)

        for i, child in enumerate(node.children):
            if child:
                char = self._index_to_char(i)
                self._findNearestUpcomingWords(child, word + char, word_list)
        return word_list

    def _findNearestWordsFromNode(self, current_node: Node, word: str) -> list:
        """
        Finds the nearest words in lexicographic order, both before and after a given node in the Trie.

        Args:
            current_node (Node): The current Trie node from which to search for upcoming words.
            word (str): _description_

        Returns:
            list: _description_
        """
        two_words_after = self._findNearestUpcomingWords(current_node, word)
        two_words_before = []
        return two_words_before + two_words_after

    def insert(self, word: str) -> None:
        """
        Inserts a word into the Trie data structure.

        Args:
            word (str): The word to be inserted into the Trie.
        """
        if len(word) > 0:
            current_node = self.root
            for char in word:
                c_idx = self._charToIdx(char)
                if c_idx > 25 or c_idx < 0:
                    raise IndexError(f'list index out of range, c_idx={c_idx}')
                if not current_node.children[c_idx]:
                    current_node.children[c_idx] = self.getNode()
                current_node = current_node.children[c_idx]
            
            current_node.isEndOfWord = True