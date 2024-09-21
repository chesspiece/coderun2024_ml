import os
from pathlib import Path

import numpy as np
import numpy.typing as npt

from sklearn.cluster import KMeans
from scipy.optimize import minimize


def parser(path: os.PathLike[str]) -> tuple[npt.NDArray[np.int64], int, int, int, int]:
    """
    Parse the initial file.
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


def compute_centers(
    points: npt.NDArray[np.int64],
    n_clusters: int,
    n_points: int,
    c_cost: int,
    C_const: int,
):
    """
    According to the conditions of the task it is assumed that points contains in itself n_clusters convex clusters.
    This function creates txt files which contains results of the task.

    Args:
    -----
        points (npt.NDArray[np.int64]): 2d coordinates
        n_clusters (int): number of clusters.
        n_points (int): number of points. Should be equal to the points.size
        c_cost (int): cost constant
        C_const (int): overall gain constant

    Returns:
    --------
    """
    clusters_find = KMeans(n_clusters=n_clusters, algorithm="elkan").fit(points)
    clusters_points: dict[int, npt.NDArray[np.int32]] = {
        i: np.where(clusters_find.labels_ == i)[0] for i in range(n_clusters)
    }
    cluster_centres: list[npt.NDArray[np.float64]] = []

    sm = 0
    for idx in range(n_clusters):
        cluster_centre = clusters_find.cluster_centers_[idx]
        current_cluster_size = clusters_points[idx].size

        def fn(x: npt.NDArray[np.float64]):
            sm3 = 0
            for j in range(current_cluster_size):
                idx2 = clusters_points[idx][j]
                sm3 += (
                    c_cost
                    * (np.power(np.linalg.norm(x - points[idx2], ord=2), 1 / 4) + 1)
                    / current_cluster_size
                )
            return sm3

        res = minimize(
            fn, clusters_find.cluster_centers_[idx], method="Nelder-Mead", tol=1e-12
        )
        cluster_centre: npt.NDArray[np.float64] = res.x
        sm += res.fun

        cluster_centres.append(cluster_centre)

    with open("output_task_556.txt", "w") as f:
        f.write(f"{C_const - sm}\n")
        for centre in cluster_centres:
            f.write(f"{centre[0]} {centre[1]}\n")
        for idx in range(n_clusters):
            f.write(" ".join(map(str, clusters_points[idx])) + "\n")
    return


if __name__ == "__main__":
    path = Path("./data/556.txt")
    compute_centers(*parser(path))
