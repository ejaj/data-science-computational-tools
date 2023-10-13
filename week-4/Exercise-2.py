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


ex_string, q = 'abcdabd', 2
ex_shingles = shingle(ex_string, q, delimiter='')
print('Initial string:', ex_string)
print(f'>> Shingles with q = {q} :', ex_shingles)

# Example from the HINT
ex_string, q = 'i want to go home do you want to', 2
ex_shingles = shingle(ex_string, q)
assert len(ex_shingles) == 7
print('\nInitial string:', ex_string)
print(f'>> Shingles with q = {q} :', ex_shingles)
