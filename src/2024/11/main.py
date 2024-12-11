from collections import defaultdict


def run_once(count_dict):
    out_dict = defaultdict(int)
    for key, val in count_dict.items():
        if key == 0:
            out_dict[1] += val
        elif (m := len(ns := str(key))) % 2 == 0:
            m //= 2
            out_dict[int(ns[:m])] += val
            out_dict[int(ns[m:])] += val
        else:
            out_dict[key * 2024] += val

    return out_dict


def simulate(s, n):
    count_dict = defaultdict(int)
    for x in s:
        count_dict[x] += 1
    for _ in range(n):
        count_dict = run_once(count_dict)
    return sum(count_dict.values())


if __name__ == '__main__':
    with open('input.txt') as f:
        stones = [int(s) for s in list(f.readline().strip().split())]

    print('1:', simulate(stones, 25))
    print('2:', simulate(stones, 75))
