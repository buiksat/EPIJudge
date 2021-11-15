from test_framework import generic_test
dp = dict()

def levenshtein_distance(A: str, B: str) -> int:
    # TODO - you fill in here.

    if not A:
        return len(B)
    if not B:
        return len(A)

    if A[0] == B[0]:
        return check_dp(A[1:], B[1:])
    else:
        opt1 = check_dp(A, B[1:])
        opt2 = check_dp(A[1:], B)
        opt3 = check_dp(A[1:], B[1:])
        return  1 + min(opt1, opt2, opt3)


def check_dp(A: str, B: str):
    key = A + "|" + B
    if key in dp.keys():
        return dp[key]
    else:
        dp[key] = levenshtein_distance(A, B)
        return dp[key]






if __name__ == '__main__':

    exit(
        generic_test.generic_test_main('levenshtein_distance.py',
                                       'levenshtein_distance.tsv',
                                       levenshtein_distance))
                                       

