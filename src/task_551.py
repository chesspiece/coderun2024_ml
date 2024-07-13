import bisect
import os
from collections import defaultdict
from fractions import Fraction
from pathlib import Path


def countingSort(array: list[int]):
    """
    Counting sort implementations.
    Returns indexes for  sorted array.
    """
    size = len(array)
    output = [0] * size

    # Initialize count array
    count = [0] * size

    # Store the count of each elements in count array
    for i in range(0, size):
        count[array[i]] += 1

    # Store the cummulative count
    for i in range(1, size):
        count[i] += count[i - 1]

    # Find the index of each element of the original array in count array
    # place the elements in output array
    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = i
        count[array[i]] -= 1
        i -= 1

    return output


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
    idxs = countingSort(h2_classes)

    summ = size * (size - 1) >> 1
    h1_dict: list[list[int]] = [[] for _ in range(size)]
    sm1_dict: dict[int, tuple[int, int]] = defaultdict(lambda: (0, 0))

    divisor = summ
    h1_dict[h1_classes[idxs[0]]].append(0)
    idx_check = 0

    for i in range(1, size):
        ic = idxs[i]
        r1 = h1_classes[ic]
        if h2_classes[ic] != h2_classes[idxs[i - 1]]:
            idx_check = i
            sm1_dict = defaultdict(lambda: (0, 0))
        res1 = h1_dict[r1]
        lres1 = len(res1)
        lres2 = i - idx_check

        sm, it = sm1_dict[r1]
        ln = bisect.bisect_left(res1[it::], idx_check)
        sm += 2 * ln
        sm1_dict[r1] = (sm, it + ln)
        summ -= sm + lres2 - lres1

        h1_dict[r1].append(i)
    return Fraction(summ, divisor)


if __name__ == "__main__":
    path = Path("./data/551.txt")
    res = similarity(*parser(path))
    print(f"{res.numerator}/{res.denominator}")
