class EvenNumbers:

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.n = (self.end - self.start)/2

    def __iter__(self):
        self.i = 0
        self.n += 1
        self.start -= 2
        return self

    def __next__(self):
        self.i += 1
        self.start += 1
        if self.start % 2 == 0:
            if self.i > self.n:
                raise StopIteration()
            self.start += 1
        return self.start + 1


en = EvenNumbers(0, 1)
for a in en:
    print(a)

