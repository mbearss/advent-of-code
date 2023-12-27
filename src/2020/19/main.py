def match(line, s, e, n):
    if (s, e, n) in M:
        return M[(s, e, n)]
    f = False
    if n in T:
        f = line[s:e] == T[n]
    else:
        for pos in R[n]:
            if match_list(line, s, e, pos):
                M[(s, e, n)] = True
                return True
    M[(s, e, n)] = f
    return f


def match_list(line, s, e, options):
    if s == e and not options:
        return True
    elif s == e or not options:
        return False

    for i in range(s + 1, e + 1):
        if i == e and len(options) > 1:
            continue
        if match(line, s, i, options[0]) and match_list(line, i, e, options[1:]):
            return True
    return False


R, T, M = {}, {}, {}
if __name__ == '__main__':
    messages = []
    with open('input.txt') as f:
        for line in f:
            if ':' in line:
                tok = line.split()
                n = tok[0][:-1]
                r = ' '.join(tok[1:])
                if '\"' in r:
                    T[n] = r[1:-1]
                else:
                    R[n] = [p.split(' ') for p in r.split(' | ')]
            elif line:
                messages.append(line.strip())

    valid = 0
    for m in messages:
        M.clear()
        if match(m, 0, len(m), '0'):
            valid += 1

    print('1:', valid)

    R['8'] = [['42'], ['42', '8']]
    R['11'] = [['42', '31'], ['42', '11', '31']]

    valid = 0
    for m in messages:
        M.clear()
        if match(m, 0, len(m), '0'):
            valid += 1

    print('2:', valid)