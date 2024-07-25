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
    res: list[tuple[int, int]] = []
    for idx1, str1 in enumerate(input_strings):
        for idx2, str2 in enumerate(input_strings):
            if idx1 == idx2:
                continue
            new_str = str1 + str2
            if len(new_str) % 2 != 0:
                continue
            half_len = len(new_str) // 2
            for i in range(half_len):
                if new_str[i] != new_str[i + half_len]:
                    break
            else:
                res.append((idx1 + 1, idx2 + 1))
    return res


if __name__ == "__main__":
    path = Path("./data/552.txt")
    res = check_tandem(parser(path))
    for i, j in res:
        print(f"{i} {j}")
