def run(cups, num_iters):
    next = list(range(1, len(cups) + 2))
    N = max(cups)
    for i, label in enumerate(cups[:-1]):
        next[label] = cups[i + 1]

    head = cups[0]
    next[cups[-1]] = head

    for i in range(num_iters):
        cur = next[head]
        next[head] = next[next[next[cur]]]
        pick = cur, next[cur], next[next[cur]]

        dest = head - 1 if head > 1 else N
        while dest in pick:
            dest = N if dest == 1 else dest - 1

        next[next[next[cur]]] = next[dest]
        next[dest] = cur

        head = next[head]

    cup = next[1]
    while cup != 1:
        yield cup
        cup = next[cup]


if __name__ == '__main__':
    with open('input.txt') as f:
        cups = [int(c) for c in f.read()]

    print('1:', ''.join([str(c) for c in run(cups, 100)]))

    with open('input.txt') as f:
        cups = [int(c) for c in f.read()]
    cups.extend(range(max(cups) + 1, 1_000_001))

    r = run(cups, 10_000_000)
    print('2:', next(r) * next(r))
