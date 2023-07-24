from Trie import Trie
import re

class SpellChecker:
    def __init__(self):
        self.trie = Trie()

    def getNearestFourWords(self, word: str) -> list:
        """
        Returns the nearest four words to the given word in the dictionary.

        Args:
            word (str): The word for which to find the nearest four words.

        Returns:
            list: A list containing the nearest four words in lexicographic order.
        """
        return self.trie.findNearestWords(word)
    
    def storeDitionary(self, dict_path: str) -> None:
        """
        Reads words from a dictionary file and stores them in the Trie.

        Args:
            dict_path (str): The path to the dictionary file.
        """
        with open(dict_path, "r", errors="ignore") as f:
            words = f.readlines()
        
        # Remove non-alphabetic characters and create a word_list from the dictionary file.
        word_list = [re.sub(r"[^a-zA-Z]", "", word.strip()) for word in words]

        for word in word_list:
            self.trie.insert(word) 

    def insertWord(self, word: str) -> None:
        """
        Inserts a new word into the Trie.

        Args:
            word (str): The word to be inserted.
        """
        self.trie.insert(word)
        print(f"The word {word} added to the dictionary")