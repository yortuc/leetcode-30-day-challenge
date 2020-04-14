class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        
        ret = s
        
        for s in shift:
            direction = s[0]
            amount = s[1]
            
            # left shift
            if direction == 0:
                cut = ret[:amount]
                paste = ret + cut
                ret = paste[amount:]
            
            if direction == 1:
                cut = ret[len(ret) - amount:]
                paste = cut + ret
                ret = paste[:len(paste) - amount]
            
        return ret
        
        
# 31 / 31 test cases passed.
# Status: Accepted
# Runtime: 28 ms
# Memory Usage: 13.8 MB