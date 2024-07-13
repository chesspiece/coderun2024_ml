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
        initial_matrix_rows, initial_matrix_columns, kernel_size = (
            int(x) for x in f.readline().strip().split(sep=" ")
        )

        initial_matrix = np.zeros(
            (
                initial_matrix_rows,
                initial_matrix_columns,
            ),
            dtype=np.int32,
        )
        for initial_matrix_row in range(initial_matrix_rows):
            initial_matrix[initial_matrix_row, :] = np.array(
                [int(x) for x in f.readline().strip().split(sep=" ")]
            )
        convolved_matrix = np.zeros(
            (
                initial_matrix_rows - kernel_size + 1,
                initial_matrix_columns - kernel_size + 1,
            ),
            dtype=np.int32,
        )
        for convolved_matrix_row in range(initial_matrix_rows - kernel_size + 1):
            convolved_matrix[convolved_matrix_row, :] = np.array(
                [int(x) for x in f.readline().strip().split(sep=" ")]
            )

    return (
        (initial_matrix_rows, initial_matrix_columns, kernel_size),
        initial_matrix,
        convolved_matrix,
    )


def custom_inverse_conv2d(
    initial_matrix_rows: int,
    initial_matrix_columns: int,
    kernel_size: int,
    initial_matrix: npt.NDArray[np.int32],
    convolved_matrix: npt.NDArray[np.int32],
) -> npt.NDArray[np.float32]:
    V = np.zeros(
        (
            kernel_size**2,
            kernel_size**2,
        ),
        dtype=np.int32,
    )
    res = np.zeros((kernel_size**2, 1), dtype=np.int32)
    row_index, column_index = 0, 0
    for elem in range(kernel_size**2):
        row_index_kernel_elem, column_index_kernel_elem = row_index, column_index
        for row in range(kernel_size):
            column_index_kernel_elem = column_index
            for column in range(kernel_size):
                V[elem, row * kernel_size + column] = initial_matrix[
                    row_index_kernel_elem, column_index_kernel_elem
                ]
                column_index_kernel_elem = column_index_kernel_elem + 1
            row_index_kernel_elem = row_index_kernel_elem + 1
        res[elem, :] = convolved_matrix[row_index, column_index]

        column_index = column_index + 1
        if initial_matrix_columns - column_index < kernel_size:
            column_index = 0
            row_index += 1
    return (np.linalg.inv(V) @ res).reshape((kernel_size, kernel_size))


if __name__ == "__main__":
    path = Path("./data/555.txt")
    params, initial_matrix, convolved_matrix = parser(path)
    res = custom_inverse_conv2d(*params, initial_matrix, convolved_matrix)
    for row in res:
        print(" ".join([f"{x:.0f}" for x in row]))
