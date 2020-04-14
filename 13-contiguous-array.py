class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        c = {}
        relative = 0
        
        for i in range(len(nums)):
            if nums[i] == 0:
                relative -= 1
            if nums[i] == 1:
                relative += 1
            
            if relative in c:
                c[relative].append(i)
            else:
                c[relative] = [i]
                
        # get max range in the same keys
        print(c)
        
        mx = 0
        for k in c.keys():
            if len(c[k]) > 1:
                mx = max(mx, c[k][-1] - c[k][0])
            if k == 0:
                mx = max(mx, c[k][-1]+1)
        
        return mx
        
        
# 555 / 555 test cases passed.
# Status: Accepted
# Runtime: 956 ms
# Memory Usage: 22 MB