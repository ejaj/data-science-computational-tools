from similarity import list_string_hash


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


ex_string, q = 'i want to go home do you want to', 2
ex_shingles = shingle(ex_string, q)
print(f'MinHash of {ex_shingles}:', minhash(ex_shingles, 42))
k = 10
print(f'MinHash of {ex_shingles} with k = {k}:\n', minhash2(ex_shingles, k))
