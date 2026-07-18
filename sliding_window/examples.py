# Example sliding window solution

from typing import List

def max_sub_array_sum_size_k(nums: List[int], k: int) -> int:
    current_sum = sum(nums[:k])
    max_sum = current_sum
    for i in range(k, len(nums)):
        current_sum += nums[i]
        current_sum -= nums[i-k]
        max_sum = max(max_sum, current_sum)

    return max_sum

if __name__ == '__main__':
    print(max_sub_array_sum_size_k([4, 2, 1, -9, 8, 4, 3], 3))
