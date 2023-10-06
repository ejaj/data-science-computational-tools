from collections import defaultdict

documents = [
    "Deer Bear River Car Car River Deer Car Bear",
    "Deer Antelope Stream River Stream"
]


# Step 1: Map Phase
def map_phase(id, doc):
    word_list = doc.split()
    pairs = [(word, id) for word in word_list]
    return pairs


# Step 2: Reduce Phase
def reduce_phase(word, doc_ids):
    return word, doc_ids


# Initialize an inverted index dictionary
inverted_index = defaultdict(list)
for doc_id, document in enumerate(documents, 1):
    word_doc_pairs = map_phase(doc_id, document)
    for word, pair_id in word_doc_pairs:
        inverted_index[word].append(pair_id)

# Reduce Phase: Group document IDs by word
inverted_index = {
    word: list(set(doc_ids)) for word, doc_ids in inverted_index.items()
}

for word, doc_ids in inverted_index.items():
    print(f'({word}, {doc_ids})')
