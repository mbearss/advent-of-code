if __name__ == '__main__':
    with open('input.txt') as f:
        data = tuple(l.strip().split() for l in f.readlines())

    h, d = 0, 0
    for line in data:
        if line[0] == 'forward':
            h += int(line[1])
        else:
            d += int(line[1]) if line[0] == 'down' else -int(line[1])
    print('1:', h*d)

    a, h, d = 0, 0, 0
    for line in data:
        if line[0] == 'forward':
            x = int(line[1])
            h += x
            d += a * x
        else:
            a += int(line[1]) if line[0] == 'down' else -int(line[1])
    print('2:', h * d)