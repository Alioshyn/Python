class tribonachiIterator:
    num1 = 0
    num2 = 0
    num3 = 1

    def __init__(self, val):
        self.counter = 0
        self.limit = val

    def __next__(self):
        if self.counter <= self.limit:
            self.counter += 1
            if (self.counter == 1 or self.counter == 2): return self.num1
            if (self.counter==3): return self.num3
            else:
                sum = self.num1 + self.num2 + self.num3
                self.num1 = self.num2
                self.num2 = self.num3
                self.num3 = sum_num
                return sum_num
        else: raise StopIteration

    def __iter__(self): return self



val = int(input('Введите длину ряда Трибоначчи: '))
iter = tribonachiIterator(val)

trib_list = []
for i in iter:
    trib_list.append(i)
print(trib_list)