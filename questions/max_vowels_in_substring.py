

def max_vowels(s: str, k: int) -> int:
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
    for i in range(len(s) - k + 1):
        curr_vowels = 0
        for j in range(i, i + k):
            if s[j] in vowels:
                curr_vowels += 1
        max_vowel = max(max_vowel, curr_vowels)
    return max_vowel

