# Create a simple text analyzer the counts words,characters,and sentences in a given text. 

text = """Python is a powerful programming language. It's easy to learn and versatile! You can use Python for web development, data science, and automation. The syntax is clean and readable. This makes Python perfect for begineers and experts alike."""

word_count = len(text.split()) # this will count the number of words in the string 'text' by splitting the string into a list of words and then counting the length of that list

character_count = len(text) # this will count the number of characters in the string 'text' by using the len() function which returns the number of characters in a string, including spaces and punctuation

sentence_count = text.count('.') + text.count('!') + text.count('?') # this will count the number of sentences in the string 'text' by counting the number of periods, exclamation marks, and question marks

print(f"Analyzing the text: \n{text}\n")
print(f"Word Count: {word_count} words")
print(f"Character Count: {character_count} characters")
print(f"Sentence Count: {sentence_count} sentences")


