import os
from pathlib import Path
import bisect
from fractions import Fraction


def fisl(elem: int, sorted_list: list[int]):
    # https://docs.python.org/3/library/bisect.html
    "Locate the leftmost value exactly equal to x"
    i = bisect.bisect_left(sorted_list, elem)
    if i != len(sorted_list) and sorted_list[i] == elem:
        return i
    return -1


def gcd(a: int, b: int):
    """
    Returns the gcd of its inputs times the sign of b if b is nonzero,
    and times the sign of a if b is 0.
    """
    while b != 0:
        a, b = b, a % b
    return a


def gcd2(a: int, b: int):
    if a == b:
        return a

    # GCD(0, b) == b; GCD(a, 0) == a,
    # GCD(0, 0) == 0
    if a == 0:
        return b

    if b == 0:
        return a

    # look for factors of 2
    # a is even
    if (~a & 1) == 1:
        # b is odd
        if (b & 1) == 1:
            return gcd(a >> 1, b)
        else:
            # both a and b are even
            return gcd(a >> 1, b >> 1) << 1

    # a is odd, b is even
    if (~b & 1) == 1:
        return gcd(a, b >> 1)

    # reduce larger number
    if a > b:
        return gcd((a - b) >> 1, b)

    return gcd((b - a) >> 1, a)


def parser(
    path: os.PathLike[str],
) -> tuple[list[int], list[int], int]:
    """
    Parse input from file into an array and kernel
    """
    with open(path, "r") as f:
        size = int(f.readline().strip())
        h1_classes = [
            int(x) for x in f.readline().strip().split(sep=" ")
        ]  # classes choosen by first human
        h2_classes = [
            int(x) for x in f.readline().strip().split(sep=" ")
        ]  # classes choosen by second human
    return h1_classes, h2_classes, size


def similarity(h1_classes: list[int], h2_classes: list[int], size: int) -> Fraction:
    """
    Compute similarity metric from task 551.
    """
    """
    Compute similarity metric from task 551.
    """
    sum = 0
    h1_dict: list[list[int]] = [
        [] for _ in range(size)
    ]  # [[]]*size#defaultdict(lambda: [])
    h2_dict: list[list[int]] = [[] for _ in range(size)]  # defaultdict(lambda: [])
    # sm1_dict: dict[tuple[int, int], tuple[int, int]] = defaultdict(lambda: (0, 0))
    # sm2_dict: dict[tuple[int, int], tuple[int, int]] = defaultdict(lambda: (0, 0))

    # sm2_dict: dict[int, int] = defaultdict(lambda: 0)
    divisor = size * (size - 1) >> 1
    h1_dict[h1_classes[0]].append(0)
    h2_dict[h2_classes[0]].append(0)

    for i in range(1, size):
        res1 = h1_dict[h1_classes[i]]
        res2 = h2_dict[h2_classes[i]]

        sum += i

        if len(res1) < len(res2):
            sm = 0
            # sm, it = sm1_dict[(h1_classes[i], h2_classes[i])]
            for ii in res1:  # res1[it::]:
                # it += 1
                if fisl(ii, res2) == -1:
                    sm += 1
            # sm1_dict[(h1_classes[i], h2_classes[i])] = (sm, it)
            sum -= sm + (len(res2) - (len(res1) - sm))
        else:
            sm = 0  # sm2_dict[(h2_classes[i], h1_classes[i])]
            # sm, it = sm2_dict[(h2_classes[i], h1_classes[i])]
            for ii in res2:  # res2[it::]:
                # it += 1
                if fisl(ii, res1) == -1:
                    sm += 1
            # sm2_dict[(h2_classes[i], h1_classes[i])] = (sm, it)
            sum -= sm + (len(res1) - (len(res2) - sm))

        h1_dict[h1_classes[i]].append(i)
        h2_dict[h2_classes[i]].append(i)
    # gcd_val = gcd(sum, divisor)
    return Fraction(sum, divisor)


if __name__ == "__main__":
    path = Path("./data/551.txt")
    res = similarity(*parser(path))
    print(f"{res.numerator}/{res.denominator}")
