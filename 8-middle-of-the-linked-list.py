# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        
        c = {}
        cur = head
        i = 0
        
        while cur is not None:
            c[i] = cur
            i += 1
            cur = cur.next
        
        count = len(c.keys())
        mid_index = count // 2 
        
        if count == 0:
            return head
        else:
            return c[mid_index]
            
# -----------------------------------
# 15 / 15 test cases passed.
# Status: Accepted
# Runtime: 20 ms
# Memory Usage: 13.8 MB
# -----------------------------------
