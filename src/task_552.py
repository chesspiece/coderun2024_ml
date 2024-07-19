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


if __name__ == "__main__":
    pass
