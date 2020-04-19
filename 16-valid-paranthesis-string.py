
# https://leetcode.com/problems/valid-parenthesis-string/discuss/582174/Simple-Python-solution-Time%3A-O(n)-space%3A-O(1)
class Solution:

    def checkValidString(self, s: str) -> bool:
        left_balance = 0
        right_balance = 0
        n = len(s)
        
        for i in range(n):
            # checl left balance
            if s[i] == '*' or s[i] == '(':
                left_balance += 1
            else:
                left_balance -= 1
            
            #chec right balance
            if s[n-i-1] == '*' or s[n-i-1] == ')':
                right_balance += 1
            else:
                right_balance -= 1
                
            
            if left_balance <0 or right_balance<0:
                return False
            
        return True
        
         
# 58 / 58 test cases passed.
# Status: Accepted
# Runtime: 24 ms
# Memory Usage: 13.8 MB
