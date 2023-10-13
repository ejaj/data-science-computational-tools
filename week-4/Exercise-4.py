import os

import mmh3
import numpy as np

from similarity import list_string_hash

q = 3  # length of shingle
k = 100  # number of minhashes
docs = {}  # dictionary mapping document id to document contents


def shingle(a_string, q, delimiter=' '):
    """

    Args:
        a_string:
        q:
        delimiter:

    Returns: list of unique shingles

    """
    all_shingles = []
    if delimiter != '':
        words_list = a_string.split(delimiter)
    else:
        words_list = a_string
    for i in range(len(words_list) - q + 1):
        all_shingles.append(delimiter.join(words_list[i:i + q]))
    return list(set(all_shingles))


def minhash(shingles_list, seed):
    """
    Args:
        shingles_list:
        seed:

    Returns:

    """
    minhash_value = None
    for shingle in shingles_list:
        hashcode = list_string_hash([shingle], seed)
        if minhash_value is None or hashcode < minhash_value:
            minhash_value = hashcode
    return minhash_value


def minhash2(shingles_list, k):
    """
    Args:
        shingles_list:
        k:

    Returns:

    """
    all_minhash = []
    for i in range(k):
        all_minhash.append(minhash(shingles_list, i))
    return all_minhash


def clean_text(a_string):
    output = a_string.replace('\n', '')
    output_list = output.split()
    output_list = [''.join(ch for ch in aWord if ch.isalnum()) for aWord in output_list]
    output_list = [s.lower() for s in output_list]
    output = ' '.join(output_list)
    return " ".join(output.split())


srcfolder = os.path.abspath('../data')
datafolder = os.path.join(srcfolder, "ats_corpus_small")  # change to ats_corpus for large data set

for file in os.listdir(datafolder):
    filepath = os.path.join(datafolder, file)
    f = open(filepath, 'r')
    docs[file] = f.read()
    docs[file] = clean_text(docs[file])
    print("read document " + file)
    f.close()


def signature(dict_docs, q=q, num_hashes=k):
    dict_signatures = {}
    total_texts = len(list(dict_docs.keys()))
    counter = 1
    for key, text in dict_docs.items():
        print(f'{counter}/{total_texts} - {key} - Processing...')
        doc_shingles = shingle(text, q)
        minhash_values = minhash2(doc_shingles, num_hashes)
        dict_signatures[key] = minhash_values
        counter += 1
    return dict_signatures


dict_signatures_docs = signature(docs)


# Exercise 5 - Jaccard Similarity
def jaccard(name1, name2, signatures_dict):
    """
    Jaccard Similarity
    Args:
        name1:
        name2:
        signatures_dict:

    Returns:

    """
    signatures_doc1 = np.array(signatures_dict[name1])
    signatures_doc2 = np.array(signatures_dict[name2])
    return len(np.intersect1d(signatures_doc1, signatures_doc2)) / len(np.union1d(signatures_doc1, signatures_doc2))


first_doc_key = list(docs.keys())[0]
second_doc_key = list(docs.keys())[1]
print(f'Jaccard similarity between {first_doc_key} and {second_doc_key}:',
      jaccard(first_doc_key, second_doc_key, dict_signatures_docs))


# Exercise 6 - Find Similar Items
def similar(signatures_dict, jaccard_threshold=0.6):
    """
    Find Similar Items
    Args:
        signatures_dict:
        jaccard_threshold:

    Returns:

    """
    list_keys = list(signatures_dict.keys())
    similar_items = {}
    for i in range(len(list_keys) - 1):
        for j in range(i + 1, len(list_keys)):
            similarity_score = jaccard(list_keys[i], list_keys[j], signatures_dict)
            if similarity_score >= jaccard_threshold:
                similar_items[(list_keys[i], list_keys[j])] = similarity_score
    return similar_items


found_similar_items = similar(dict_signatures_docs)
print('Found similar items:\n', found_similar_items)
# Exercise 7 - Locality-Sensitive Hashing
b, r = 20, 5
assert k == b * r


def lsh(signatures_dict, jaccard_threshold=0.6, seed=42):
    lsh_dict = {}
    for key, values in signatures_dict.items():
        blocks = np.split(np.array(values), b)
        blocks_hash_values = []
        for aBlock in blocks:
            blocks_hash_values.append(mmh3.hash(aBlock, seed))
        lsh_dict[key] = blocks_hash_values
    list_keys = list(lsh_dict.keys())
    similar_items = {}
    for i in range(len(list_keys) - 1):
        for j in range(i + 1, len(list_keys)):
            common_values = np.intersect1d(lsh_dict[list_keys[i]], lsh_dict[list_keys[j]])
            if len(common_values) > 0:
                # we found a candidate
                similarity_score = jaccard(list_keys[i], list_keys[j], signatures_dict)
                if similarity_score >= jaccard_threshold:
                    similar_items[(list_keys[i], list_keys[j])] = similarity_score
    return similar_items


found_similar_items_with_lsh = lsh(dict_signatures_docs)
print('Found similar items with LSH:\n', found_similar_items_with_lsh)
