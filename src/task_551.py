import os
from pathlib import Path
import bisect
from fractions import Fraction
from collections import defaultdict


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

    summ = 0
    h1_dict: dict[int, list[int]] = [[] for _ in range(size)]  # type: ignore
    h2_dict: dict[int, list[int]] = [[] for _ in range(size)]  # type: ignore
    res2_dict_check: list[dict[int, bool]] = [
        defaultdict(lambda: False) for _ in range(size)
    ]
    # h2_dict_check: list[list[int]] = [[False]*size for _ in range(size)]
    # sm1_dict: dict[tuple[int, int], tuple[int, int]] = defaultdict(lambda: (0, 0))
    # sm2_dict: dict[tuple[int, int], tuple[int, int]] = defaultdict(lambda: (0, 0))

    divisor = size * (size - 1) >> 1
    h1_dict[h1_classes[0]].append(0)
    h2_dict[h2_classes[0]].append(0)
    res2_dict_check[h2_classes[0]][0] = True

    for i in range(1, size):
        r1 = h1_classes[i]
        r2 = h2_classes[i]
        res1 = h1_dict[r1]
        res2 = h2_dict[r2]
        lres1 = len(res1)
        lres2 = len(res2)

        summ += i

        # sm, it = sm1_dict[(h1_classes[i], h2_classes[i])]
        sm = 0
        # for ii in res1:#res1[it::]:
        #        #it += 1
        #    if not res2_dict_check[r2][ii]:#fisl(ii, res2) == -1:
        #        sm += 1
        sm = sum([2 if (fisl(ii, res2) == -1) else 0 for ii in res1])
        # sm1_dict[(h1_classes[i], h2_classes[i])] = (sm, it)
        summ -= sm + lres2 - lres1

        h1_dict[r1].append(i)
        h2_dict[r2].append(i)
        res2_dict_check[r2][i] = True

    # gcd_val = gcd(sum, divisor)
    return Fraction(summ, divisor)


if __name__ == "__main__":
    path = Path("./data/551.txt")
    res = similarity(*parser(path))
    print(f"{res.numerator}/{res.denominator}")
