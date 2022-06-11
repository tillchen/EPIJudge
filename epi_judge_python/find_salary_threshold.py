from typing import List

from test_framework import generic_test


# Total = sum(payrolls_below_cap) + num_of_capped_payrolls * cap
# cap = (Total - sum(payrolls_below_cap)) / num_of_capped_ payrolls
def find_salary_cap(target_payroll: int, current_salaries: List[int]) -> float:
    current_salaries.sort()
    sum_of_payrolls_below_cap = 0
    for i, salary in enumerate(current_salaries):
        num_of_capped_payrolls = len(current_salaries) - i
        if sum_of_payrolls_below_cap + num_of_capped_payrolls * salary >= target_payroll:
            return (target_payroll - sum_of_payrolls_below_cap) / num_of_capped_payrolls
        sum_of_payrolls_below_cap += salary
    return -1.0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('find_salary_threshold.py',
                                       'find_salary_threshold.tsv',
                                       find_salary_cap))
