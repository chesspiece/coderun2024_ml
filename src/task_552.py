import os
from pathlib import Path


def parser(
    path: os.PathLike[str],
) -> list[str]:
    with open(path, "r") as f:
        n = int(f.readline())
        res: list[str] = []
        for _ in range(n):
            res.append(f.readline().strip())
    return res


def check_tandem(input_strings: list[str]) -> list[tuple[int, int]]:
    return [(0, 1)]


if __name__ == "__main__":
    path = Path("./data/552.txt")
    res = similarity(*parser(path))
