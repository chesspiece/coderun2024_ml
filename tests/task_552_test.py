from pathlib import Path

from src.task_552 import check_tandem, parser


def test_parser_552():
    path = Path("./tests/data/552/test1.txt")
    input_strigs = parser(path)
    assert input_strigs == ["a", "abbaa", "bba", "abb"]

    path = Path("./tests/data/552/test2.txt")
    input_strigs = parser(path)
    assert input_strigs == ["tan", "dem", "tandemtan", "demtandem"]

    path = Path("./tests/data/552/test3.txt")
    input_strigs = parser(path)
    assert input_strigs == ["a", "aa", "aaa", "aaaa"]


def test_task_552():
    path = Path("./tests/data/552/test1.txt")
    res = check_tandem(parser(path))
    assert res == [(2, 3), (3, 2)]

    path = Path("./tests/data/552/test2.txt")
    res = check_tandem(parser(path))
    assert res == [(1, 4), (2, 3), (3, 2), (4, 1)]

    path = Path("./tests/data/552/test3.txt")
    res = check_tandem(parser(path))
    assert res == [(1, 3), (2, 4), (3, 1), (4, 2)]
