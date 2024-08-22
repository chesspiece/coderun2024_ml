import os
from pathlib import Path

import numpy as np
import numpy.typing as npt


def parser(path: os.PathLike[str]) -> tuple[npt.NDArray[np.int64], int, int, int, int]:
    """
    Parse the intial file.
    Args:
    -----
        path (os.PathLike[str]): path to input file

    Returns:
    --------
        npt.NDArray[np.int64]: array of point
        int: number of clusters
        int: number of point,
        int: cost value
        int: constant value for computations
    """
    with open(path, "r") as f:
        n_clusters, n_points, c_cost, C_const = [
            int(x) for x in f.readline().strip().split()
        ]
        points = np.zeros((n_points, 2), dtype=np.int64)
        for idx, line in enumerate(f):
            points[idx, :] = np.array([int(x) for x in line.strip().split()])
    return points, n_clusters, n_points, c_cost, C_const


if __name__ == "__main__":
    path = Path("./data/556.txt")
