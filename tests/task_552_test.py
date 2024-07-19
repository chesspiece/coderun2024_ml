from pathlib import Path

from src.task_552 import parser


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
