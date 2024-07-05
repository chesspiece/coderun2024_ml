from pathlib import Path

import numpy as np

from src.task_554 import main, parser


def test_task_554():
    path = Path("./tests/data/554/test1.txt")
    assert np.all(main(*parser(path)) == np.array([[6, 9]]))
    path = Path("./tests/data/554/test2.txt")
    assert np.all(main(*parser(path)) == np.array([[3, 6], [6, 3]]))
    path = Path("./tests/data/554/test3.txt")
    assert np.all(main(*parser(path)) == np.array([[-2, 2, -2, 2], [3, -3, 3, -3]]))
    path = Path("./tests/data/554/test4.txt")
    assert np.all(main(*parser(path)) == np.array([[4]]))
