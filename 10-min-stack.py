class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = []
        self.mins = []


    def push(self, x: int) -> None:
        self.arr.append(x)
        
        if len(self.mins) == 0 or x <= self.getMin():
            self.mins.append(x)

    def pop(self) -> None:
        if self.arr:
            ret = self.arr.pop()
            
            if ret == self.getMin():
                self.mins.pop()
        
            return ret
    
    def top(self) -> int:
        return self.arr[-1]
        

    def getMin(self) -> int:
        return self.mins[-1]


# 18 / 18 test cases passed.
# Status: Accepted
# Runtime: 64 ms
# Memory Usage: 17.3 MB
