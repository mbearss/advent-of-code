def itr(x):
    x = ((x * 64) ^ x) % 16777216
    x = ((x // 32) ^ x) % 16777216
    return ((x * 2048) ^ x) % 16777216


if __name__ == '__main__':
    nums = []
    with open('input.txt', 'r') as f:
        for line in f:
            nums.append(int(line.strip()))

    p1, p2 = 0, dict()
    for n in nums:
        seen = set()
        last4 = (10, 10, 10, 10)
        for _ in range(2000):
            prev = n % 10
            n = itr(n)
            last4 = last4[1:] + (n % 10 - prev,)
            if last4 not in seen:
                seen.add(last4)
                p2[last4] = p2.get(last4, 0) + n % 10
        p1 += n

    print('1:', p1)
    print('2:', max(p2.values()))
