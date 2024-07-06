from pathlib import Path

import numpy as np

from src.task_551 import similarity, parser


def test_parser_551():
    path = Path("./tests/data/551/test1.txt")
    h1_classes, h2_classes, size = parser(path)
    assert np.all(h1_classes == np.array([1, 2, 0]))
    assert np.all(h2_classes == np.array([0, 2, 1]))
    assert size == 3

    path = Path("./tests/data/551/test2.txt")
    h1_classes, h2_classes, size = parser(path)
    assert np.all(h1_classes == np.array([1, 1, 2, 2, 2]))
    assert np.all(h2_classes == np.array([3, 3, 3, 4, 4]))
    assert size == 5

    path = Path("./tests/data/551/test3.txt")
    h1_classes, h2_classes, size = parser(path)
    assert np.all(h1_classes == np.array([1, 2, 1, 2, 1, 2, 1, 2, 1, 2]))
    assert np.all(h2_classes == np.array([1, 2, 3, 4, 5, 5, 4, 3, 2, 1]))
    assert size == 10

    path = Path("./tests/data/551/test4.txt")
    h1_classes, h2_classes, size = parser(path)
    assert np.all(h1_classes == np.array([1, 1]))
    assert np.all(h2_classes == np.array([0, 0]))
    assert size == 2

    path = Path("./tests/data/551/test5.txt")
    h1_classes, h2_classes, size = parser(path)
    assert np.all(h1_classes == np.array([1, 1]))
    assert np.all(h2_classes == np.array([0, 1]))
    assert size == 2


def test_task_551():
    path = Path("./tests/data/551/test1.txt")
    assert similarity(*parser(path)) == (1, 1)

    path = Path("./tests/data/551/test2.txt")
    assert similarity(*parser(path)) == (3, 5)

    path = Path("./tests/data/551/test3.txt")
    assert similarity(*parser(path)) == (4, 9)

    path = Path("./tests/data/551/test4.txt")
    assert similarity(*parser(path)) == (1, 1)

    path = Path("./tests/data/551/test5.txt")
    assert similarity(*parser(path)) == (0, 1)
