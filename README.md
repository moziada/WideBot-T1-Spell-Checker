# Spell-Checker

This project implements a simple spell checker using a Trie data structure. The spell checker class takes a dictionary as input and provides three main operations:

* Store Dictionary: The spell checker stores the given dictionary in a Trie data structure for efficient word storage and retrieval.

* Find Nearest Words: Given an input word, the spell checker returns the nearest four words (two words before and two words after) in lexicographic order if the input word is not found in the dictionary.

* Insert Word: The spell checker allows the insertion of a new word into the dictionary using the Trie data structure.

## Files

The project consists of the following three Python files:

* `Trie.py`: This file contains the implementation of the Trie data structure used for word storage and retrieval.

* `SpellChecker.py`: This file contains the implementation of the SpellChecker class that uses the Trie data structure to perform spell checking operations.

* `main.py`: This file serves as the entry point of the project, where you can interact with the SpellChecker class and perform various spell checking operations.

## How to Use

1. Create a dictionary file (e.g., `dictionary.txt`) containing a list of words, one word per line, and place it into `Data` directory.

2. In the main.py file, specify the path to the dictionary file using the DICTIONARY_PATH variable.

3. Run the main.py file to use the spell checker. The script will read the dictionary file, store it in the Trie data structure.

## Operations and Complexity

### Dictionary Space Complexity

O(N * L), where N is the number of words in the dictionary, and L is the average length of a word.

### Find Nearest Words

**Time Complexity**: O(L), where L is the length of the input word.

### Insert Word:

**Time Complexity**: O(L), where L is the length of the input word.

## Example Usage

```python

from SpellChecker import SpellChecker

# Define the path to the dictionary file
DICTIONARY_PATH = "Data/dictionary.txt"

# Create an instance of the SpellChecker class
spell_checker = SpellChecker()
spell_checker.storeDitionary(DICTIONARY_PATH)

# Find the nearest four words to "eleph" and print the result
print(spell_checker.getNearestFourWords("eleph"))
# >> ['elephant', 'elephantiasis']

# Insert the word "MohamedZiada" into the Trie
spell_checker.insertWord("MohamedZiada")
# >> The word "MohamedZiada" added to the dictionary
```
