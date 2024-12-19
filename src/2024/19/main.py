def count_ways(patterns, string):
    n = len(string)
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        for pattern in patterns:
            if i >= len(pattern) and string[i - len(pattern):i] == pattern:
                dp[i] += dp[i - len(pattern)]

    return dp[n]

if __name__ == '__main__':
    with open('input.txt') as f:
        pat = [x.strip() for x in f.readline().split(',')]
        towel = []
        f.readline()
        while line := f.readline():
            towel.append(line.strip())

    count = 0
    ways = 0
    for t in towel:
        if w := count_ways(pat, t):
            count += 1
            ways += w

    print('1:', count)
    print('2:', ways)
