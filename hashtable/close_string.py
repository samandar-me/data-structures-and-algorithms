from collections import Counter

class Solution:
    # AI optimized version
    def closeStrings(self, word1: str, word2: str) -> bool:
        counter1 = Counter(word1)
        counter2 = Counter(word2)

        return (
            counter1.keys() == counter2.keys()
            and sorted(counter1.values()) == sorted(counter2.values())
        )

    # my version
    def closeStrings(self, word1: str, word2: str) -> bool:
        n1 = len(word1)
        n2 = len(word2)

        if n1 != n2:
            return False

        set1 = set(word1)
        set2 = set(word2)

        if set1 != set2:
            return False

        counter1 = list(Counter(word1).values())
        counter2 = list(Counter(word2).values())

        counter1.sort()
        counter2.sort()

        for i in range(len(counter1)):
            if counter1[i] != counter2[i]:
                return False

        return True
