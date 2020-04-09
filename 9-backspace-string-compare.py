#
# O(n) Solution
#   
from collections import deque

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        c1 = deque()
        c2 = deque()
        
        for s in S:
            if s == '#':
                if c1:
                    c1.pop()
            else:
                c1.append(s)
                
        for t in T:
            if t == '#':
                if c2:
                    c2.pop()
            else:
                c2.append(t)
                                
        return list(c1) == list(c2)
        

# -----------------------------
# 104 / 104 test cases passed.
# Status: Accepted
# Runtime: 28 ms
# Memory Usage: 13.9 MB
# -----------------------------