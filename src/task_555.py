import os
import pathlib

import numpy as np
import numpy.typing as npt


def parser(
    path: os.PathLike[str],
) -> tuple[tuple[int, int, int], npt.NDArray[np.int32], npt.NDArray[np.int32]]:
    """
    Parse input from file into an array and kernel
    """
    with open(path, "r") as f:
        n, m, k = (int(x) for x in f.readline().strip().split(sep=" "))

        initial_matrix = np.zeros(
            (
                n,
                m,
            ),
            dtype=np.int32,
        )
        for initial_matrix_row in range(n):
            initial_matrix[initial_matrix_row, :] = np.array(
                [int(x) for x in f.readline().strip().split(sep=" ")]
            )
        convolved_matrix = np.zeros(
            (
                n - k + 1,
                m - k + 1,
            ),
            dtype=np.int32,
        )
        for convolved_matrix_row in range(n - k + 1):
            convolved_matrix[convolved_matrix_row, :] = np.array(
                [int(x) for x in f.readline().strip().split(sep=" ")]
            )

    return (n, m, k), initial_matrix, convolved_matrix


def custom_inverse_conv2d():
    pass


if __name__ == "__main__":
    pass
