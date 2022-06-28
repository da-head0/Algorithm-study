class MyStack:

    def __init__(self):
        self.myqueue = []
        

    def push(self, x: int) -> None:
        self.myqueue.append(x)
        

    def pop(self) -> int:
        top_item = self.myqueue.pop()
        return top_item
    
    def top(self) -> int:
        return self.myqueue[-1]
        

    def empty(self) -> bool:
        if len(self.myqueue) == 0:
            return True
        else:
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()