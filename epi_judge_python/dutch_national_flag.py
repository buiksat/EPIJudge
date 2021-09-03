import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)


def swap(A, i, j):
    tmp = A[i]
    A[i] = A[j]
    A[j] = tmp
    return

def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:

    # TODO - you fill in here.
    left = 0
    pivot_left = pivot_right = pivot_index
    right = len(A) - 1
    pivot = A[pivot_index]
    while left < pivot_left:
        if A[left] > pivot:
            swap(A, left, right)
            right += 1
        elif A[left] < pivot:
            left += 1
        else:
            swap(A, left, pivot_left - 1)
            pivot_left -= 1

    while right > pivot_right:
        if A[right] > pivot:
            right -= 1
        elif A[right] < pivot:
            swap(A, pivot_right + 1, right)
            swap(A, pivot_right + 1, pivot_left)
            pivot_left +=1
            pivot_right += 1
        else:
            swap(A, pivot_right + 1, right)
            pivot_right += 1
    return


@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure('Some elements are missing from original array')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('dutch_national_flag.py',
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))
