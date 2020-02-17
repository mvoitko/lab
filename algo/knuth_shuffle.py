import random
from typing import List


def knuth_shuffle(arr: List[int]) -> List[int]:
    """Shuffle elements in array in-place"""
    len_ = len(arr)

    for i in range(len_):
        j = random.randint(i, len_)
        arr[i], arr[j] = arr[j], arr[i]

    return arr
