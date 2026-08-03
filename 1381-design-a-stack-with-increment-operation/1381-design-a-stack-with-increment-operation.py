class CustomStack:

    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.stack = []
        self.inc = []

    def push(self, x):
        if len(self.stack) < self.maxSize:
            self.stack.append(x)
            self.inc.append(0)

    def pop(self):
        if not self.stack:
            return -1

        i = len(self.stack) - 1

        if i > 0:
            self.inc[i - 1] += self.inc[i]

        return self.stack.pop() + self.inc.pop()

    def increment(self, k, val):
        if self.stack:
            self.inc[min(k, len(self.stack)) - 1] += val