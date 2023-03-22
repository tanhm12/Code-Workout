class BrowserHistory:

    def __init__(self, homepage: str):
        self.urls = [homepage]
        self.counter = 0
        self.last = 0

    def visit(self, url: str) -> None:
        if len(self.urls) <= self.counter + 1:
            self.urls.append(url)
        else:
            self.urls[self.counter + 1] = url
        self.counter += 1
        self.last = self.counter
        

    def back(self, steps: int) -> str:
        self.counter = max(self.counter-steps, 0)
        return self.urls[self.counter]
        

    def forward(self, steps: int) -> str:
        self.counter = min(self.last, self.counter + steps)
        # self.last = self.counter
        return self.urls[self.counter]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)