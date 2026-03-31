class MinStack:

    def __init__(self):
        self.output_stack = []
        self.min_stack = []
        
    def push(self, val: int) -> None:
        self.output_stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
            
    def pop(self) -> None:
        val = self.output_stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()
            
    def top(self) -> int:
        return self.output_stack[-1]
        
    def getMin(self) -> int:
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()