class Solution:
    def isAnagram(self, s, t):
        char_map = {}

        for i, ch in enumerate(s):
            char_map[ch] = char_map.get(ch, 0) + 1
        
        for i, ch in enumerate(t):
            char_map[ch] = char_map.get(ch, 0) - 1
            if char_map[ch] == 0:
                del char_map[ch]
        
        return not char_map
            
        
              