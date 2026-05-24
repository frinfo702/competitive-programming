class FenwickTree:
    """
    aka BIT
    
    """
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i, x):
        i += 1
        while i <= self.n:
            self.bit[i] += x
            i += i & -i

    def sum(self, i):
        # sum of [0, i]
        i += 1
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s
