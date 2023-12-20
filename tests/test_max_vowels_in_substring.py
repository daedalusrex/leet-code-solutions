import pytest

from questions.max_vowels_in_substring import max_vowels

vowel_test_cases = [
    # Testing when the input string has no vowels
    ("", 3, 0),
    # Testing when the input string has fewer vowels than k
    ("hello", 7, 2),
    # Testing when the input string has more vowels than k
    ("hello", 2, 1),
    # Testing when the input string has exactly k vowels
    ("hello", 3, 1),
    # Testing when the input string has multiple substrings with maximum vowels
    ("aeiouaeiou", 3, 3),
    # Testing when the input string has multiple substrings with different maximum vowels
    ("aeiouaeiou", 2, 2),
    # Testing when the input string has only vowels
    ("aeiou", 3, 3),
    # Testing when the input string has only consonants
    ("bcdfgh", 2, 0),
]


@pytest.mark.parametrize("s,k,expected", vowel_test_cases)
def test_max_vowels(s, k, expected):
    assert max_vowels(s, k) == expected

