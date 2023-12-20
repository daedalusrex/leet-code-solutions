

def max_vowels_mostly_generated(s: str, k: int) -> int:
    """
    Calculates the maximum number of vowels in a substring of length k in a given string s.
    Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

    Parameters:
        s (str): The input string.
        k (int): The length of the substring.

    Returns:
        int: The maximum number of vowels in a substring of length k.
    """
    vowels = {'a', 'e', 'i', 'o', 'u'}
    max_vowel = 0
    i_range = range(len(s) - k + 1) if len(s) >= k else range(1)
    for i in i_range:
        curr_vowels = 0
        j_range = range(i, i + k) if i + k < len(s) else range(i, len(s))
        for j in j_range:
            if s[j] in vowels:
                curr_vowels += 1
        max_vowel = max(max_vowel, curr_vowels)
    return max_vowel

