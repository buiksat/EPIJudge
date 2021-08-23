from test_framework import generic_test


def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    # TODO - you fill in here.
    m = {10: "A", 11: "B", 12 : "C", 13: "D", 14: "E", 15 : "F"}
    n = {"0":0, "1": 1, "2":2, "3": 3, "4": 4, "5":5, "6":6, "7":7, "8":8,  "9":9,
        "A":10, "B":11, "C":12, "D":13, "E":14, "F":15}
    neg = False
    if num_as_string[0] == "-":
        neg = True
        num_as_string = num_as_string[1:]
    # convert to 10
    num_10 = 0;
    length = len(num_as_string)
    for s in num_as_string:
        num_10 += n[s] * pow(b1, length - 1)
        length -= 1

    # convert to base b2
    #answer = []
    answer = ""
    while (True):
        num_b2 = num_10 % b2
        if num_b2 > 9:
            #answer.append(m[num_b2])
            answer = m[num_b2] + answer
        else:
            #answer.append(str(num_b2))
            answer = str(num_b2) + answer
        num_10 = num_10 // b2
        if not num_10:
            break

    #answer = answer[::-1]
    #answer = "".join(answer)
    if neg:
        return "-" + answer
    return answer






if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('convert_base.py', 'convert_base.tsv',
                                       convert_base))
