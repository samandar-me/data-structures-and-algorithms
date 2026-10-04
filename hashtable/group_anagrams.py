from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hash_map = defaultdict(list)

        for s in strs:
            key = ''.join(sorted(s))
            hash_map[key].append(s)

        return list(hash_map.values())

    # def groupAnagrams(self, strs: list[str]) -> int:
    #
    #     for i in range(len(strs)):
    #         sort = sorted(strs[i])
    #         strs[i] = "".join(sort)
    #
    #     counter = Counter(strs)
    #
    #     return len(counter)