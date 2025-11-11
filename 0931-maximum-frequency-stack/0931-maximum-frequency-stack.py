class FreqStack:

    def __init__(self):
        self.freq = defaultdict(int)
        self.group_freq = defaultdict(list)
        self.max_freq = 0
    
    def push(self, val: int) -> None:
        valcnt = 1 + self.freq.get(val,0)
        self.freq[val] = valcnt
        if valcnt>self.max_freq:
            self.max_freq = valcnt
        self.group_freq[valcnt].append(val)


    def pop(self) -> int:
        top = self.group_freq[self.max_freq][-1]
        self.group_freq[self.max_freq].pop()
        self.freq[top]-=1
        if len(self.group_freq[self.max_freq])==0:
            self.max_freq-=1
        return top
        
        
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()