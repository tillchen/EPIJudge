from typing import List

from test_framework import generic_test, test_utils


def generate_balanced_parentheses(num_pairs: int) -> List[str]:
    result = []
    def helper(num_of_left_parens_needed: int, num_of_right_parens_needed: int, valid_prefix: str):
        if num_of_right_parens_needed == 0:
            result.append(valid_prefix)
            return
        if num_of_left_parens_needed > 0:
            helper(num_of_left_parens_needed - 1, num_of_right_parens_needed, valid_prefix + '(')
        if num_of_left_parens_needed < num_of_right_parens_needed:
            helper(num_of_left_parens_needed, num_of_right_parens_needed - 1, valid_prefix + ')')
    helper(num_pairs, num_pairs, '')
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('enumerate_balanced_parentheses.py',
                                       'enumerate_balanced_parentheses.tsv',
                                       generate_balanced_parentheses,
                                       test_utils.unordered_compare))
