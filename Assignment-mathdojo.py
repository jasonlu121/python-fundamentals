class MathDojo:
    def __init__(self):
        self.start = 0

    def add(self, *args):
        for a in args:
            self.start += a
        return self

    def minus(self, *args):
        for b in args:
            self.start -= b
        return self

    def result(self):
        return self.start
md = MathDojo()
x = md.add(2).add(2, 5, 1).minus(3, 2).result()
print(x)
