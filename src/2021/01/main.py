if __name__ == '__main__':
    with open('input.txt') as f:
        data = tuple(int(l.strip()) for l in f.readlines())
    for t, s in enumerate((1, 3)):
        x = [1 if sum(data[i:i+s]) < sum(data[i+1: i+s+1]) else 0 for i in range(len(data)-s)]
        print(str(t+1) + ':', sum(x))