class EvenNumbers:

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.i = 0

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        self.i += 1
        if self.i <= self.end - self.start:
            if self.start % 2 == 0:
                self.start += 1
                return self.start

        raise StopIteration()


en = EvenNumbers(10, 25)
for a in en:
    print(a)

