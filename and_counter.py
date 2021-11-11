paragraph = "According to Global Witness, IETA is backed by many major oil companies who promote offsetting and carbon trading as a way of allowing them to continue extracting oil and gas."

import string
table = str.maketrans('', '', string.punctuation)
words = paragraph.split() ##Break paragraph into list of words
stripped = [w.translate(table) for w in words] ##Remove punctuation from list of words
stripped = [word.lower() for word in stripped] ## Convert all words to lower case
words = stripped

##Intialise counter to 0
counter = 0

##Check for words equal to "and" and increment counter
for word in words:
    if word == "and":
        counter += 1

print(words)

print("Number of ands:", counter)
