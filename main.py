from SpellChecker import SpellChecker

# Define the path to the dictionary file
DICTIONARY_PATH = "Data/dictionary.txt"

# Create an instance of the SpellChecker class
spell_checker = SpellChecker()
spell_checker.storeDitionary(DICTIONARY_PATH)

# Find the nearest four words to "eleph" and print the result
print(spell_checker.getNearestFourWords("eleph"))

# Insert the word "MohamedZiada" into the Trie
spell_checker.insertWord("MohamedZiada")



