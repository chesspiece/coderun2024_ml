import os
from pathlib import Path

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


def custom_inverse_conv2d(
    n: int,
    m: int,
    k: int,
    initial_matrix: npt.NDArray[np.int32],
    convolved_matrix: npt.NDArray[np.int32],
) -> npt.NDArray[np.float32]:
    V = np.zeros(
        (
            k**2,
            k**2,
        ),
        dtype=np.int32,
    )
    res = np.zeros((k**2, 1), dtype=np.int32)
    row_index, column_index = 0, 0
    for tt in range(k**2):
        row_index1, column_index1 = row_index, column_index
        for ii in range(k):
            column_index1 = column_index
            for jj in range(k):
                V[tt, ii * k + jj] = initial_matrix[row_index1, column_index1]
                column_index1 = column_index1 + 1
            row_index1 = row_index1 + 1
        res[tt, :] = convolved_matrix[row_index, column_index]

        column_index = column_index + 1
        if m - column_index < k:
            column_index = 0
            row_index += 1
    return (np.linalg.inv(V) @ res).reshape((k, k))


if __name__ == "__main__":
    path = Path("./data/555.txt")
    params, initial_matrix, convolved_matrix = parser(path)
    res = custom_inverse_conv2d(*params, initial_matrix, convolved_matrix)
    for row in res:
        print(" ".join([f"{x:.0f}" for x in row]))
