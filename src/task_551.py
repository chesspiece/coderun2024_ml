import numpy as np
import os
from pathlib import Path
import numpy.typing as npt


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
    array: npt.NDArray[np.int64], ker: npt.NDArray[np.int64], size: int
) -> tuple[int, int]:
    """
    Compute 2d convolution.
    """
    return (0, 0)


if __name__ == "__main__":
    path = Path("./data/551.txt")
    res = similarity(*parser(path))
