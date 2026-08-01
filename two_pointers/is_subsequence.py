class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        if not t:
            return False

        sn = len(s)

        counter = 0

        for i in range(len(t)):
            if counter < sn and t[i] == s[counter]:
                counter += 1

        return counter == sn