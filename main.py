import re

from english_words import get_english_words_set
dictionary = get_english_words_set(['web2'], lower=True)
my_dictionary = {"hardik", "bindal", "gmail", "com"}
print(f"Total Words: {len(dictionary)}")


with open("words.txt", "r") as final:
 content1 = final.read().lower()
 ready = content1.split()


with open("readme.txt.txt", "r") as file:
 content = file.read().lower()
 content = re.sub(r'[^a-z\s]', ' ', content)

words_that_are_in_file = content.split()


for word in words_that_are_in_file:
 if word not in ready:
  print(f"Spelled Incorrectly: {word}")