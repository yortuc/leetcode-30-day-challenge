class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        g = {}
        
        def get_hash(ss):
            ret = 1
            for k in ss:
                ret *= ord(k)
            return ret + sum([ord(q) for q in ss])
        
        for s in strs:
            s_hash = get_hash(s)
            
            if s_hash in g:
                g[s_hash].append(s)
            else:
                g[s_hash] = [s]
                
        ret = []
        for k in g:
            ret.append(g[k])
            
        return ret
        
       
# ------------------------------        
# Not the sexiest solution. And not guaranteed to work with all strings.
# better way: sort each string chars, put into dict as keys.
# ------------------------------
# 101 / 101 test cases passed.
# Runtime: 116 ms
# Memory Usage: 16.9 MB
# ------------------------------

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        g = {}
        
        for s in strs:
            s_hash = ''.join(sorted(list(s)))
            if s_hash in g: 
                g[s_hash].append(s)
            else:
                g[s_hash] = [s]
        
        ret = [g[k] for k in g]
        return ret
        
# Runtime: 96 ms
# Memory Usage: 16.5 MB
# the gain is less than I expected
