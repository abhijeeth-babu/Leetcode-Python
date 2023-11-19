class Solution:
    def lengthOfLongestSubstring(self, s: str):
        char_map = {}
        max_len = 0
        left = 0

        for right, ch in enumerate(s):
            char_map[ch] = char_map.get(ch, 0) + 1

            if char_map[ch] < 2:
                max_len = max(max_len, right - left + 1)

            while char_map[ch] > 1:
                ch_left = s[left]
                char_map[ch_left] -= 1
                left += 1
        
        return max_len
