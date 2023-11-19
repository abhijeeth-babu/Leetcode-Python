# Given a string s, find the longest palindromic substring in s
# --- Example
# longestPalindrome("cbbd") --> "bb"
# longestPalindrome("abba") --> "abba"
# longestPalindrome("a") --> "a"

class Solution:
    def longestPalindrome(self, s: str):
        len_s = len(s)
        max_len = 0
        max_l = 0
        max_r = 0
        for i, _ in enumerate(s):
            l, r = i, i + 1
            while l >= 0 and r < len_s:
                if s[l] == s[r]:
                    l -= 1
                    r += 1
                else:
                    break
            if r - l - 1 > max_len:
                max_len = r - l - 1
                max_l = l
                max_r = r
            # longest = s[l+1:r] if r - 1 - l > len(longest) else longest 

            l, r = i - 1, i + 1
            while l >= 0 and r < len_s:
                if s[l] == s[r]:
                    l -= 1
                    r += 1   
                else:
                    break
            # longest = s[l+1:r] if r - 1 - l > len(longest) else longest
            if r - l - 1 > max_len:
                max_len = r - l - 1
                max_l = l
                max_r = r

        return s[max_l+1: max_r]
            

