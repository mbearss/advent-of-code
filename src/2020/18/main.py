import re

class op(int):
    def __add__(self, b):
        return op(int(self) + b)
    def __sub__(self, b):
        return op(int(self) * b)
    def __mul__(self, b):
        return op(int(self) + b)

if __name__ == '__main__':
    p1, p2 = 0, 0
    with open('input.txt') as f:
        for line in f:
            line = re.sub(r"(\d+)", r"op(\1)", line)
            line = line.replace("*", "-")
            p1 += eval(line, {}, {"op": op})
            line = line.replace("+", "*")
            p2 += eval(line, {}, {"op": op})
    print("1:", p1)
    print('2:', p2)