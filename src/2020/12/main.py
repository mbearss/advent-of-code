import math


def rotate_around_origin(p, a):
    x, y = p
    match a[0]:
        case 'L':
            if a[1:] == '90':
                x = -p[1]
                y = p[0]
            if a[1:] == '180':
                x = -p[0]
                y = -p[1]
            if a[1:] == '270':
                x = p[1]
                y = -p[0]
        case 'R':
            if a[1:] == '90':
                x = p[1]
                y = -p[0]
            if a[1:] == '180':
                x = -p[0]
                y = -p[1]
            if a[1:] == '270':
                x = -p[1]
                y = p[0]
    return x, y

if __name__ == '__main__':
    e, n, h = 0, 0, 0
    ew, nw = 10, 1
    e2, n2 = 0, 0

    with open('input.txt') as f:
        for l in f:
            match l[0]:
                case 'N':
                    n += int(l[1:])
                    nw += int(l[1:])
                case 'S':
                    n -= int(l[1:])
                    nw -= int(l[1:])
                case 'E':
                    e += int(l[1:])
                    ew += int(l[1:])
                case 'W':
                    e -= int(l[1:])
                    ew -= int(l[1:])
                case 'L':
                    h = (h + int(l[1:]) // 90) % 4
                    ew, nw = rotate_around_origin((ew, nw), l.strip())
                case 'R':
                    h = (h - int(l[1:]) // 90) % 4
                    ew, nw = rotate_around_origin((ew, nw), l.strip())
                case 'F':
                    n += (1 if h == 1 else -1 if h == 3 else 0) * int(l[1:])
                    e += (1 if h == 0 else -1 if h == 2 else 0) * int(l[1:])
                    n2 += nw * int(l[1:])
                    e2 += ew * int(l[1:])
    print('1:', abs(n) + abs(e))
    print('2:', abs(n2) + abs(e2))