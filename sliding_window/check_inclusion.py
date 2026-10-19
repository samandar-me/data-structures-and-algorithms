class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        sett = set()
        sett.add("".join(sorted(s2[:k])))

        for right in range(1, len(s2) - k + 1):
            s = sorted(s2[right:right + k])
            sett.add("".join(s))

        s1 = "".join(sorted(s1))
        if s1 in sett:
            return True

        return False