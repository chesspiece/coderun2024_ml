from pathlib import Path

import numpy as np

from src.task_556 import parser


def test_parser_552():
    path = Path("./tests/data/556/test1.txt")
    points, n_clusters, n_points, c_cost, C_const = parser(path)
    assert n_clusters == 402
    assert n_points == 17038
    assert c_cost == 10
    assert C_const == 25000
    shp1, shp2 = points.shape
    assert shp1 == n_points
    assert shp2 == 2
    assert np.all(points[0, :] == np.array([-10452622, 18779177]))
    assert np.all(points[2, :] == np.array([30245517, 97800613]))
    assert np.all(points[3, :] == np.array([-32888777, -63963290]))
    assert np.all(points[-1, :] == np.array([-79502479, -79893390]))
