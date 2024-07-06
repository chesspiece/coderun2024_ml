import numpy as np
import os
from pathlib import Path
import numpy.typing as npt


def gcd(a: int, b: int) -> int:
    """
    Returns the gcd of its inputs times the sign of b if b is nonzero,
    and times the sign of a if b is 0.
    """
    while b != 0:
        a, b = b, a % b
    return a


def parser(
    path: os.PathLike[str],
) -> tuple[npt.NDArray[np.int64], npt.NDArray[np.int64], int]:
    """
    Parse input from file into an array and kernel
    """
    with open(path, "r") as f:
        size = int(f.readline().strip())
        h1_classes = np.array(
            [int(x) for x in f.readline().strip().split(sep=" ")]
        )  # classes choosen by first human
        h2_classes = np.array(
            [int(x) for x in f.readline().strip().split(sep=" ")]
        )  # classes choosen by second human
    return h1_classes, h2_classes, size


def similarity(
    h1_classes: npt.NDArray[np.int64], h2_classes: npt.NDArray[np.int64], size: int
) -> tuple[int, int]:
    """
    Compute similarity metric from task 551.
    """
    sum = 0
    divisor = size * (size - 1)
    for i in range(size):
        for j in range(i):
            sum += int(
                (h1_classes[i] == h1_classes[j]) == (h2_classes[i] == h2_classes[j])
            )
    gcd_val = gcd(2 * sum, divisor)
    return (2 * sum // gcd_val, divisor // gcd_val)


if __name__ == "__main__":
    path = Path("./data/551.txt")
    res = similarity(*parser(path))
    print(f"{res[0]}/{res[1]}")
