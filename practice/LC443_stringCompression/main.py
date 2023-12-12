from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        # pointer that traverses the list
        start = 0
        # keep tracking of the position we will be writing into
        writing_pos = 0
        while start < len(chars):
            count = 1
            ch = chars[start]
            # count the occurances
            while start + count < len(chars) and chars[start + count] == ch:
                count += 1

            # write into chars
            count_str = ch if count == 1 else ch + str(count)
            chars[writing_pos : writing_pos + len(count_str)] = list(count_str)

            # move writing pointer to next free pos
            writing_pos += len(count_str)

            # move pointer to next char
            start += count

        return writing_pos
