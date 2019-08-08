"""
PE013 Large sum

Work out the first ten digits of the sum of the following one-hundred 50-digit numbers in pe0013_data.txt
"""


def first_ten_digits(data):
    """returns the first ten digits of the sum of big numbers

    data: txt file name in string
    """

    with open(data) as raw:
        numbers = raw.readlines()

    return str(sum(int(i) for i in numbers))[:10]


if __name__ == "__main__":
    print(first_ten_digits("p013_data.txt"))
    # >>> 5537376230
    # passed
