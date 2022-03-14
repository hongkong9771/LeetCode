class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        l_s, l_t = len(s), len(t)
        s_stack = []
        t_stack = []
        for i in range(l_s):
            if s[i] != "#":
                s_stack.append(s[i])
            else:
                if s_stack:
                    s_stack.pop()
        
        for j in range(l_t):
            if t[j] != "#":
                t_stack.append(t[j])
            else:
                if t_stack:
                    t_stack.pop()
        return s_stack == t_stack