# Happy Number
# Solution
# Write an algorithm to determine if a number is "happy".

# A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

# Example: 

# Input: 19
# Output: true
# Explanation: 
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1

class Solution:
    def isHappy(self, n: int) -> bool:    
        hist = set()
        n_val = n
        
        while True:        
            if n_val in hist:
                return False

            sq_val = sum([int(t)*int(t) for t in list(str(n_val))])

            if sq_val == 1:
                return True
            else:
                hist.add(n_val)
                n_val = sq_val 

                
# ----------------------------------------------------
# Your runtime beats 30.63 % of python3 submissions.
# 401 / 401 test cases passed.
# Status: Accepted
# Runtime: 36 ms
# Memory Usage: 13.6 MB
# ----------------------------------------------------
