from typing import List


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:

        result = []

        for row in image:
            row.reverse()
            row_list = []
            for num in row:
                if num == 0:
                    row_list.append(1)
                else:
                    row_list.append(0)


            result.append(row_list)

        return result