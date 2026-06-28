class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        best_capacity = float('inf')
        best_index = -1

        for i, cap in enumerate(capacity):
            if cap >= itemSize and cap < best_capacity:
                best_capacity = cap
                best_index = i

        return best_index



    # def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
    #     hash_map = {}
    #
    #     for i in range(len(capacity)):
    #         if capacity[i] >= itemSize:
    #             hash_map[i] = capacity[i]
    #
    #     if not hash_map:
    #         return -1
    #
    #     m = min(hash_map.values())
    #
    #     for k, v in hash_map.items():
    #         if v == m:
    #             return k
    #
    #     return -1

