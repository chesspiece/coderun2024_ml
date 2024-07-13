from pathlib import Path

import numpy as np

from src.task_555 import custom_inverse_conv2d, parser


def test_parser_555():
    path = Path("./tests/data/555/test1.txt")
    params, initial_matrix, result_matrix = parser(path)
    assert params == (5, 6, 1)
    assert np.equal(
        initial_matrix,
        np.array(
            [
                [1, 2, 3, 4, 5, 6],
                [1, 2, 3, 4, 5, 6],
                [1, 2, 3, 4, 5, 6],
                [1, 2, 3, 4, 5, 6],
                [1, 2, 3, 4, 5, 6],
            ]
        ),
    ).all()
    assert np.equal(
        result_matrix,
        np.array(
            [
                [1, 2, 3, 4, 5, 6],
                [1, 2, 3, 4, 5, 6],
                [1, 2, 3, 4, 5, 6],
                [1, 2, 3, 4, 5, 6],
                [1, 2, 3, 4, 5, 6],
            ]
        ),
    ).all()

    path = Path("./tests/data/555/test2.txt")
    params, initial_matrix, result_matrix = parser(path)
    assert params == (5, 5, 2)
    assert np.equal(
        initial_matrix,
        np.array(
            [
                [-48, -47, -5, 58, -93],
                [35, -26, 42, -58, -59],
                [-37, 30, 20, 100, -83],
                [43, -99, -9, 19, -48],
                [93, 37, -84, -99, 84],
            ]
        ),
    ).all()
    assert np.equal(
        result_matrix,
        np.array(
            [
                [-2688, 10345, -6343, -9836],
                [1671, 3474, 1850, -13016],
                [-8449, 5224, 4502, -18620],
                [-11835, -2233, -1057, 12591],
            ]
        ),
    ).all()

    path = Path("./tests/data/555/test3.txt")
    params, initial_matrix, result_matrix = parser(path)
    assert params == (6, 5, 3)
    assert np.equal(
        initial_matrix,
        np.array(
            [
                [-17, -37, 61, -19, 90],
                [94, 6, 22, 86, -82],
                [10, 65, -56, 52, -80],
                [-52, -53, -27, -81, 39],
                [4, 22, 58, -53, -63],
                [-98, 62, -100, 66, -34],
            ]
        ),
    ).all()
    assert np.equal(
        result_matrix,
        np.array(
            [
                [-375, 16185, -6904],
                [-9850, -11424, 5127],
                [2151, -14707, 1641],
                [-1387, 10203, -15056],
            ]
        ),
    ).all()


def test_task_555():
    path = Path("./tests/data/555/test1.txt")
    params, initial_matrix, result_matrix = parser(path)
    res = custom_inverse_conv2d(*params, initial_matrix, result_matrix)
    assert np.allclose(
        res,
        np.array([[1]]),
    )

    path = Path("./tests/data/555/test2.txt")
    params, initial_matrix, result_matrix = parser(path)
    res = custom_inverse_conv2d(*params, initial_matrix, result_matrix)
    assert np.allclose(
        res,
        np.array([[-93, 38], [-82, 96]]),
    )

    path = Path("./tests/data/555/test3.txt")
    params, initial_matrix, result_matrix = parser(path)
    res = custom_inverse_conv2d(*params, initial_matrix, result_matrix)
    assert np.allclose(
        res,
        np.array([[-92, 70, -15], [-3, 97, 32], [50, 38, 43]]),
    )
