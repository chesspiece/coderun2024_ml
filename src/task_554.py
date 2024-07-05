import numpy as np
import os
from pathlib import Path
import numpy.typing as npt


def parser(path: os.PathLike) -> tuple[npt.NDArray[np.int64], npt.NDArray[np.int64]]:
    """
    Parse input from file into an array and kernel
    """
    with open(path, "r") as f:
        shp1, shp2 = (int(shp) for shp in f.readline().strip().split(sep=" "))
        array = np.zeros(
            (
                shp1,
                shp2,
            ),
            dtype=np.int64,
        )
        for idx in range(shp1):
            array[idx, :] = np.array(
                [int(x) for x in f.readline().strip().split(sep=" ")]
            )
        shp1 = int(f.readline().strip())
        ker = np.zeros((shp1, shp1), dtype=np.int64)  # kernel
        for idx in range(shp1):
            ker[idx, :] = np.array(
                [int(x) for x in f.readline().strip().split(sep=" ")]
            )
        return array, ker


def main(
    array: npt.NDArray[np.int64],
    ker: np.ndarray[np.int64],
) -> npt.NDArray[np.int64]:
    """
    Compute 2d convolution.
    """
    shp, _ = ker.shape
    shp1, shp2 = (arr_shp - shp + 1 for arr_shp in array.shape)
    new_array = np.zeros_like(array)
    for t in range(shp):
        for l in range(shp):  # noqa: E741
            new_array += np.roll(np.roll(array, -t, axis=0), -l, axis=1) * ker[t, l]
    return new_array[0:shp1, 0:shp2]


if __name__ == "__main__":
    path = Path("./data/554.txt")
    arr, ker = parser(path)
    res = main(arr, ker)
    shp1, shp2 = res.shape
    for idx in range(shp1):
        print(" ".join([str(x) for x in res[idx, :]]))
    pass
