📌 Spell Checker using Python

A simple yet effective spell-checking tool built in Python that identifies incorrectly spelled words in a text file by comparing them against a standard English dictionary.

🚀 Features
Reads and processes text files (readme.txt.txt)
Uses a large English word dataset (english_words)
Cleans input using regular expressions
Detects and prints misspelled words
Custom word support (e.g., names, domains like hardik, gmail, com)

🛠️ Tech Stack
Python 🐍
re (Regular Expressions)
english-words library

⚙️ How It Works
Loads a predefined English dictionary.
Reads input text and converts it to lowercase.
Removes special characters using regex.
Splits the text into words.
Compares each word with the dictionary + custom word list.
Prints words that are not found (i.e., misspelled).

🎯 Future Improvements
Suggest correct spellings (like autocorrect)
GUI interface
Support for multiple languages
Real-time spell checking
