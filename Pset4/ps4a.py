# Problem Set 4A
# Name: Yuhan Liu
# Collaborators:
# Time Spent: 50 minutes

def get_permutations(sequence):
    """
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    # >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    """
    permutations = []
    list_seq = list(sequence)

    if len(sequence) == 1:
        permutations.append(sequence)
        return permutations

    letter = list_seq.pop(0)
    subpermutations = get_permutations(''.join(list_seq))

    if subpermutations:
        for x in subpermutations:
            list_x = list(x)
            index = x.find(letter)
            if index < 0:
                for i in range(len(list_x) + 1):
                    list_x.insert(i, letter)
                    permutations.append(''.join(list_x))
                    list_x.remove(letter)
            else:
                for i in range(len(list_x)):
                    if i == index + 1:
                        continue
                    list_x.insert(i, letter)
                    permutations.append(''.join(list_x))
                    list_x.remove(letter)

    return permutations


def get_permutations2(sequence):
    if len(sequence) == 1:
        return [sequence]
    elif len(sequence) == 2:
        return [sequence, sequence[::-1]]
    else:
        seq_copy = sequence[:]
        perm_list = []
        for char in sequence:
            perm_list += [char + x for x in get_permutations(seq_copy.replace(char, ''))]
        return perm_list


if __name__ == '__main__':
    #   EXAMPLE
    #   example_input = 'abc'
    #   print('Input:', example_input)
    #   print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    #   print('Actual Output:', get_permutations(example_input))
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))
    print('----------')

    example_input = 'aba'
    print('Input:', example_input)
    print('Expected Output:', ['aba', 'aab', 'baa'])
    print('Actual Output:', get_permutations(example_input))
    print('----------')

    example_input = 'aaa'
    print('Input:', example_input)
    print('Expected Output:', ['aaa'])
    print('Actual Output:', get_permutations(example_input))
    print('----------')
    #    # Put three example test cases here (for your sanity, limit your inputs
    #    to be three characters or fewer as you will have n! permutations for a
    #    sequence of length n)
