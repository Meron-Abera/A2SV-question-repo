class Node:
    def __init__(self, value):
        self.value = value
        self.min = None
    
class MinStack:

    def __init__(self):
        self.stack = []
        self.min = float('inf')

    def push(self, x: int) -> None:
        node = Node(x) 
        node.min = self.min
        self.stack.append(node)
        self.min = min(self.min,x)

    def pop(self) -> None:
        node = self.stack.pop()
        self.min = node.min

    def top(self) -> int:
        return self.stack[-1].value

    def getMin(self) -> int:
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
