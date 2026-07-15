class MinStack:

    def __init__(self):
        self.mst=[]
        self.st=[]
    def push(self, value: int) -> None:
        self.st.append(value)
        if not self.mst or value<=self.mst[-1]:
            self.mst.append(value)
    def pop(self) -> None:
        if self.st[-1]==self.mst[-1]:
            self.mst.pop()
        self.st.pop() 
    def top(self) -> int:
        return self.st[-1]
        

    def getMin(self) -> int:
        return self.mst[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()