from itertools import combinations

if __name__ == '__main__':
    data = []
    with open('input.txt') as f:
        for line in f:
            data.append(int(line))

    for i in range(25, len(data)):
        c = set([sum(x) for x in combinations(data[i - 25:i], 2)])
        if data[i] not in c:
            p1 = data[i]

    p2 = None
    for w in range(2, len(data) + 1):
        if p2 is not None:
            break
        for i in range(len(data) - w):
            if sum(data[i:i+w]) == p1:
                p2 = min(data[i:i + w]) + max(data[i:i + w])
                break

    print('1:', p1)
    print('2:', p2)
