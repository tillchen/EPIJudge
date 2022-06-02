from typing import List

from test_framework import generic_test
from collections import Counter
from collections import defaultdict


def find_all_substrings(s: str, words: List[str]) -> List[int]:
    word_to_frequency = Counter(words)
    unit = len(words[0])
    def match_all_words(start_index: int) -> bool:
        current_word_to_frequency = defaultdict(int)
        for i in range(start_index, start_index + unit * len(words), unit):
            word = s[i:i+unit]
            if word not in word_to_frequency:
                return False
            current_word_to_frequency[word] += 1
            if current_word_to_frequency[word] > word_to_frequency[word]:
                return False
        return True
    return [i for i in range(len(s) - unit * len(words) + 1) if match_all_words(i)]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'string_decompositions_into_dictionary_words.py',
            'string_decompositions_into_dictionary_words.tsv',
            find_all_substrings))
