from test_framework import generic_test


def compute_binomial_coefficient(n: int, k: int) -> int:
    # TODO - you fill in here.
    if n == k:
        return 1
    dp = dict()
    dp[(1,0)] = 1
    dp[(1,1)] = 1
    dp[(2,1)] = 2
    for i in range(2,k+1):
        dp[(i + 1,i)] = (i+1)*dp[(i,i -1)]/i
    for j in range(k+1,n):
        dp[(j + 1, k)] = (j+1) * dp[(j, k)] / (j+1 - k)

    return int(dp[(n,k)])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('binomial_coefficients.py',
                                       'binomial_coefficients.tsv',
                                       compute_binomial_coefficient))
