def checksum(data, cursor):
    chk = 0
    for i, c, in enumerate(data[:cursor + 1]):
        chk += i * max(c, 0)
    return chk

if __name__ == '__main__':
    with open('input.txt') as f:
        line = f.readline().strip()

    data = []
    c, i = 0, 0
    while c < len(line):
        data += [i] * int(line[c])
        if c < len(line) - 1:
            data += [-1] * int(line[c+1])
        c += 2
        i += 1

    part1 = data.copy()
    c1, c2 = 0, len(data)-1
    while c1 < c2:
        if part1[c1] == -1:
            while part1[c2] == -1:
                c2 -= 1
            part1[c1] = part1[c2]
            c2 -= 1
        c1 += 1

    print('1:', checksum(part1, c2))

    c1 = len(data) - 1
    for id in range(data[c1], 0, -1):
        c2 = c1
        while data[c1] > id:
            c1 -= 1
            c2 -= 1
        while data[c1] == id:
            c1 -= 1

        c1 += 1

        c3, c4 = 0, 0
        while c4 < c1:
            if data[c4] == -1:
                c4 += 1
            else:
                c3 = c4 = c4 + 1

            if c4 - c3 - 1 == c2 - c1:
                data[c3:c4] = data[c1:c2 + 1]
                data[c1:c2 + 1] = [-1] * (c2 - c1 + 1)
                c1 -= 1
                break
        else:
            c1 -= 1

        while data[c1] == -1:
            c1 -= 1

    print('2:', checksum(data, len(data) - 1))
