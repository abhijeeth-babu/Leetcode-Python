class Solution:
    def isValid(self, s):
        ch_map = {
            ')':'(',
            ']':'[',
            '}':'{'
        }
        st = []
        
        for ch in s:
            if ch in ['(', '[', '{']:
                st.append(ch)
            else:
                if not st or st[-1] != ch_map[ch]:
                    return False
                st.pop()
        
        return not st

