def combat(d1, d2):
    while len(decks[0]) > 0 and len(decks[1]) > 0:
        if d1[0] > d2[0]:
            d1.extend((d1.pop(0), d2.pop(0)))
        else:
            d2.extend((d2.pop(0), d1.pop(0)))


def recursive_combat(d1, d2):
    seen = set()
    while len(d1) > 0 and len(d2) > 0:
        if tuple(d1) in seen:
            return True
        seen.add(tuple(d1))
        c1, c2 = d1.pop(0), d2.pop(0)
        if len(d1) >= c1 and len(d2) >= c2:
            p1_win = recursive_combat(d1[:c1], d2[:c2])
        else:
            p1_win = c1 > c2
        if p1_win:
            d1.extend((c1, c2))
        else:
            d2.extend((c2, c1))
    return p1_win


def score(d1, d2):
    s = 0
    for i, c in enumerate((d1 if len(d1) > 0 else d2)[::-1]):
        s += (i + 1) * c
    return s


if __name__ == '__main__':
    decks = ([], [])
    index = 0
    with open('input.txt') as f:
        for line in f:
            line = line.strip()
            if line.isdigit():
                decks[index].append(int(line))
            elif line == 'Player 2:':
                index += 1

    decks2 = (decks[0].copy(), decks[1].copy())
    combat(*decks)

    print('1:', score(*decks))

    recursive_combat(*decks2)
    print('2:', score(*decks2))
