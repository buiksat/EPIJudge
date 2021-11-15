from test_framework import generic_test


def number_of_ways(n: int, m: int) -> int:
    # TODO - you fill in here.
    dp = [[0] * (m + 1) for _ in range(n)]
    dp[0] = [1] * (m + 1)

    for i in range(1,n):
        for j in range(1,m + 1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[-1][-1]


if __name__ == '__main__':
    # print(number_of_ways(5,5))
    exit(
        generic_test.generic_test_main('number_of_traversals_matrix.py',
                                       'number_of_traversals_matrix.tsv',
                                       number_of_ways))
