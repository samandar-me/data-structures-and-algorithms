import math
from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        length = len(chars)

        if length == 1: return 1

        start_point = 0

        for i in range(1, length):
            char_count = i - start_point

            if chars[i] != chars[i - 1] or i + 1 == length:
                if i + 1 == length:
                    char_count += 1

                if 1 < char_count < 10:
                    chars[start_point+1] = f"{char_count}"
                    start_point = i
                elif 1 < char_count >= 10:
                    length_char = int(math.log10(abs(char_count))) + 1
                    stored_length = length_char
                    while char_count:
                        remainder = char_count % 10
                        char_count //= 10
                        chars[start_point+length_char] = f"{remainder}"
                        length_char -= 1
                    start_point += stored_length + 1
                else:
                    start_point += 1

        return start_point