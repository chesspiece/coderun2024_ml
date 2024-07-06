from pathlib import Path

import numpy as np

from src.task_554 import custom_conv2d, parser


def test_parser_554():
    path = Path("./tests/data/554/test1.txt")
    arr, ker = parser(path)
    assert np.all(arr == np.array([[1, 2, 3], [2, 3, 4]]))
    assert np.all(ker == np.array([[1, 0], [1, 1]]))

    path = Path("./tests/data/554/test2.txt")
    arr, ker = parser(path)
    assert np.all(arr == np.array([[1, 2], [2, 1]]))
    assert np.all(ker == np.array([[3]]))

    path = Path("./tests/data/554/test3.txt")
    arr, ker = parser(path)
    assert np.all(arr == np.array([[1, 0, 1, 0, 1], [0, 1, 0, 1, 0], [2, 0, 2, 0, 2]]))
    assert np.all(ker == np.array([[-1, 1], [1, -1]]))

    path = Path("./tests/data/554/test4.txt")
    arr, ker = parser(path)
    assert np.all(arr == np.array([[1, 2], [3, 4]]))
    assert np.all(ker == np.array([[0, 0], [0, 1]]))


def test_task_554():
    path = Path("./tests/data/554/test1.txt")
    assert np.all(custom_conv2d(*parser(path)) == np.array([[6, 9]]))

    path = Path("./tests/data/554/test2.txt")
    assert np.all(custom_conv2d(*parser(path)) == np.array([[3, 6], [6, 3]]))

    path = Path("./tests/data/554/test3.txt")
    assert np.all(custom_conv2d(*parser(path)) == np.array([[-2, 2, -2, 2], [3, -3, 3, -3]]))

    path = Path("./tests/data/554/test4.txt")
    assert np.all(custom_conv2d(*parser(path)) == np.array([[4]]))
