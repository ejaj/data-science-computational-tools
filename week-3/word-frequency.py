from collections import Counter

document = "Deer Bear River Car Car River Deer Car Bear"
# Step 1: Map Phase
# Split the document into words and create key-value pairs where the key is the word and the value is 1.
words = document.split()
word_counts = Counter(words)

# Step 2: Reduce Phase
# Sum the values (counts) for each unique key (word).
word_frequency = [(word, count) for word, count in word_counts.items()]
# Print the word frequencies
for word, count in word_frequency:
    print(f'({word}, {count})')
