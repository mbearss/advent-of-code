if __name__ == '__main__':
    seats = []
    with open('input.txt') as f:
        for line in f:
            row = [0, 127]
            col = [0, 7]
            rl, ru = 0, 127
            cl, cu = 0, 8
            for t in line:
                if t == 'F':
                    row[1] -= (row[1] - row[0]) // 2 + 1
                elif t == 'B':
                    row[0] += (row[1] - row[0]) // 2 + 1
                elif t == 'L':
                    col[1] -= (col[1] - col[0]) // 2 + 1
                elif t == 'R':
                    col[0] += (col[1] - col[0]) // 2 + 1
            seats.append(row[0] * 8 + col[0])
    m1, m2 = min(seats), max(seats)
    print('1:', m1)
    print('2:', sum(range(m1, m2 + 1)) - sum(seats))

