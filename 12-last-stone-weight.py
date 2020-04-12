class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        while True:
            # get two heaviest
            if len(stones) == 1:
                return stones.pop()

            if len(stones) == 0:
                return 0

            stones = sorted(stones)
            h1 = stones.pop()
            h2 = stones.pop()
            
            if h1 != h2:
                stones.append(abs(h1 - h2))
                
                
# 70 / 70 test cases passed.
# Status: Accepted
# Runtime: 24 ms
# Memory Usage: 13.8 MB