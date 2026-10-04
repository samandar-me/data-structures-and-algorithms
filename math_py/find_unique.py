from typing import Counter

def find_unique(nums: list) -> int:
    counter = Counter(nums)

    for k, v in counter.items():
        if v == 1:
            return k