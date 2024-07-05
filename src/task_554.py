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
    array: npt.NDArray[np.int64, ker : np.ndarray[np.int64]],
) -> npt.NDArray[np.int64]:
    pass


if __name__ == "__main__":
    tst = np.zeros((1, 1))
    pass
