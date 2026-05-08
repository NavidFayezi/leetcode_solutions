class MinStack:

    def __init__(self):
        self.main_stack = []
        self.min_stack = []
        
    def push(self, val: int) -> None:
        # this will break if python does not short-circuit logical statements
        if len(self.min_stack) == 0 or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        self.main_stack.append(val)
        
    def pop(self) -> None:
        if self.main_stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        self.main_stack.pop()

    def top(self) -> int:
        return self.main_stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
