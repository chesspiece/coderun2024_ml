import os
from collections import defaultdict
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
    add_str_left: dict[str, list[int]] = defaultdict(lambda: [])
    for idx1, str1 in enumerate(input_strings):
        add_str_left[str1].append(idx1)
        ln = len(str1)
        ln2 = ln // 2
        for i in range(ln2):
            if str1[0 : i + 1] == str1[ln - i - 1 : :]:
                add_str_left[str1[i + 1 : ln - i - 1]].append(idx1)
    for idx1, str1 in enumerate(input_strings):
        idx_lst = add_str_left[str1]
        for idx in idx_lst:
            if idx == idx1:
                continue
            res.append((idx + 1, idx1 + 1))
            res.append((idx1 + 1, idx + 1))
    return sorted(res)


if __name__ == "__main__":
    path = Path("./data/552.txt")
    res = check_tandem(parser(path))
    for i, j in res:
        print(f"{i} {j}")
