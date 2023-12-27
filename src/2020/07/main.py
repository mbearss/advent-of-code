if __name__ == '__main__':
    c = {}
    g = {}
    d = set()
    with open('input.txt') as f:
        for line in f:
            tokens = line.split()
            outer = ' '.join(tokens[0:2])
            n = [int(x) if x != 'no' else 0 for x in tokens[4::4]]
            t = zip([x for x in tokens[5::4]], [x for x in tokens[6::4]])
            t = [l for sub in [[' '.join(x)] * n[i] for i, x in enumerate(t)] for l in sub]
            c[outer] = t

    p = {k: 0 for k in c}
    g = {k: False for k in c}
    for k, v in c.items():
        if 'shiny gold' in v:
            g[k] = True
        if len(v) == 0:
            d.add(k)

    while len(d) != len(c):
        for k, v in c.items():
            if k not in d:
                for b in v:
                    if b in d:
                        p[k] += p[b] + 1
                        g[k] |= g[b]
                        v.remove(b)
                    if len(v) == 0:
                        d.add(k)

    print('1:', sum(g.values()))
    print('2:', p['shiny gold'])
