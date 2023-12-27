if __name__ == '__main__':
    p1, p2 = 0, 0
    with open('input.txt') as f:
        for line in f:
            tokens = line.split()
            l, u = map(int, tokens[0].split('-'))
            c = tokens[1][0]
            if l <= tokens[2].count(c) <= u:
                p1 += 1
            if (tokens[2][l-1] == c) ^ (tokens[2][u-1] == c):
                p2 += 1
    print('1:', p1)
    print('2:', p2)

