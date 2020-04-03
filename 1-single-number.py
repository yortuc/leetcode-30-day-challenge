# Single Number
# Solution
# Given a non-empty array of integers, every element appears twice except for one. Find that single one.

# Note:
# Your algorithm should have a linear runtime complexity. 
# Could you implement it without using extra memory?

# Example 1:

# Input: [2,2,1]
# Output: 1
# Example 2:

# Input: [4,1,2,1,2]
# Output: 4

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cache = set()
        
        for n in nums:
            if n in cache:
                cache.remove(n)
            else:
                cache.add(n)
                
        # there should be only one remaining item in cache
        
        return list(cache)[0]
        
# ----------------------------------------------------
# Your runtime beats 83.64 % of python3 submissions.
# 16 / 16 test cases passed.
# Status: Accepted
# Runtime: 84 ms
# Memory Usage: 16.3 MB
# ----------------------------------------------------
