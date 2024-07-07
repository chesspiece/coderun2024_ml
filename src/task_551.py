import numpy as np
import os
from pathlib import Path
import numpy.typing as npt
from collections import defaultdict


def gcd(a: int, b: int) -> int:
    """
    Returns the gcd of its inputs times the sign of b if b is nonzero,
    and times the sign of a if b is 0.
    """
    while b != 0:
        a, b = b, a % b
    return a


def parser(
    path: os.PathLike[str],
) -> tuple[list[int], list[int], int]:
    """
    Parse input from file into an array and kernel
    """
    with open(path, "r") as f:
        size = int(f.readline().strip())
        h1_classes = [int(x) for x in f.readline().strip().split(sep=" ")] # classes choosen by first human
        h2_classes = [int(x) for x in f.readline().strip().split(sep=" ")] # classes choosen by second human
    return h1_classes, h2_classes, size


def similarity(
    h1_classes: list[int], h2_classes: list[int], size: int
) -> tuple[int, int]:
    """
    Compute similarity metric from task 551.
    """
    sum = 0
    h1_dict = {}#defaultdict(lambda: np.array([], dtype=np.int32))
    h2_dict = {}#defaultdict(lambda: np.array([], dtype=np.int32))
    h1_dicttmp = defaultdict(lambda: [])
    h2_dicttmp = defaultdict(lambda: [])
    sm1_dict = defaultdict(lambda: (0, 0))
    #sm2_dict: dict[int, int] = defaultdict(lambda: 0)
    divisor = size * (size - 1) >> 1
    for i in range(0, size):
        h1_dicttmp[h1_classes[i]].append(i)
        h2_dicttmp[h2_classes[i]].append(i)
    for j in h1_dicttmp:
        h1_dict[j] = np.array(h1_dicttmp[j])
    for j in h2_dicttmp:
        h2_dict[j] = np.array(h2_dicttmp[j])
    
    #h1_dict[h1_classes[0]] = np.append(h1_dict[h1_classes[0]], 0) 
    #h2_dict[h2_classes[0]] = np.append(h2_dict[h2_classes[0]], 0) 
    for i in range(1, size):
        #sm1 = (h1_classes[i + 1::] == h1_classes[i])
        #sm2 = (h2_classes[i + 1::] == h2_classes[i])
        #h1_dict[h1_classes[i]] = np.append(h1_dict[h1_classes[i]], i) 
        #h2_dict[h2_classes[i]] = np.append(h2_dict[h2_classes[i]], i) 
        res1 = h1_dict[h1_classes[i]]
        res2 = h2_dict[h2_classes[i]]
        #res1 = res1[res1 < i]
        t1 = res1.searchsorted(i)
        res1=res1[0:t1]
        #res2 = res2[res2 < i]
        t2 = res2.searchsorted(i)
        res2=res2[0:t2]
        sum += i
        if len(res1) == 0:
            sum -= len(res2)
            continue
        if len(res2) == 0:
            sum -= len(res1)
            continue

        if len(res1) < len(res2):
            sm, it = sm1_dict[h1_classes[i]]
            for i in res1[it::]:
                tts = res2.searchsorted(i)
                #if i not in res2:
                if tts==len(res2) or res2[tts] != i:
                    sm += 1
            sm1_dict[(h1_classes[i], h2_classes[i])] = (sm, it+1)
            sum -= sm + (len(res2) - (len(res1) - sm))
        else:
            sm, it = sm1_dict[h2_classes[i]]
            for i in res2[it::]:
                tts = res1.searchsorted(i)
                #if i not in res2:
                if tts==len(res1) or res1[tts] != i:
                    sm += 1
            sm1_dict[(h2_classes[i], h1_classes[i])] = (sm, it+1)
            sum -= sm + (len(res1) - (len(res2) - sm))
        #sum -= res2.size - (res1.size - sm)
    gcd_val = gcd(sum, divisor)
    return (sum // gcd_val, divisor // gcd_val)


if __name__ == "__main__":
    path = Path("./data/551.txt")
    res = similarity(*parser(path))
    print(f"{res[0]}/{res[1]}")
