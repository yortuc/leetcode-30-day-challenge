class Solution:
    def countElements(self, arr: List[int]) -> int:
        ret = 0
        cache = {}
        
        # count items 
        for i in arr:
            if i in cache:
                cache[i] += 1
            else:
                cache[i] = 1
        
        for i in cache.keys():
            if i+1 in cache.keys():
                ret += cache[i]

        return ret

# ---------------------------		
# 35 / 35 test cases passed.
# Status: Accepted
# Runtime: 24 ms
# Memory Usage: 14 MB
# ---------------------------