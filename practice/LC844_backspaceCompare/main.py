class Solution:
    def backspaceCompare(self, S, T):
        st_s = []
        st_t = []

        for ch in S:
            if ch == '#':
                if st_s:
                    st_s.pop()
            else:
                st_s.append(ch)
        
        for ch in T:
            if ch == '#':
                if st_t:
                    st_t.pop()
            else:
                st_t.append(ch)
        
        return ''.join(st_s) == ''.join(st_t)
