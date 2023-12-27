import numpy as np


if __name__ == '__main__':
    rules = []
    my_ticket = 0
    with open('input.txt') as f:
        state = 0
        tickets = []
        skip = 0
        for line in f:
            if skip > 0:
                skip -= 1
                continue
            if line.strip() == '':
                skip = 1
                state += 1
            elif state == 0:
                tok = line.split()
                rules.append([tuple(map(int, t.split('-'))) for t in tok[-3::2]])
            elif state == 1:
                my_ticket = tuple(map(int, line.strip().split(',')))
            elif state == 2:
                if line.strip() != '':
                    tickets.append(tuple(map(int, line.strip().split(','))))

        errors = []
        to_remove = []
        for i, t in enumerate(tickets):
            for f in t:
                s = False
                for r in rules:
                    for r2 in r:
                        if r2[0] <= f <= r2[1]:
                            s = True
                if not s:
                    errors.append(f)
                    to_remove.append(i)

        print('1:', sum(errors))

        for i in to_remove[::-1]:
            del tickets[i]

        m = np.array(tickets)
        sat = []
        for r in rules:
            sat.append([])
            for c in range(m.shape[1]):
                z = m[:, c]
                x = z[((z >= r[0][0]) & (z <= r[0][1]) | ((z >= r[1][0]) & (z <= r[1][1])))]
                sat[-1].append(len(x))
        sat = np.array(sat)

        col = []
        while not np.all((sat == len(tickets)) | (sat == 0)):
            full = np.sum(sat == len(tickets), axis=1)
            min_con = np.argmin(full)
            c = np.argmax(sat[min_con])
            col.append((c, min_con))
            sat[min_con] = len(tickets)
            sat[:, c] = 0

        col = sorted(col, key=lambda tup: tup[1])

        print('2:', np.prod([my_ticket[c[0]] for c in col[:6]]))

