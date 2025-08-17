class StockSpanner:

    def __init__(self):
        self.stack = []


    def next(self, price: int) -> int:
        c = 1
        while self.stack and self.stack[-1][0] <= price:
            _,n_c = self.stack.pop()
            c+=n_c
        self.stack.append([price,c])
        return c


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)